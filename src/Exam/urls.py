"""Exam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path,re_path
from django.conf import settings
from django.conf.urls.static import static
from auth_user.views import index,accueil
from django.contrib.auth import views as auth_views
from wkhtmltopdf.views import PDFTemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth_user/',include('auth_user.urls')),
    path('generate/',include('generate.urls')),
    path('api/', include('apis.urls')),
    path('pdf/',include('pdf.urls')),
    path('accounts/login/',
         auth_views.LoginView.as_view(template_name='auth_user/login.html'), name='login'),
    path('accounts/logout/',
         auth_views.LogoutView.as_view(template_name='auth_user/login.html'), name='logout'),
    path('accounts/profil',index,name='index'),
    path('',accueil,name='accueil'),
    re_path(r'^pdf/$', PDFTemplateView.as_view(template_name='pdf/index.html',
                                           filename='my_pdf.pdf'), name='pdf'),   
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)