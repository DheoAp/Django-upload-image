from django.views.generic import ListView, TemplateView, CreateView

# Create your views here.


from .models import Upload
from .forms import UplaodForm

class UploadImage(CreateView):
    form_class = UplaodForm
    template_name = 'UploadImage.html'


class SuccesImage(ListView):
    model = Upload
    template_name = 'hasil.html'
    context_object_name = 'hasil_upload'
