from django.urls import path
from .views import *
from .api import *

urlpatterns = [
]

urlpatterns += [
    path('createview_userprofile/', UserProfile_CreateView.as_view(), name='UserProfile_CreateView'),
    path('listview_userprofile/', UserProfile_ListView.as_view(), name='UserProfile_ListView'),
    path('updateview_userprofile/<int:pk>/', UserProfile_UpdateView.as_view(), name='UserProfile_UpdateView'),
    path('detailview_userprofile/<int:pk>/', UserProfile_DetailView.as_view(), name='UserProfile_DetailView'),
    path('deleteview_userprofile/', UserProfile_DeleteView.as_view(), name='UserProfile_DeleteView'),
    path('api/listapiview_userprofile/', UserProfileListAPIView.as_view(), name='UserProfile_ListAPIView'),
    path('api/createapiview_userprofile/', UserProfileCreateAPIView.as_view(), name='UserProfile_CreateAPIView'),
    path('api/retrieveapiview_userprofile/<int:pk>/', UserProfileRetrieveAPIView.as_view(), name='UserProfile_RetrieveAPIView'),
    path('api/updateapiview_userprofile/<int:pk>/', UserProfileUpdateAPIView.as_view(), name='UserProfile_UpdateAPIView'),
    path('api/destroyapiview_userprofile/<int:pk>/', UserProfileDestroyAPIView.as_view(), name='UserProfile_DestroyAPIView'),
]

urlpatterns += [
    path('createview_role/', Role_CreateView.as_view(), name='Role_CreateView'),
    path('listview_role/', Role_ListView.as_view(), name='Role_ListView'),
    path('updateview_role/<int:pk>/', Role_UpdateView.as_view(), name='Role_UpdateView'),
    path('detailview_role/<int:pk>/', Role_DetailView.as_view(), name='Role_DetailView'),
    path('deleteview_role/', Role_DeleteView.as_view(), name='Role_DeleteView'),
    path('api/listapiview_role/', RoleListAPIView.as_view(), name='Role_ListAPIView'),
    path('api/createapiview_role/', RoleCreateAPIView.as_view(), name='Role_CreateAPIView'),
    path('api/retrieveapiview_role/<int:pk>/', RoleRetrieveAPIView.as_view(), name='Role_RetrieveAPIView'),
    path('api/updateapiview_role/<int:pk>/', RoleUpdateAPIView.as_view(), name='Role_UpdateAPIView'),
    path('api/destroyapiview_role/<int:pk>/', RoleDestroyAPIView.as_view(), name='Role_DestroyAPIView'),
]

urlpatterns += [
    path('createview_permission/', Permission_CreateView.as_view(), name='Permission_CreateView'),
    path('listview_permission/', Permission_ListView.as_view(), name='Permission_ListView'),
    path('updateview_permission/<int:pk>/', Permission_UpdateView.as_view(), name='Permission_UpdateView'),
    path('detailview_permission/<int:pk>/', Permission_DetailView.as_view(), name='Permission_DetailView'),
    path('deleteview_permission/', Permission_DeleteView.as_view(), name='Permission_DeleteView'),
    path('api/listapiview_permission/', PermissionListAPIView.as_view(), name='Permission_ListAPIView'),
    path('api/createapiview_permission/', PermissionCreateAPIView.as_view(), name='Permission_CreateAPIView'),
    path('api/retrieveapiview_permission/<int:pk>/', PermissionRetrieveAPIView.as_view(), name='Permission_RetrieveAPIView'),
    path('api/updateapiview_permission/<int:pk>/', PermissionUpdateAPIView.as_view(), name='Permission_UpdateAPIView'),
    path('api/destroyapiview_permission/<int:pk>/', PermissionDestroyAPIView.as_view(), name='Permission_DestroyAPIView'),
]

urlpatterns += [
    path('createview_message/', Message_CreateView.as_view(), name='Message_CreateView'),
    path('listview_message/', Message_ListView.as_view(), name='Message_ListView'),
    path('updateview_message/<int:pk>/', Message_UpdateView.as_view(), name='Message_UpdateView'),
    path('detailview_message/<int:pk>/', Message_DetailView.as_view(), name='Message_DetailView'),
    path('deleteview_message/', Message_DeleteView.as_view(), name='Message_DeleteView'),
    path('api/listapiview_message/', MessageListAPIView.as_view(), name='Message_ListAPIView'),
    path('api/createapiview_message/', MessageCreateAPIView.as_view(), name='Message_CreateAPIView'),
    path('api/retrieveapiview_message/<int:pk>/', MessageRetrieveAPIView.as_view(), name='Message_RetrieveAPIView'),
    path('api/updateapiview_message/<int:pk>/', MessageUpdateAPIView.as_view(), name='Message_UpdateAPIView'),
    path('api/destroyapiview_message/<int:pk>/', MessageDestroyAPIView.as_view(), name='Message_DestroyAPIView'),
]
