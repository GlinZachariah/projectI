from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
# Create your views here.
import pandas
import os
import result_main
from django.views.generic.list import ListView

def index(request):
    return HttpResponse("Hello, world. You're at the viewresults page.")

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'simple_upload.html')

def make_result(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        
        result_main.res_gen(uploaded_file_url)
        return render(request, 'simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'simple_upload.html')
    # return HttpResponse("Hello, world. You're at the make_results page.")

def dir_view(request):
    syspath =os.path.dirname(os.path.realpath(__file__))
    syspath = syspath.replace('\\', '/')
    path=syspath+"/../media/output/"
    class FileObject():
        name = ''
        def __init__(self, name):
            self.name = name
    files = []
    filenames={}
    for filename in os.listdir(path):
        fileobject = FileObject(name=filename)
        files.append(fileobject)
        filenames[filename]= "file:///"+path+filename
        # print(filenames)
    # return files
    return render(request, 'list_dir.html', {
        'files': filenames
    })

    # return render(request, 'list_dir.html')