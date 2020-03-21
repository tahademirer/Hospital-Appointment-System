from django.contrib.auth.models import AbstractUser, User, Group
from django.db import models
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver

Roles = (
    ('admin', 'ADMIN'),
    ('doctor', 'DOCTOR'),
    ('patient', 'PATIENT'),
    ('visitor', 'VISITOR'),
)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, null=True)
    role = models.CharField(max_length=50, choices=Roles, default='client')


class Province(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=30)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Hospitals(models.Model):
    name = models.CharField(max_length=100)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    numBeds = models.CharField(max_length=5)
    numRooms = models.CharField(max_length=5)

    def __str__(self):
        return self.name


class Departments(models.Model):
    name = models.CharField(max_length=80)
    hospital = models.ForeignKey(Hospitals, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    # ID , gsm, address, e-mail, title
    user = models.OneToOneField(User, on_delete=models.CASCADE, default="")
    name = models.CharField(max_length=50, default='')
    gsm = models.CharField(max_length=11)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    title = models.CharField(max_length=20)
    department = models.CharField(max_length=100)
    hospital = models.ForeignKey(Hospitals, on_delete=models.CASCADE, blank=True, null=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Doctor.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.doctor.save()

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse("")


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default="", editable=False)
    tckno = models.CharField(max_length=12, default="tck")
    name = models.CharField(max_length=50)
    gsm = models.CharField(max_length=11)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    age = models.CharField(max_length=3)
    gender = models.CharField(max_length=1)

    def __str__(self):
        return self.name

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Patient.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.patient.save()


class Comments(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    message = models.TextField()


class Day(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()


class Slot(models.Model):
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    slot1 = models.BooleanField(default=False)
    slot2 = models.BooleanField(default=False)
    slot3 = models.BooleanField(default=False)
    slot4 = models.BooleanField(default=False)
    slot5 = models.BooleanField(default=False)
    slot6 = models.BooleanField(default=False)
    slot7 = models.BooleanField(default=False)
    slot8 = models.BooleanField(default=False)


class Prescription(models.Model):
    patientName = models.ForeignKey(Patient, on_delete=models.CASCADE)
    diagnosis = models.CharField(max_length=50)
    recipe = models.TextField()
