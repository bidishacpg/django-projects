from django.contrib import admin
from contact.models import Contact
class contactadmin(admin.ModelAdmin):
    list_display=('username','email','mobile','feedback')
admin.site.register(Contact,contactadmin)