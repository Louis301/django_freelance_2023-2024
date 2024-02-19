from django import forms
from main_app.models import Track


class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ('track',)


