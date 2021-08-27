from django.contrib import admin
from E_Form_app.models import Forms
# Register your models here.
@admin.register(Forms)
class PostAdmin(admin.ModelAdmin):
    list_display =['fno']
