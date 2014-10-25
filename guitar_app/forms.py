from django.forms import ModelForm, BooleanField
import models

class GuitarAddForm(ModelForm):
    class Meta:
        model = models.Guitar
        fields = '__all__'
        exclude = ['id']