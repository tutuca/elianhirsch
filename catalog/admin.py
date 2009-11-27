from django.contrib import admin
from models import Serie, Category, Foto

class FotoInLine(admin.TabularInline):
    model = Foto
    extra = 1

class SerieAdmin(admin.ModelAdmin):
    inlines = [FotoInLine]

admin.site.register(Serie, SerieAdmin)
admin.site.register(Category)
admin.site.register(Foto)
