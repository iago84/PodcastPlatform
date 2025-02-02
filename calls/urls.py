from django.urls import path
from .views import *
from .api import *

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]

urlpatterns += [
    path('createview_call/', Call_CreateView.as_view(), name='Call_CreateView'),
    path('listview_call/', Call_ListView.as_view(), name='Call_ListView'),
    path('updateview_call/<int:pk>/', Call_UpdateView.as_view(), name='Call_UpdateView'),
    path('detailview_call/<int:pk>/', Call_DetailView.as_view(), name='Call_DetailView'),
    path('deleteview_call/', Call_DeleteView.as_view(), name='Call_DeleteView'),
    path('api/listapiview_call/', CallListAPIView.as_view(), name='Call_ListAPIView'),
    path('api/createapiview_call/', CallCreateAPIView.as_view(), name='Call_CreateAPIView'),
    path('api/retrieveapiview_call/<int:pk>/', CallRetrieveAPIView.as_view(), name='Call_RetrieveAPIView'),
    path('api/updateapiview_call/<int:pk>/', CallUpdateAPIView.as_view(), name='Call_UpdateAPIView'),
    path('api/destroyapiview_call/<int:pk>/', CallDestroyAPIView.as_view(), name='Call_DestroyAPIView'),
]

urlpatterns += [
    path('createview_videocall/', VideoCall_CreateView.as_view(), name='VideoCall_CreateView'),
    path('listview_videocall/', VideoCall_ListView.as_view(), name='VideoCall_ListView'),
    path('updateview_videocall/<int:pk>/', VideoCall_UpdateView.as_view(), name='VideoCall_UpdateView'),
    path('detailview_videocall/<int:pk>/', VideoCall_DetailView.as_view(), name='VideoCall_DetailView'),
    path('deleteview_videocall/', VideoCall_DeleteView.as_view(), name='VideoCall_DeleteView'),
    path('api/listapiview_videocall/', VideoCallListAPIView.as_view(), name='VideoCall_ListAPIView'),
    path('api/createapiview_videocall/', VideoCallCreateAPIView.as_view(), name='VideoCall_CreateAPIView'),
    path('api/retrieveapiview_videocall/<int:pk>/', VideoCallRetrieveAPIView.as_view(), name='VideoCall_RetrieveAPIView'),
    path('api/updateapiview_videocall/<int:pk>/', VideoCallUpdateAPIView.as_view(), name='VideoCall_UpdateAPIView'),
    path('api/destroyapiview_videocall/<int:pk>/', VideoCallDestroyAPIView.as_view(), name='VideoCall_DestroyAPIView'),
]

urlpatterns += [
    path('createview_callhistory/', CallHistory_CreateView.as_view(), name='CallHistory_CreateView'),
    path('listview_callhistory/', CallHistory_ListView.as_view(), name='CallHistory_ListView'),
    path('updateview_callhistory/<int:pk>/', CallHistory_UpdateView.as_view(), name='CallHistory_UpdateView'),
    path('detailview_callhistory/<int:pk>/', CallHistory_DetailView.as_view(), name='CallHistory_DetailView'),
    path('deleteview_callhistory/', CallHistory_DeleteView.as_view(), name='CallHistory_DeleteView'),
    path('api/listapiview_callhistory/', CallHistoryListAPIView.as_view(), name='CallHistory_ListAPIView'),
    path('api/createapiview_callhistory/', CallHistoryCreateAPIView.as_view(), name='CallHistory_CreateAPIView'),
    path('api/retrieveapiview_callhistory/<int:pk>/', CallHistoryRetrieveAPIView.as_view(), name='CallHistory_RetrieveAPIView'),
    path('api/updateapiview_callhistory/<int:pk>/', CallHistoryUpdateAPIView.as_view(), name='CallHistory_UpdateAPIView'),
    path('api/destroyapiview_callhistory/<int:pk>/', CallHistoryDestroyAPIView.as_view(), name='CallHistory_DestroyAPIView'),
]
