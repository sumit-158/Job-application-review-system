from django.contrib import admin
from .models import Applicant


class APadmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "resume")
    list_display_links = ("first_name", "last_name", "email", "resume")


admin.site.register(Applicant, APadmin)
