from django.urls import path
from . import views

app_name = 'ads'

urlpatterns = [
    # Main ads page - list all ads
    path('', views.AdListView.as_view(), name='all'),
    
    # Ad detail view
    path('ad/<int:pk>', views.AdDetailView.as_view(), name='ad_detail'),
    
    # Create new ad
    path('ad/create', views.AdCreateView.as_view(), name='ad_create'),
    
    # Update existing ad
    path('ad/<int:pk>/update', views.AdUpdateView.as_view(), name='ad_update'),
    
    # Delete ad
    path('ad/<int:pk>/delete', views.AdDeleteView.as_view(), name='ad_delete'),
]