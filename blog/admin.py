from django.contrib import admin
from blog.models import makale

class MakaleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("baslik",)}

admin.site.register(makale)