from django.forms import ModelForm
from app_test.models import *

# Create the form class.
class Tabla01Form(ModelForm):
    class Meta:
        model = Tabla01
        exclude = ['created_by','modified_by',]