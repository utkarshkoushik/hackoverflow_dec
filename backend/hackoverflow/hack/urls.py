from rest_framework import routers
from django.urls import path, include

from .views import userDataApi
from .import views

router = routers.DefaultRouter()
router.register('userData',userDataApi,'userDataApi')
router.register('hackathon',views.HackathonAPi,'hackapi')
router.register('TeamAPi',views.TeamAPi,'TeamAPi')
router.register('GroupAPi',views.GroupAPi,'GroupAPi')

urlpatterns =[
    path('',include(router.urls)),
    path('login',views.login,name='login'),
    path('logout',views.logout,name="logout"),
    path('create_user',views.create_user,name="create_user"),
    path('create_team_memeber',views.create_team_memeber,name="create_team_memeber"),
    path('create_group_memeber',views.create_group_memeber,name="create_group_memeber"),
    path('create_message',views.create_message,name="create_message"),
    path('get_group_message',views.get_group_message,name="get_group_message"),
    path('get_user_grp',views.get_user_grp,name="get_user_grp"),
    path('get_all_grp_members',views.get_all_grp_members,name="get_all_grp_members"),
    path('get_user_data',views.get_user_data,name="get_user_data"),
]