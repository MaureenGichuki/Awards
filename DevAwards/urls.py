from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path
urlpatterns=[
    path('', views.home, name='home'),
    path('project/', views.project, name='project'),
    path('search/', views.search_results, name='search_results'),
    path('user/<user_id>/', views.profile, name='profile'),
    path('user/update/profile', views.update_profile, name='updateprofile'),
    path('projectdetails/<project_id>',views.project_details,name='projectdetails'),
    path('rates/<project_id>',views.submit_rates,name='submitrates'),
    path('api/project/', views.ProjectList.as_view(),name=''),
    path('api/profile/', views.ProfileList.as_view(),name='')
  
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)