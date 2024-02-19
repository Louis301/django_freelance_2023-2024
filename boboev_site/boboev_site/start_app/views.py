from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from .models import Feedback, AlumniReviews


class IndexView(View):
    def get(self, request):
        alumni_reviews = AlumniReviews.objects.all()
        return render(request, 'start.html', {'alumni_review' : alumni_reviews[0]})
    
    def post(self, request):
        if request.POST.get('send') == 'Отправить':
            feedback = Feedback()
            feedback.fullname = request.POST.get('fullname')
            feedback.age = request.POST.get('age')
            feedback.sex = request.POST.get('sex')
            feedback.message = request.POST.get('message')
            feedback.save()
            return HttpResponseRedirect('/#openModal')


class ProgramView(View):
    def get(self, request):
        return render(request, 'program.html')
    

class ReviewsView(View):

    def get(self, request):
        return render(request, 'reviews.html', {'alumni_reviews' : AlumniReviews.objects.all()})
    
    def post(self, request):
        if request.POST.get('send') == 'Отправить':
            ar = AlumniReviews()
            ar.fullname = request.POST.get('fullname')
            ar.group = request.POST.get('group')
            ar.release_year = request.POST.get('release_year')
            ar.feedback_text = request.POST.get('feedback_text')
            ar.slogan = request.POST.get('slogan')
            ar.save()
            return render(request, 'reviews.html', {'alumni_reviews' : AlumniReviews.objects.all()})
    