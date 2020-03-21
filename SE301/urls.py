from django.contrib import admin
from django.urls import path
from .views import home_view, admin_view, doctor_view, patient_view, contact_view, forget_view, news_view
from django.conf.urls import url, include
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from accounts.views import login_view, register_view, register_view2

urlpatterns = [
    path('', home_view, name='home'),
    url(r'^contact/$', contact_view, name="contact"),
    url(r'^forgetPassword/$', forget_view, name="forgetPassword"),
    path('login/', login_view),
    url(r'^news/$', news_view, name="news"),
    url(r'^signup/$', register_view, name="signup"),
    url(r'^signup2/$', register_view2, name="signup2"),
    url(r'^adminPage/$', admin_view, name="admin"),
    url(r'^doctorPage/$', doctor_view, name="doctor"),
    url(r'^patientPage/$', patient_view, name="patient"),
    path('bootstrap/', TemplateView.as_view(template_name='bootstrap/example.html')),
    path('admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^appointments/', include('appointments.urls'))
]

urlpatterns += staticfiles_urlpatterns()
