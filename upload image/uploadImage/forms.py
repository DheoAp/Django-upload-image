from django.forms import ModelForm

from .models import Upload

class UplaodForm(ModelForm):
    class Meta:
        model = Upload
        fields = '__all__'

