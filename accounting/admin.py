from django.contrib import admin

from accounting.models import Bill, Payment

# Register your models here.

admin.site.register(Bill)
admin.site.register(Payment)