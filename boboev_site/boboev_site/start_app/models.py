from django.db import models


class Feedback(models.Model):
	
	fullname = models.CharField('Полное имя', max_length=40)
	age = models.IntegerField('Возраст')
	sex = models.CharField('Пол', max_length=5)
	message = models.CharField('Сообщение', max_length=40)

	def __str__(self):
		return self.fullname + ', ' + str(self.age) + ', ' + self.sex + ', ' + self.message
	

class AlumniReviews(models.Model):

	fullname = models.CharField('Полное имя', max_length=40)
	group = models.CharField('Группа', max_length=10)
	release_year = models.DateField('Выпуск')
	feedback_text = models.CharField('Отзыв', max_length=400)
	slogan = models.CharField('Слоган', max_length=100, default='default')

	def __str__(self):

		result = f"""
			{self.fullname},
			группа: {self.group} (выпуск {self.release_year}),
			{self.slogan}
		"""
		return result