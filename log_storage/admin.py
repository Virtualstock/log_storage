from django.contrib import admin
from .models import Log


class LogAdmin(admin.ModelAdmin):
    readonly_fields = ('log_data', 'db_log_data', 'filename', 'save_file',)
    list_display = ('filename', 'created', 'save_file',)
    list_filter = ('created', 'save_file',)
    search_fields = ('filename',)


admin.site.register(Log, LogAdmin)

