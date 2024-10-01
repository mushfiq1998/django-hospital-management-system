from django import forms
from .models import Patient, Employee, Doctor, Appointment, Ward, Bed

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'date_of_birth', 'gender', 
                  'phone_number', 'email', 'address', 'photo', 'patient_type']

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'position', 'department', 'phone_number', 'email', 'photo']

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'specialization', 'phone_number', 'photo']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient', 'doctor', 'date', 'time', 'reason']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

class WardForm(forms.ModelForm):
    class Meta:
        model = Ward
        fields = ['name', 'capacity']

class BedForm(forms.ModelForm):
    class Meta:
        model = Bed
        fields = ['number', 'ward', 'is_occupied']
        widgets = {
            'number': forms.TextInput(attrs={'class': 'form-control'}),
            'ward': forms.Select(attrs={'class': 'form-control'}),
            'is_occupied': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }