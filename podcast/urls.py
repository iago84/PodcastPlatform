from django.urls import path
from .views import *
from .api import *

urlpatterns = [
]

urlpatterns += [
    path('createview_episode/', Episode_CreateView.as_view(), name='Episode_CreateView'),
    path('listview_episode/', Episode_ListView.as_view(), name='Episode_ListView'),
    path('updateview_episode/<int:pk>/', Episode_UpdateView.as_view(), name='Episode_UpdateView'),
    path('detailview_episode/<int:pk>/', Episode_DetailView.as_view(), name='Episode_DetailView'),
    path('deleteview_episode/', Episode_DeleteView.as_view(), name='Episode_DeleteView'),
    path('api/listapiview_episode/', EpisodeListAPIView.as_view(), name='Episode_ListAPIView'),
    path('api/createapiview_episode/', EpisodeCreateAPIView.as_view(), name='Episode_CreateAPIView'),
    path('api/retrieveapiview_episode/<int:pk>/', EpisodeRetrieveAPIView.as_view(), name='Episode_RetrieveAPIView'),
    path('api/updateapiview_episode/<int:pk>/', EpisodeUpdateAPIView.as_view(), name='Episode_UpdateAPIView'),
    path('api/destroyapiview_episode/<int:pk>/', EpisodeDestroyAPIView.as_view(), name='Episode_DestroyAPIView'),
]

urlpatterns += [
    path('createview_category/', Category_CreateView.as_view(), name='Category_CreateView'),
    path('listview_category/', Category_ListView.as_view(), name='Category_ListView'),
    path('updateview_category/<int:pk>/', Category_UpdateView.as_view(), name='Category_UpdateView'),
    path('detailview_category/<int:pk>/', Category_DetailView.as_view(), name='Category_DetailView'),
    path('deleteview_category/', Category_DeleteView.as_view(), name='Category_DeleteView'),
    path('api/listapiview_category/', CategoryListAPIView.as_view(), name='Category_ListAPIView'),
    path('api/createapiview_category/', CategoryCreateAPIView.as_view(), name='Category_CreateAPIView'),
    path('api/retrieveapiview_category/<int:pk>/', CategoryRetrieveAPIView.as_view(), name='Category_RetrieveAPIView'),
    path('api/updateapiview_category/<int:pk>/', CategoryUpdateAPIView.as_view(), name='Category_UpdateAPIView'),
    path('api/destroyapiview_category/<int:pk>/', CategoryDestroyAPIView.as_view(), name='Category_DestroyAPIView'),
]

urlpatterns += [
    path('createview_statistic/', Statistic_CreateView.as_view(), name='Statistic_CreateView'),
    path('listview_statistic/', Statistic_ListView.as_view(), name='Statistic_ListView'),
    path('updateview_statistic/<int:pk>/', Statistic_UpdateView.as_view(), name='Statistic_UpdateView'),
    path('detailview_statistic/<int:pk>/', Statistic_DetailView.as_view(), name='Statistic_DetailView'),
    path('deleteview_statistic/', Statistic_DeleteView.as_view(), name='Statistic_DeleteView'),
    path('api/listapiview_statistic/', StatisticListAPIView.as_view(), name='Statistic_ListAPIView'),
    path('api/createapiview_statistic/', StatisticCreateAPIView.as_view(), name='Statistic_CreateAPIView'),
    path('api/retrieveapiview_statistic/<int:pk>/', StatisticRetrieveAPIView.as_view(), name='Statistic_RetrieveAPIView'),
    path('api/updateapiview_statistic/<int:pk>/', StatisticUpdateAPIView.as_view(), name='Statistic_UpdateAPIView'),
    path('api/destroyapiview_statistic/<int:pk>/', StatisticDestroyAPIView.as_view(), name='Statistic_DestroyAPIView'),
]

urlpatterns += [
    path('createview_comment/', Comment_CreateView.as_view(), name='Comment_CreateView'),
    path('listview_comment/', Comment_ListView.as_view(), name='Comment_ListView'),
    path('updateview_comment/<int:pk>/', Comment_UpdateView.as_view(), name='Comment_UpdateView'),
    path('detailview_comment/<int:pk>/', Comment_DetailView.as_view(), name='Comment_DetailView'),
    path('deleteview_comment/', Comment_DeleteView.as_view(), name='Comment_DeleteView'),
    path('api/listapiview_comment/', CommentListAPIView.as_view(), name='Comment_ListAPIView'),
    path('api/createapiview_comment/', CommentCreateAPIView.as_view(), name='Comment_CreateAPIView'),
    path('api/retrieveapiview_comment/<int:pk>/', CommentRetrieveAPIView.as_view(), name='Comment_RetrieveAPIView'),
    path('api/updateapiview_comment/<int:pk>/', CommentUpdateAPIView.as_view(), name='Comment_UpdateAPIView'),
    path('api/destroyapiview_comment/<int:pk>/', CommentDestroyAPIView.as_view(), name='Comment_DestroyAPIView'),
]

urlpatterns += [
    path('createview_download/', Download_CreateView.as_view(), name='Download_CreateView'),
    path('listview_download/', Download_ListView.as_view(), name='Download_ListView'),
    path('updateview_download/<int:pk>/', Download_UpdateView.as_view(), name='Download_UpdateView'),
    path('detailview_download/<int:pk>/', Download_DetailView.as_view(), name='Download_DetailView'),
    path('deleteview_download/', Download_DeleteView.as_view(), name='Download_DeleteView'),
    path('api/listapiview_download/', DownloadListAPIView.as_view(), name='Download_ListAPIView'),
    path('api/createapiview_download/', DownloadCreateAPIView.as_view(), name='Download_CreateAPIView'),
    path('api/retrieveapiview_download/<int:pk>/', DownloadRetrieveAPIView.as_view(), name='Download_RetrieveAPIView'),
    path('api/updateapiview_download/<int:pk>/', DownloadUpdateAPIView.as_view(), name='Download_UpdateAPIView'),
    path('api/destroyapiview_download/<int:pk>/', DownloadDestroyAPIView.as_view(), name='Download_DestroyAPIView'),
]
