from django.contrib import admin
from .models import ContactForm


# Register your models here.
class ContactFormAdmin(admin.ModelAdmin):

    list_display = ('name', 'message', 'sent_on', 'read',)
    list_filter = ('sent_on', 'read',)


admin.site.register(ContactForm, ContactFormAdmin)
