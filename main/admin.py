from django.contrib import admin

# Register your models here.
from .forms import InputForm
from .models import Input, Doctor


class InputAdmin(admin.ModelAdmin):
	list_display  = ["__unicode__", "timestamp"]
	form = InputForm

class DoctorAdmin(admin.ModelAdmin):
	pass

admin.site.register(Input, InputAdmin)
admin.site.register(Doctor, DoctorAdmin)