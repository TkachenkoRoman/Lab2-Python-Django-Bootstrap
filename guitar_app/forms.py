from django.forms import ModelForm, TextInput
import models

class GuitarAddForm(ModelForm):
    class Meta:
        model = models.Guitar
        fields = '__all__'
        exclude = ['id']

class VariablesForm(ModelForm):
    class Meta:
        model = models.Variables
        fields = ['short_name', 'value']
        widgets = {
            'short_name': TextInput(attrs={'readonly':'readonly'}),
        }
