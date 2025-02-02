from django.urls import path
from .views import *
from .api import *

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]

urlpatterns += [
    path('createview_recommendation/', Recommendation_CreateView.as_view(), name='Recommendation_CreateView'),
    path('listview_recommendation/', Recommendation_ListView.as_view(), name='Recommendation_ListView'),
    path('updateview_recommendation/<int:pk>/', Recommendation_UpdateView.as_view(), name='Recommendation_UpdateView'),
    path('detailview_recommendation/<int:pk>/', Recommendation_DetailView.as_view(), name='Recommendation_DetailView'),
    path('deleteview_recommendation/', Recommendation_DeleteView.as_view(), name='Recommendation_DeleteView'),
    path('api/listapiview_recommendation/', RecommendationListAPIView.as_view(), name='Recommendation_ListAPIView'),
    path('api/createapiview_recommendation/', RecommendationCreateAPIView.as_view(), name='Recommendation_CreateAPIView'),
    path('api/retrieveapiview_recommendation/<int:pk>/', RecommendationRetrieveAPIView.as_view(), name='Recommendation_RetrieveAPIView'),
    path('api/updateapiview_recommendation/<int:pk>/', RecommendationUpdateAPIView.as_view(), name='Recommendation_UpdateAPIView'),
    path('api/destroyapiview_recommendation/<int:pk>/', RecommendationDestroyAPIView.as_view(), name='Recommendation_DestroyAPIView'),
]

urlpatterns += [
    path('createview_algorithm/', Algorithm_CreateView.as_view(), name='Algorithm_CreateView'),
    path('listview_algorithm/', Algorithm_ListView.as_view(), name='Algorithm_ListView'),
    path('updateview_algorithm/<int:pk>/', Algorithm_UpdateView.as_view(), name='Algorithm_UpdateView'),
    path('detailview_algorithm/<int:pk>/', Algorithm_DetailView.as_view(), name='Algorithm_DetailView'),
    path('deleteview_algorithm/', Algorithm_DeleteView.as_view(), name='Algorithm_DeleteView'),
    path('api/listapiview_algorithm/', AlgorithmListAPIView.as_view(), name='Algorithm_ListAPIView'),
    path('api/createapiview_algorithm/', AlgorithmCreateAPIView.as_view(), name='Algorithm_CreateAPIView'),
    path('api/retrieveapiview_algorithm/<int:pk>/', AlgorithmRetrieveAPIView.as_view(), name='Algorithm_RetrieveAPIView'),
    path('api/updateapiview_algorithm/<int:pk>/', AlgorithmUpdateAPIView.as_view(), name='Algorithm_UpdateAPIView'),
    path('api/destroyapiview_algorithm/<int:pk>/', AlgorithmDestroyAPIView.as_view(), name='Algorithm_DestroyAPIView'),
]
