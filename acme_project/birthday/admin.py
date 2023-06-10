from django.contrib import admin

# Из модуля models импортируем модель Category...
from .models import Birthday, Tag

admin.site.register(Birthday)
admin.site.register(Tag)
