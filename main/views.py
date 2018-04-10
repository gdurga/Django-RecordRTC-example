import os
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

            # convert to fix the duration of audio
            file_path = newform.fl.path
            os.system(
                "/usr/bin/mv %s %s" % (
                    file_path, (file_path + '.original'))
            )
            os.system(
                "/usr/bin/ffmpeg -i %s -c copy -fflags +genpts %s" % (
                    (file_path + '.original'), file_path)
            )

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
