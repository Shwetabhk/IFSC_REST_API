from django.urls import path
from .views import ListBankView, FromIFSCView, FromBankInfoView


urlpatterns = [
    path('banks/', ListBankView.as_view(), name="banks-all"),
    path('banks/<str:pk>/', FromIFSCView.as_view(), name="from-ifsc"),
    path('branches/', FromBankInfoView.as_view(), name="from-info"),
]
