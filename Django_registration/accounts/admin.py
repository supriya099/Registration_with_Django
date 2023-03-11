from django.contrib import admin
from .models import User, patient, doctor

admin.site.register(User)
admin.site.register(patient)
admin.site.register(doctor)
