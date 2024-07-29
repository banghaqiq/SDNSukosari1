from django import forms
from .models import *

class DataGuruForm(forms.ModelForm):
    class Meta:
        model = DataGuru
        fields = '__all__'
        widget = {
            'image' : forms.Select(attrs={'class' : 'form-control'}),
            'nama' : forms.Select(attrs={'class' : 'form-control'}),
            'jabatan' : forms.Select(attrs={'class' : 'form-control'}),
        }

class FasilitasForm(forms.ModelForm):
    class Meta:
        model = Fasilitas
        fields = '__all__'
        widget = {
            'icon' : forms.FileInput(attrs={'class' : 'form-control'}),
            'deskripsi' : forms.Textarea(attrs={'class' : 'form-control'}),
        }

class AlumniForm(forms.ModelForm):
    class Meta:
        model = AlumniLK
        fields = '__all__'
        widget = {
            'image' : forms.FileInput(attrs={'class' : 'form-control'}),
            'deskripsi' : forms.Textarea(attrs={'class' : 'form-control'}),
            'nama' : forms.TextInput(attrs={'class' : 'form-control'}),
            'sekolah' : forms.TextInput(attrs={'class' : 'form-control'}),
        }

    class Meta:
        model = AlumniPR
        fields = '__all__'
        widget = {
            'image' : forms.FileInput(attrs={'class' : 'form-control'}),
            'deskripsi' : forms.Textarea(attrs={'class' : 'form-control'}),
            'nama' : forms.TextInput(attrs={'class' : 'form-control'}),
            'sekolah' : forms.TextInput(attrs={'class' : 'form-control'}),
        }