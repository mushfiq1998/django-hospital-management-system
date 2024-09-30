from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Patient, Employee, Doctor, Appointment
from .forms import PatientForm, EmployeeForm, DoctorForm, AppointmentForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Dashboard View
@login_required
def dashboard(request):
    employees_count = Employee.objects.count()
    patients_count = Patient.objects.count()
    indoor_patients_count = Patient.objects.filter(patient_type='indoor').count()
    outdoor_patients_count = Patient.objects.filter(patient_type='outdoor').count()
    doctors_count = Doctor.objects.count()
    appointments_count = Appointment.objects.count()
    context = {
        'employees_count': employees_count,
        'patients_count': patients_count,
        'indoor_patients_count': indoor_patients_count,
        'outdoor_patients_count': outdoor_patients_count,
        'doctors_count': doctors_count,
        'appointments_count': appointments_count,
    }
    return render(request, 'hospital/dashboard.html', context)

def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}. You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'hospital/register.html', {'form': form})

def user_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome, {username}! You have been logged in.")
                return redirect('dashboard')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'hospital/login.html', {'form': form})

def user_logout(request):
    username = request.user.username
    logout(request)
    messages.success(request, f"Goodbye, {username}! You have been logged out.")
    return redirect('login')

# .......................................................................
# Patient Views ..........................................................
@login_required
def patient_list(request):
    patient_type = request.GET.get('type', 'all')
    if patient_type == 'indoor':
        patients = Patient.objects.filter(patient_type='indoor')
    elif patient_type == 'outdoor':
        patients = Patient.objects.filter(patient_type='outdoor')
    else:
        patients = Patient.objects.all()
    context = {'patients': patients, 'current_type': patient_type}
    return render(request, 'hospital/patient_list.html', context)

@login_required
def patient_add(request):
    if request.method == 'POST':
        form = PatientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()
    return render(request, 'hospital/patient_form.html', {'form': form})

@login_required
def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    context = {'patient': patient}
    return render(request, 'hospital/patient_detail.html', context)

@login_required
def patient_edit(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        form = PatientForm(request.POST, request.FILES, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'hospital/patient_form.html', {'form': form})

def delete_object(request, model, pk, redirect_url):
    obj = get_object_or_404(model, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect(redirect_url)
    context = {
        'object': obj,
        'cancel_url': reverse(redirect_url)
    }
    return render(request, 'hospital/confirm_delete.html', context)

@login_required
def patient_delete(request, pk):
    return delete_object(request, Patient, pk, 'patient_list')

# .......................................................................
# Employee Views 
@login_required
def employee_list(request):
    employees = Employee.objects.all()
    context = {'employees': employees}
    return render(request, 'hospital/employee_list.html', context)

@login_required
def employee_add(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'hospital/employee_form.html', {'form': form})

@login_required
def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    context = {'employee': employee}
    return render(request, 'hospital/employee_detail.html', context)

@login_required
def employee_edit(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'hospital/employee_form.html', {'form': form})

@login_required
def employee_delete(request, pk):
    return delete_object(request, Employee, pk, 'employee_list')

@login_required
def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'hospital/employee_form.html', {'form': form})


# .......................................................................
# Doctor Views ..........................................................
@login_required
def doctor_list(request):
    doctors = Doctor.objects.all()
    context = {'doctors': doctors}
    return render(request, 'hospital/doctor_list.html', context)

@login_required
def doctor_add(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = DoctorForm()
    return render(request, 'hospital/doctor_form.html', {'form': form})

@login_required
def doctor_detail(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    context = {'doctor': doctor}
    return render(request, 'hospital/doctor_detail.html', context)

@login_required
def doctor_edit(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'hospital/doctor_form.html', {'form': form})

@login_required
def doctor_delete(request, pk):
    return delete_object(request, Doctor, pk, 'doctor_list')

@login_required
def doctor_create(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = DoctorForm()
    return render(request, 'hospital/doctor_form.html', {'form': form})


# ......................................................................
# Appointment Views ....................................................
@login_required
def appointment_list(request):
    appointments = Appointment.objects.all()
    context = {'appointments': appointments}
    return render(request, 'hospital/appointment_list.html', context)

@login_required
def appointment_add(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'hospital/appointment_form.html', {'form': form})

@login_required
def appointment_detail(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    context = {'appointment': appointment}
    return render(request, 'hospital/appointment_detail.html', context)

@login_required
def appointment_edit(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'hospital/appointment_form.html', {'form': form})

@login_required
def appointment_delete(request, pk):
    return delete_object(request, Appointment, pk, 'appointment_list')
