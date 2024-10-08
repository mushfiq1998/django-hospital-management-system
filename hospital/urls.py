from django.urls import path
from . import views

urlpatterns = [
    # Registration URL
    path('', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    # Dashboard URL
    path('dashboard/', views.dashboard, name='dashboard'),

    # Patient URLs
    path('patients/', views.patient_list, name='patient_list'),
    path('patients/add/', views.patient_add, name='patient_add'),
    path('patients/<int:pk>/', views.patient_detail, name='patient_detail'),
    path('patients/<int:pk>/edit/', views.patient_edit, name='patient_edit'),
    path('patients/<int:pk>/delete/', views.patient_delete, name='patient_delete'),
    path('patients/<int:pk>/admit/', views.admit_patient, name='admit_patient'),

    # Employee URLs
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/add/', views.employee_add, name='employee_add'),
    path('employees/<int:pk>/', views.employee_detail, name='employee_detail'),
    path('employees/<int:pk>/edit/', views.employee_edit, name='employee_edit'),
    path('employees/<int:pk>/delete/', views.employee_delete, name='employee_delete'),

    # Doctor URLs
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('doctors/add/', views.doctor_add, name='doctor_add'),
    path('doctors/<int:pk>/', views.doctor_detail, name='doctor_detail'),
    path('doctors/<int:pk>/edit/', views.doctor_edit, name='doctor_edit'),
    path('doctors/<int:pk>/delete/', views.doctor_delete, name='doctor_delete'),

    # Appointment URLs
    path('appointments/', views.appointment_list, name='appointment_list'),
    path('appointments/add/', views.appointment_add, name='appointment_add'),
    path('appointments/<int:pk>/', views.appointment_detail, name='appointment_detail'),
    path('appointments/<int:pk>/edit/', views.appointment_edit, name='appointment_edit'),
    path('appointments/<int:pk>/delete/', views.appointment_delete, name='appointment_delete'),

    # Ward URLs
    path('wards/', views.ward_list, name='ward_list'),
    path('wards/<int:pk>/', views.ward_detail, name='ward_detail'),
    path('wards/create/', views.ward_create, name='ward_create'),
    path('wards/<int:pk>/update/', views.ward_update, name='ward_update'),
    path('wards/<int:pk>/delete/', views.ward_delete, name='ward_delete'),

    # Bed URLs
    path('beds/', views.bed_list, name='bed_list'),
    path('beds/<int:pk>/', views.bed_detail, name='bed_detail'),
    path('beds/create/', views.bed_create, name='bed_create'),
    path('beds/<int:pk>/update/', views.bed_update, name='bed_update'),
    path('patients/<int:patient_id>/assign_bed/', views.assign_bed, name='assign_bed'),
    path('beds/<int:pk>/delete/', views.bed_delete, name='bed_delete'),

    # OT Booking URLs
    path('ot-bookings/', views.ot_booking_list, name='ot_booking_list'),
    path('ot-bookings/create/', views.ot_booking_create, name='ot_booking_create'),
    path('ot-bookings/<int:pk>/update/', views.ot_booking_update, name='ot_booking_update'),
    path('ot-bookings/<int:pk>/delete/', views.ot_booking_delete, name='ot_booking_delete'),
    path('ot-bookings/<int:pk>/', views.ot_booking_detail, name='ot_booking_detail'),

    # Account Management URLs
    path('account/', views.account_management, name='account_management'),
    path('account/change-password/', views.change_password, name='change_password'),
    path('account/profile/', views.profile, name='profile'),
    path('account/view-profile/', views.view_profile, name='view_profile'),

    # Payroll URL
    path('payroll/', views.payroll_list, name='payroll_list'),
    path('payroll/add/', views.payroll_add, name='payroll_add'),
    path('payroll/<int:pk>/edit/', views.payroll_edit, name='payroll_edit'),
    path('payroll/<int:pk>/', views.payroll_view, name='payroll_view'),
    path('payroll/<int:pk>/delete/', views.payroll_delete, name='payroll_delete'),

    # Patient Billing URLs
    path('patient-billing/', views.patient_billing_list, name='patient_billing_list'),
    path('patient-billing/add/', views.patient_billing_add, name='patient_billing_add'),
    path('patient-billing/<int:pk>/', views.patient_billing_view, name='patient_billing_view'),
    path('patient-billing/<int:pk>/edit/', views.patient_billing_edit, name='patient_billing_edit'),
    path('patient-billing/<int:pk>/delete/', views.patient_billing_delete, name='patient_billing_delete'),
]