from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import FilesForm
from django.http import HttpResponseRedirect
from django.templatetags.static import static
from .primer_checker import primer_checker
from .models import AvailablePrimers, UnavailablePrimers, ResultFiles
import csv
import os


def index(request):
    if request.method == 'POST':
        form = FilesForm(request.POST, request.FILES)
        if form.is_valid():
            new_upload = ResultFiles(vcf=request.FILES['vcf'], bed=request.FILES['bed'])
            new_upload.save()
        return redirect('results')
    else:
        form = FilesForm()
    return render(request, 'pricheck/index.html', {'form': form})


def results(request):
    getFiles = ResultFiles.objects.last()
    vcf = open(str(getFiles.vcf))
    bed = open(str(getFiles.bed))
    with_p, without_p = primer_checker(vcf, bed)
    return render(request, 'pricheck/results.html', {'with_p': with_p, 'without_p': without_p})
