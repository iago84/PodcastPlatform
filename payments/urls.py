from django.urls import path
from .views import *
from .api import *

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]

urlpatterns += [
    path('createview_payment/', Payment_CreateView.as_view(), name='Payment_CreateView'),
    path('listview_payment/', Payment_ListView.as_view(), name='Payment_ListView'),
    path('updateview_payment/<int:pk>/', Payment_UpdateView.as_view(), name='Payment_UpdateView'),
    path('detailview_payment/<int:pk>/', Payment_DetailView.as_view(), name='Payment_DetailView'),
    path('deleteview_payment/', Payment_DeleteView.as_view(), name='Payment_DeleteView'),
    path('api/listapiview_payment/', PaymentListAPIView.as_view(), name='Payment_ListAPIView'),
    path('api/createapiview_payment/', PaymentCreateAPIView.as_view(), name='Payment_CreateAPIView'),
    path('api/retrieveapiview_payment/<int:pk>/', PaymentRetrieveAPIView.as_view(), name='Payment_RetrieveAPIView'),
    path('api/updateapiview_payment/<int:pk>/', PaymentUpdateAPIView.as_view(), name='Payment_UpdateAPIView'),
    path('api/destroyapiview_payment/<int:pk>/', PaymentDestroyAPIView.as_view(), name='Payment_DestroyAPIView'),
]

urlpatterns += [
    path('createview_invoice/', Invoice_CreateView.as_view(), name='Invoice_CreateView'),
    path('listview_invoice/', Invoice_ListView.as_view(), name='Invoice_ListView'),
    path('updateview_invoice/<int:pk>/', Invoice_UpdateView.as_view(), name='Invoice_UpdateView'),
    path('detailview_invoice/<int:pk>/', Invoice_DetailView.as_view(), name='Invoice_DetailView'),
    path('deleteview_invoice/', Invoice_DeleteView.as_view(), name='Invoice_DeleteView'),
    path('api/listapiview_invoice/', InvoiceListAPIView.as_view(), name='Invoice_ListAPIView'),
    path('api/createapiview_invoice/', InvoiceCreateAPIView.as_view(), name='Invoice_CreateAPIView'),
    path('api/retrieveapiview_invoice/<int:pk>/', InvoiceRetrieveAPIView.as_view(), name='Invoice_RetrieveAPIView'),
    path('api/updateapiview_invoice/<int:pk>/', InvoiceUpdateAPIView.as_view(), name='Invoice_UpdateAPIView'),
    path('api/destroyapiview_invoice/<int:pk>/', InvoiceDestroyAPIView.as_view(), name='Invoice_DestroyAPIView'),
]

urlpatterns += [
    path('createview_payout/', Payout_CreateView.as_view(), name='Payout_CreateView'),
    path('listview_payout/', Payout_ListView.as_view(), name='Payout_ListView'),
    path('updateview_payout/<int:pk>/', Payout_UpdateView.as_view(), name='Payout_UpdateView'),
    path('detailview_payout/<int:pk>/', Payout_DetailView.as_view(), name='Payout_DetailView'),
    path('deleteview_payout/', Payout_DeleteView.as_view(), name='Payout_DeleteView'),
    path('api/listapiview_payout/', PayoutListAPIView.as_view(), name='Payout_ListAPIView'),
    path('api/createapiview_payout/', PayoutCreateAPIView.as_view(), name='Payout_CreateAPIView'),
    path('api/retrieveapiview_payout/<int:pk>/', PayoutRetrieveAPIView.as_view(), name='Payout_RetrieveAPIView'),
    path('api/updateapiview_payout/<int:pk>/', PayoutUpdateAPIView.as_view(), name='Payout_UpdateAPIView'),
    path('api/destroyapiview_payout/<int:pk>/', PayoutDestroyAPIView.as_view(), name='Payout_DestroyAPIView'),
]
