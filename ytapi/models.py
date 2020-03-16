from django.db import models

#model oluşturuldu

# Create your models here.
class TranslateTable(models.Model):
    input_word = models.CharField(max_length = 50,verbose_name = "input_word")
    output_word = models.CharField(max_length = 50,verbose_name = "output_word")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name = "Olusturulma_tarihi")
    def __str__(self):
        return self.input_word
    class Meta:
        #Sıralaması
        ordering = ['-created_date']