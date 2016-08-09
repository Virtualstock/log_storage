from django.contrib import admin
from .models import Log

class LogAdmin(admin.ModelAdmin):
    readonly_fields = ('log_data', )

admin.site.register(Log, LogAdmin)

