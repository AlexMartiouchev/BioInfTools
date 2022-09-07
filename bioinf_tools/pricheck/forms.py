from django import forms


class FilesForm(forms.Form):
    vcf = forms.FileField(label='Select a vcf file')
    bed = forms.FileField(label='Select a bed file')