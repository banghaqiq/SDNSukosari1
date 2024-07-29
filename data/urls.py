from django.urls import path
from . import views

urlpatterns = [
 path('', views.beranda, name='home'),

#  ABOUT
 path('profile/', views.profil, name='profile'),
 path('vm/', views.visimisi, name='visimisi'),
 path('developer/', views.developer, name='developer'),
 path('struktur/', views.struktur, name='struktur'),
 path('dataguru/', views.dataguru, name='dataguru'),

# Prestasi
 path('kec/', views.kec, name='kecamatan'),
 path('kab/', views.kab, name='kabupaten'),
 path('prov/', views.prov, name='provinsi'),
 path('nas/', views.nas, name='nasional'),

#  Performa
 path('classmeating/', views.classmeating, name='classmeating'),
 path('drumband/', views.drumband, name='drumband'),
 path('studytour/', views.studytour, name='studytour'),
 path('keagamaan/', views.keagamaan, name='keagamaan'),
 path('penampilan/', views.penampilan, name='penampilan'),


#  informasi
 path('berita/', views.berita, name='berita'),
 path('pengumuman/', views.pengumuman, name='pengumuman'),
 path('extra/', views.extrakulikuler, name='extra'),


 path('testimonial/', views.alumni, name='testimonial'),
 path('contact/', views.contact, name='contact'),

]