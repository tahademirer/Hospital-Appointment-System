from django.shortcuts import render
from .models import Appointment, Patient, Doctor, Comments, Hospitals, Prescription
from django.http import HttpResponse, HttpResponseRedirect
from .forms import AppointmentForm
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

# def appointment_list(request):
#  appointments = Appointment.objects.all().order_by('PatientName');
#  return render(request, 'appointments/appointment_list.html', {'appointments':appointments})
#
# def appointment_details(request, PatientName):
#     appointment = Appointment.objects.get(PatientName=PatientName)
#     return render(request, 'appointments/appointment_detail.html', {'appointment':appointment})

from django.views.generic import DetailView, ListView


class list_of_appointments(ListView):
    # queryset = Appointment.objects.all()
    model = Appointment
    template_name = 'appointments/appointment_list.html'


class list_of_viewAppointments(ListView):
    model = Appointment
    template_name = 'appointments/view_appointments.html'


class list_of_searchPatients(ListView):
    model = Patient
    template_name = 'appointments/search_patients.html'


class list_of_doctors(ListView):
    model = Doctor
    template_name = 'appointments/doctors_list.html'

class list_of_hospitals(ListView):
    model = Hospitals
    template_name = 'appointments/hospital_list.html'



## PATIENT LISTING AT ADMIN'S SCREEN
class list_of_patients(ListView):
    model = Patient
    template_name = 'appointments/patient_list.html'


##PATIENT LISTING  AT DOCTOR'S SECREEN

class list_of_patients2(ListView):
    model = Patient
    template_name = 'doctorPage.html'

class list_of_messages(ListView):
        model = Comments
        template_name = 'appointments/check_messages.html'


class list_of_recipes(ListView):
    model = Prescription
    template_name = 'appointments/list_prescriptions.html'

##APPOINTMENT SAVING TO DATABASE

def add_appointment(request):
    if request.method == 'POST':  # data sent by user
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            return HttpResponse('New appointment added to database')
    else:  # display empty form
        form = AppointmentForm()

    return render(request, 'appointments/add_appointment.html', {'appointment_form': form})


class AppointmentListView(ListView):
    model = Appointment
    context_object_name = 'appointments'

class AppointmentCreateView(CreateView):
    model = Appointment
    fields = ("Date", "province", "district", "hospital", "clinic", "doctor")
    success_url = reverse_lazy('patient')

    def user(request):
        Appointment.patient = request.user()

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class AppointmentUpdateView(UpdateView):
    model = Appointment
    fields = ("Date", "province", "district", "hospital", "clinic", "doctor")
    success_url = reverse_lazy('appointments_changelist')


from accounts.models import District


def load_districts(request):
    province_id = request.GET.get('province')
    districts = District.objects.filter(province_id=province_id).order_by('name')
    return render(request, 'appointments/district_dropdown_list_options.html', {'districts': districts})

class AppointmentHistory(ListView):
    context_object_name = 'appointment_history'
    template_name = 'appointment_history.html'

    def dispatch(self, *args, **kwargs):
        return super(AppointmentHistory, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        return Appointment.objects.filter(user=self.request.user)

