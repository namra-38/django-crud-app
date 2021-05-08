from django import forms
from .models import Employe

class EmployeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EmployeForm, self).__init__(*args, **kwargs)
        
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class' : 'form-control',
            })

    class Meta:
        model = Employe
        fields = ('__all__')
