from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Employee(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100, null=True, blank=True)
    department = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    photo = models.ImageField(upload_to='employee_photos/', null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.position}"


class Ward(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name


class Bed(models.Model):
    number = models.CharField(max_length=10)
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE, related_name='beds')
    is_occupied = models.BooleanField(default=False)

    def __str__(self):
        return f"Bed {self.number} in {self.ward.name}"


class Patient(models.Model):
    PATIENT_TYPES = [
        ('indoor', 'Indoor'),
        ('outdoor', 'Outdoor'),
    ]
    name = models.CharField(max_length=200, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True,
                    choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='patient_photos/', null=True, blank=True)
    patient_type = models.CharField(max_length=7, 
                                    choices=PATIENT_TYPES, default='outdoor')
    is_admitted = models.BooleanField(default=False)
    admission_date = models.DateTimeField(null=True, blank=True)
    discharge_date = models.DateTimeField(null=True, blank=True)
    bed = models.OneToOneField(Bed, on_delete=models.SET_NULL, 
                               null=True, blank=True, related_name='current_patient')

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=200)
    specialization = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    photo = models.ImageField(upload_to='doctor_photos/', null=True, blank=True)

    def __str__(self):
        return f"Dr. {self.name}"


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    reason = models.TextField()

    def __str__(self):
        return f"{self.patient.name} - {self.doctor.name} - {self.date} {self.time}"


class OTBooking(models.Model):
    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    scheduled_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)
    procedure = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='scheduled')
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.patient.name} - {self.procedure} - {self.scheduled_time}"

    @property
    def is_ongoing(self):
        return self.status == 'in_progress'

    @property
    def is_upcoming(self):
        return self.status == 'scheduled' and self.scheduled_time > timezone.now()


class Payroll(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    bonus = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    deductions = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    pay_date = models.DateField()
    
    def total_pay(self):
        return self.salary + self.bonus - self.deductions

    def __str__(self):
        return f"{self.employee.username} - {self.pay_date}"


class PatientBilling(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('paid', 'Paid'),
        ('unpaid', 'Unpaid'),
        ('partial', 'Partial'),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='billings')
    billing_date = models.DateTimeField(default=timezone.now)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, default='unpaid')
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Billing for {self.patient.name} - {self.billing_date.date()}"
