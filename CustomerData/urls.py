from django.urls import path
from CustomerData import *
from django.urls import path
from . import views


urlpatterns = [
    path('leads_Create/',views.Leads_Create,name='leads_Create'),
    
    path('deals_Create/',views.Deals_Create,name='deals_Create'),
    
    path('task_Create/',views.Task_Create,name='task_Create'),
    
    path('lead_view/', views.Lead_view, name='lead_view'),    
    
    path('deal_view/', views.deals_view, name='deal_view'),    
    
    path('task_view/', views.task_view, name='task_view'),    
]

    
    
