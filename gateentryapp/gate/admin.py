from __future__ import unicode_literals
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import*

@admin.register(Invoice)
class InvoiceAdmin(ImportExportModelAdmin):
    pass
