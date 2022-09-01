from django.contrib import admin
from .models import Contact

# Register your models here.
class Comment(admin.ModelAdmin):
    admin.site.site_header = "kiita leaning service"
    admin.site.site_title = "Cleaner Serviecs"
    admin.site.site_title = "Cleaning  Serviecs"
    list_display = ('name','email','phone','message')
    list_editable = ('email','phone')






admin.site.register(Contact,Comment)
























