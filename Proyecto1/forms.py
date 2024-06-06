# forms.py

from django import forms
from .models import Paciente, Medico, Turno

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'apellido', 'correo']

class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ['nombre', 'apellido', 'matricula']

class TurnoForm(forms.ModelForm):
    class Meta:
        model = Turno
        fields = ['mailPaciente', 'matriculaMedico', 'fecha', 'hora']
