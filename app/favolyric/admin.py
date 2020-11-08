from django.contrib import admin
from .models import Views


@admin.register(Views)
class Views(admin.ModelAdmin):
    pass
