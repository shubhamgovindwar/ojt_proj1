"""
URL configuration for operations project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from string_op import views1
from num_op import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home_page', views1.home_view),
    path('reverse_string', views1.rev_string),
    path('pallindrome_string', views1.pallindrome),
    path('word_count', views1.word_count),
    path('num_home', views.num_home),
    path('reverse_num', views.num_rev),
    path('amstrong_num', views.amstrong_num),
    path('pallindrome_num', views.num_pallindrome),
    # path('reverse_num2', views.rev_numa),

]
