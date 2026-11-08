from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('org/projects-members-permissions/', views.org_projects_members_permissions, name='org_pmp'),
    path('org/projects-permissions-members/', views.org_projects_permissions_members, name='org_ppm'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    path('members/<int:pk>/', views.member_detail, name='member_detail'),
    path('permissions/<int:pk>/', views.permission_detail, name='permission_detail'),
]
