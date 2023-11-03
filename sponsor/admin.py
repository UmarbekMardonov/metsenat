from django.contrib import admin

from .models import Sponsor


@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'full_name', 'phone_number', 'amount', 'status', 'office_name')
