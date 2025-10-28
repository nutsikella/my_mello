from django.contrib import admin
from ads.models import Ad

@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'owner', 'created_at']
    list_filter = ['created_at', 'owner']
    search_fields = ['title', 'text']