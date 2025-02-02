from django.urls import path
from .views import *
from .api import *

urlpatterns = [
]

urlpatterns += [
    path('createview_report/', Report_CreateView.as_view(), name='Report_CreateView'),
    path('listview_report/', Report_ListView.as_view(), name='Report_ListView'),
    path('updateview_report/<int:pk>/', Report_UpdateView.as_view(), name='Report_UpdateView'),
    path('detailview_report/<int:pk>/', Report_DetailView.as_view(), name='Report_DetailView'),
    path('deleteview_report/', Report_DeleteView.as_view(), name='Report_DeleteView'),
    path('api/listapiview_report/', ReportListAPIView.as_view(), name='Report_ListAPIView'),
    path('api/createapiview_report/', ReportCreateAPIView.as_view(), name='Report_CreateAPIView'),
    path('api/retrieveapiview_report/<int:pk>/', ReportRetrieveAPIView.as_view(), name='Report_RetrieveAPIView'),
    path('api/updateapiview_report/<int:pk>/', ReportUpdateAPIView.as_view(), name='Report_UpdateAPIView'),
    path('api/destroyapiview_report/<int:pk>/', ReportDestroyAPIView.as_view(), name='Report_DestroyAPIView'),
]

urlpatterns += [
    path('createview_flaggedcontent/', FlaggedContent_CreateView.as_view(), name='FlaggedContent_CreateView'),
    path('listview_flaggedcontent/', FlaggedContent_ListView.as_view(), name='FlaggedContent_ListView'),
    path('updateview_flaggedcontent/<int:pk>/', FlaggedContent_UpdateView.as_view(), name='FlaggedContent_UpdateView'),
    path('detailview_flaggedcontent/<int:pk>/', FlaggedContent_DetailView.as_view(), name='FlaggedContent_DetailView'),
    path('deleteview_flaggedcontent/', FlaggedContent_DeleteView.as_view(), name='FlaggedContent_DeleteView'),
    path('api/listapiview_flaggedcontent/', FlaggedContentListAPIView.as_view(), name='FlaggedContent_ListAPIView'),
    path('api/createapiview_flaggedcontent/', FlaggedContentCreateAPIView.as_view(), name='FlaggedContent_CreateAPIView'),
    path('api/retrieveapiview_flaggedcontent/<int:pk>/', FlaggedContentRetrieveAPIView.as_view(), name='FlaggedContent_RetrieveAPIView'),
    path('api/updateapiview_flaggedcontent/<int:pk>/', FlaggedContentUpdateAPIView.as_view(), name='FlaggedContent_UpdateAPIView'),
    path('api/destroyapiview_flaggedcontent/<int:pk>/', FlaggedContentDestroyAPIView.as_view(), name='FlaggedContent_DestroyAPIView'),
]
