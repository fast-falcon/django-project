"""ajhang URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static
from ajhang import settings
from app import views
from app.views import logout, login_, search, signup_user, verify_user, logout_, signup_company, verify_company, \
    profile, edit_profile, addagahi, AgahiListView

urlpatterns = [
    path('createagahi/',addagahi),
    path('admin/', admin.site.urls),
    path('search',search),
    path('',AgahiListView.as_view(), name='tesyt'),
    path('signupuser/',signup_user, name='person_add'),
    path('signupcompany/',signup_company,name='company_add'),
  #  path('<int:pk>/', views.PersonUpdateView.as_view(), name='person_change'),
    path('verify_user/',verify_user),
    path('verify_company/',verify_company),
    path('profile/',profile),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
    path('logout/',logout_),
    #path('verify/',)
    path('login/',login_,name='login'),
    path('editprofile/',edit_profile)
]+static(settings.STATIC_URL, document_root=settings.SITE_ROOT)

