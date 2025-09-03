"""RiceLeaf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from RiceLeafApp.views import *
urlpatterns = [
    path('admin/', admin.site.urls),

      # Authentication
    path('', index,name='index'),
    path('login/<str:user_type>/', login_view, name='login'),
    path('register/<str:user_type>/', register_view, name='register'),
    path('create_account/', createAccount, name='create_account'),
    path('login_account/', loginAccount, name='login_account'),
    path('home/', home_view, name='home'),
    path('gallery/', gallery_view, name='gallery_view'),
    path('upload/', upload, name='upload'),
    path('detect_disease/', detect_disease, name='detect_disease'),
    path('logout/', logout, name='logout'),
    path('chatbot/', chatbot, name='chatbot')
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
