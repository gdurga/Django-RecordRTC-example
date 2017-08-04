from django.http import HttpResponse
from django.shortcuts import render, redirect
from main.forms import AudioflForm
from django.core.files.base import File
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def model_form_upload(request):
    from django.core.files.storage import FileSystemStorage
    if request.method == 'POST':
        form = AudioflForm(request.POST, request.FILES)
        if form.is_valid():
            novo = form.save(commit=False)
            djfile = File(request.FILES['data'])
            novo.foto.save(request.FILES['data'].name, djfile)
            novo.save()
            return redirect('/up')
    else:
        form = AudioflForm()
    return render(request, 'model_form_upload.html', {
        'form': form
    })
