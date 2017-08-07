from django.core.files.base import File
from django.shortcuts import render, redirect
from main.forms import AudioflForm
from main.models import Audiofl


def model_form_upload(request):
    if request.method == 'POST':
        form = AudioflForm(request.POST, request.FILES)
        if form.is_valid():
            newform = form.save(commit=False)
            djfile = File(request.FILES['data_blob'])
            newform.fl.save(request.FILES['data_blob'].name, djfile)
            newform.save()
            return redirect('/')
    else:
        form = AudioflForm()
    return render(request, 'model_form_upload.html', {
        'form': form
    })


def list_files(request):
    files = Audiofl.objects.all().order_by('uploaded_at')

    return render(request, 'list_files.html', {
        'files': files
    })
