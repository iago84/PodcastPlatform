from django.urls import path
from .views import *
from .api import *

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]

urlpatterns += [
    path('createview_plan/', Plan_CreateView.as_view(), name='Plan_CreateView'),
    path('listview_plan/', Plan_ListView.as_view(), name='Plan_ListView'),
    path('updateview_plan/<int:pk>/', Plan_UpdateView.as_view(), name='Plan_UpdateView'),
    path('detailview_plan/<int:pk>/', Plan_DetailView.as_view(), name='Plan_DetailView'),
    path('deleteview_plan/', Plan_DeleteView.as_view(), name='Plan_DeleteView'),
    path('api/listapiview_plan/', PlanListAPIView.as_view(), name='Plan_ListAPIView'),
    path('api/createapiview_plan/', PlanCreateAPIView.as_view(), name='Plan_CreateAPIView'),
    path('api/retrieveapiview_plan/<int:pk>/', PlanRetrieveAPIView.as_view(), name='Plan_RetrieveAPIView'),
    path('api/updateapiview_plan/<int:pk>/', PlanUpdateAPIView.as_view(), name='Plan_UpdateAPIView'),
    path('api/destroyapiview_plan/<int:pk>/', PlanDestroyAPIView.as_view(), name='Plan_DestroyAPIView'),
]

urlpatterns += [
    path('createview_subscription/', Subscription_CreateView.as_view(), name='Subscription_CreateView'),
    path('listview_subscription/', Subscription_ListView.as_view(), name='Subscription_ListView'),
    path('updateview_subscription/<int:pk>/', Subscription_UpdateView.as_view(), name='Subscription_UpdateView'),
    path('detailview_subscription/<int:pk>/', Subscription_DetailView.as_view(), name='Subscription_DetailView'),
    path('deleteview_subscription/', Subscription_DeleteView.as_view(), name='Subscription_DeleteView'),
    path('api/listapiview_subscription/', SubscriptionListAPIView.as_view(), name='Subscription_ListAPIView'),
    path('api/createapiview_subscription/', SubscriptionCreateAPIView.as_view(), name='Subscription_CreateAPIView'),
    path('api/retrieveapiview_subscription/<int:pk>/', SubscriptionRetrieveAPIView.as_view(), name='Subscription_RetrieveAPIView'),
    path('api/updateapiview_subscription/<int:pk>/', SubscriptionUpdateAPIView.as_view(), name='Subscription_UpdateAPIView'),
    path('api/destroyapiview_subscription/<int:pk>/', SubscriptionDestroyAPIView.as_view(), name='Subscription_DestroyAPIView'),
]

urlpatterns += [
    path('createview_transaction/', Transaction_CreateView.as_view(), name='Transaction_CreateView'),
    path('listview_transaction/', Transaction_ListView.as_view(), name='Transaction_ListView'),
    path('updateview_transaction/<int:pk>/', Transaction_UpdateView.as_view(), name='Transaction_UpdateView'),
    path('detailview_transaction/<int:pk>/', Transaction_DetailView.as_view(), name='Transaction_DetailView'),
    path('deleteview_transaction/', Transaction_DeleteView.as_view(), name='Transaction_DeleteView'),
    path('api/listapiview_transaction/', TransactionListAPIView.as_view(), name='Transaction_ListAPIView'),
    path('api/createapiview_transaction/', TransactionCreateAPIView.as_view(), name='Transaction_CreateAPIView'),
    path('api/retrieveapiview_transaction/<int:pk>/', TransactionRetrieveAPIView.as_view(), name='Transaction_RetrieveAPIView'),
    path('api/updateapiview_transaction/<int:pk>/', TransactionUpdateAPIView.as_view(), name='Transaction_UpdateAPIView'),
    path('api/destroyapiview_transaction/<int:pk>/', TransactionDestroyAPIView.as_view(), name='Transaction_DestroyAPIView'),
]
