from django.contrib import admin
# modelden eklendi
from .models import TranslateTable

# Register your models here.
@admin.register(TranslateTable)
class TranslateTableAdmin(admin.ModelAdmin):
    list_display = ["id","input_word","output_word","created_date"]
    list_filter = ["created_date"]
    class Meta:
        model = TranslateTable
