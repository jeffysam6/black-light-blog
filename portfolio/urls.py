from django.urls import path,include
from . import views

urlpatterns = [

    path('',views.about,name='portfolio-about'),

    path('resume/',views.resume,name='portfolio-resume'),

    path('contact/',views.contact,name='portfolio-contact'),

    path('projects/',views.projects,name='portfolio-projects')



    # path('',views.home,name='portfolio-home'),


 
]