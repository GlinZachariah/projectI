from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
# Create your views here.
import pandas as pd
import numpy as np
import os
import result_main
import csv
from django.utils.encoding import smart_str


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

def download_file(request,subject_code='None'):
    syspath =os.path.dirname(os.path.realpath(__file__))
    syspath = syspath.replace('\\', '/')
    path=syspath+"/../media/output/"

    if subject_code !=None:
        with open(path+subject_code, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type='text/csv')
            response['Content-Disposition'] = 'inline; filename=' + subject_code
            return response
    class FileObject():
        name = ''
        def __init__(self, name):
            self.name = name
    files = []
    filenames={}
    for filename in os.listdir(path):
        fileobject = FileObject(name=filename)
        files.append(fileobject)
        filenames[filename]= filename
    return render(request, 'list_dir.html', {
        'files': filenames,
        'subcode' : subject_code
    })

def display(request,filename):
    syspath =os.path.dirname(os.path.realpath(__file__))
    syspath = syspath.replace('\\', '/')
    path=syspath+"/../media/output/"
    url =path+filename
    df =pd.read_csv(url)
    df =df.replace(np.nan, df.replace([np.nan], ['-']))
    colnames =list(df.columns.values)
    count =len(colnames)
    table_idx =[]
    for i in range(count):
        table_idx.append(i)
    df=df.iloc[:, :-1]
    return render(request, 'viewtable.html', {
        'colnames':colnames,
        'dataframe': df,
        'index': table_idx
    })