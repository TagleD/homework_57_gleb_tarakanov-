from django.contrib import admin
from webapp.models import Task


# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    list_filter = ('id', 'title', 'description')
    search_fields = ('id', 'title', 'description')
    fields = ('id', 'title', 'description')
    readonly_fields = ('id', 'title', 'description')


admin.site.register(Task, TaskAdmin)
