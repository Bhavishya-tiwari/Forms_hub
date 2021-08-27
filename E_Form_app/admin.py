from django.contrib import admin
from E_Form_app.models import Forms,Res
# Register your models here.
@admin.register(Forms)
class PostAdmin(admin.ModelAdmin):
    list_display =['fno']
@admin.register(Res)
class PostAdmin(admin.ModelAdmin):
    list_display =['idd']