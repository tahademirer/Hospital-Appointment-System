from django.conf.urls import url
from . import views
from django.urls import path
from .views import list_of_appointments, list_of_patients, add_appointment, list_of_doctors, list_of_viewAppointments, \
    list_of_searchPatients, list_of_messages, list_of_hospitals, list_of_recipes, AppointmentHistory

app_name = 'appointments'

urlpatterns = [
    # url(r'^$', views.appointment_list, name="list"),
    # url(r'^(?P<DoctorName>[\w-]+)/$', views.appointment_details, name="detail"),
    # path('appointment_list', list_of_appointments.as_view(), name="appointment_list")
    url(r'^appointment_list/$', list_of_appointments.as_view(), name='list1'),
    url(r'^patient_list/$', list_of_patients.as_view(), name='list2'),
    url(r'^doctors_list/$', list_of_doctors.as_view(), name='list3'),
    url(r'^view_appointments/$', list_of_viewAppointments.as_view(), name='list4'),
    url(r'^search_patients/$', list_of_searchPatients.as_view(), name='list5'),
    url(r'^check_messages/$', list_of_messages.as_view(), name='list6'),
    url(r'^hospital_list/$', list_of_hospitals.as_view(), name='list7'),
    url(r'^list_prescriptions/$', list_of_recipes.as_view(), name='list8'),
    url(r'add-appointment/$', views.add_appointment, name='add_appointment'),
    path('', views.AppointmentListView.as_view(), name='appointments_changelist'),
    path('add/', views.AppointmentCreateView.as_view(), name='person_add'),
    path('<int:pk>/', views.AppointmentUpdateView.as_view(), name='person_change'),
    path('ajax/load-districts/', views.load_districts, name='ajax_load_districts'),
    path('history/', views.AppointmentHistory.as_view(), name='appointment_history'),
]
