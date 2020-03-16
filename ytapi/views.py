from django.shortcuts import render,HttpResponse,redirect
from ytapi.forms import TranslateTableForm
from ytapi.models import TranslateTable
from ytapi import myfunc


# Create your views here.

def index(request):
    "Post/Redirect/Get Kullanılmışştır"
    #return HttpResponse("Anasayfa")
    #return render(request,"index.html",{"number":"1"})
    #Render edilecek öğelerin oluşturulması 
    allsearch = TranslateTable.objects.all()
    translated_data = TranslateTable.objects.all().first()
    form = TranslateTableForm(request.POST or None)
    #formu kontol ediyor clean medhodu gibi
    if form.is_valid():
        #Normalde otomatik kayıteder ve commit eder ama durduruyoruz, özellik ekleyeceğiz.
        translated_data = form.save(commit = False)
        translated_data.output_word = myfunc.translate(translated_data.input_word)
        translated_data.save()
        #ytapideki index name li funksiyona dön
        return redirect("ytapi:index")

    context = {
        "allsearch": allsearch,
        "info" :translated_data,
        "form" : form
    }

    return render(request,"index.html",context)

def deleteAllSearch(request):
    """database temizleme işlemi"""
    TranslateTable.objects.all().delete()
    return redirect("ytapi:index")
