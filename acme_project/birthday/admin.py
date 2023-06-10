from django.contrib import admin

# Из модуля models импортируем модель Category...
from .models import Birthday

admin.site.register(Birthday) 