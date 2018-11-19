from django.contrib import admin
from ToDoApp.models import ToDoList
import csv
from django.http import HttpResponse

# Register your models here.
@admin.register(ToDoList)

class UserAdmin(admin.ModelAdmin):
    readonly_fields = ("CreatedAt","ModifiedAt")
    search_fields = ('Title','Status')
    list_filter = ('CreatedAt','Status','Deadline_Date')
    actions = ['download_csv']
    
    "Function for downloading csv data"

    def download_csv(self,request,queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)
        writer.writerow(field_names)
        for s in queryset:
             writer.writerow([getattr(s, field) for field in field_names])
        return response

    download_csv.short_description = "Download CSV file for selected list."