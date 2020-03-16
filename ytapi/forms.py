from django import forms
from .models import TranslateTable

#MOdelform Kullanılarak form oluşturuldu
class TranslateTableForm(forms.ModelForm):
    class Meta:
        model = TranslateTable
        fields = ('input_word',)
        labels = {
            'input_word': ('Türkçe Kelimeyi Giriniz: '),
        }
        widgets = {
            'input_word': forms.TextInput(attrs={
                'autofocus':'',
                'type':'text',
                'autocomplete':'off'
                }),
        }