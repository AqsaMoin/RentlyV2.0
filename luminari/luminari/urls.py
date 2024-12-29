"""
URL configuration for luminari project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.homepage_view,name='home'),
    path('places/<slug:slug>/',views.place_details,name='place_details'),
    path('',views.register_view,name="register"),
    path("login/",views.login_view,name="login"),
    path("logout/",LogoutView.as_view(),name="logout"),
    path('add-place/',views.add_place_view,name='add_place'),
    path('about-us/',views.about_us,name='about_us'),
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('search/',views.search_place,name='search_places'),
    path('profile/',views.profile_views,name='profile'),
    path('absh/',views.about_shi,name='shiva'),
    path('absi/',views.about_sin,name='sindhuja'),
    path('sam/',views.about_sam,name='sam'),
    path('intern/',views.intern_view,name='intern')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)