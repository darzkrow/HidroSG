from django import forms
from .models import Visitors, AccessSEDE
from django.core.validators import RegexValidator

# Define un formulario personalizado para Visitors

class VisitanteForms(forms.ModelForm):
    dni_validator = RegexValidator(r'^\d{6,10}$', 'Ingrese solo números válidos con un mínimo de 6 dígitos.')
    name_validator = RegexValidator(r'^[a-zA-ZáéíóúÁÉÍÓÚ\s]+$', 'Ingrese solo letras válidas para el nombre.')

    class Meta:
        model = Visitors
        fields = ['Nac', 'Dni', 'First_name', 'Last_name', 'gender', 'photo']
        widgets = {
            'Nac': forms.Select(attrs={'class': 'form-select'}),
            'Dni': forms.TextInput(attrs={'class': 'form-control'}),
            'First_name': forms.TextInput(attrs={'class': 'form-control'}),
            'Last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'photo': forms.FileInput(attrs={'accept': 'image/*', 'capture': 'camera'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Dni'].validators.append(self.dni_validator)
        self.fields['First_name'].validators.append(self.name_validator)
        self.fields['Last_name'].validators.append(self.name_validator)
        
        # Deshabilitar los campos Dni y photo si ya existe una instancia
        if self.instance.pk:
            self.fields['Dni'].disabled = True
            self.fields['photo'].disabled = True

    # Sobrescribe el método clean para mostrar errores personalizados
    def clean(self):
        cleaned_data = super().clean()
        dni = cleaned_data.get('Dni')
        if dni and not dni.isdigit():
            self.add_error('Dni', 'Ingrese solo números válidos con un mínimo de 6 dígitos.')
        return cleaned_data

class AccessSEDEForm(forms.ModelForm):
    class Meta:
        model = AccessSEDE
        fields =  ['entry','hours','hoursEx','Automovils','Licenses','obs']
        widgets = {
            'entry': forms.DateInput(attrs={'type': 'date','class': 'form-control'}),
            'hours': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'hoursEx': forms.TimeInput(attrs={'type': 'time','class': 'form-control'}),
            'Automovils': forms.Select(attrs={'class': 'form-control'}),
            'Licenses': forms.TextInput(attrs={'class': 'form-control'}),
            'obs': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
           
        }


class SearchForm(forms.Form):
    dni = forms.CharField(label='Buscar por DNI', max_length=10)