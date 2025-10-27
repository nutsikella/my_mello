from django.contrib import admin
from cats.models import Cat, Breed

class BreedAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class CatAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'breed', 'weight', 'foods')
    list_filter = ('breed',)
    search_fields = ('nickname', 'foods')
    raw_id_fields = ('breed',)

admin.site.register(Breed, BreedAdmin)
admin.site.register(Cat, CatAdmin)