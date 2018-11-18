from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import status
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from .models import Bank
from .serializers import BankSerializer


class ListBankView(generics.ListAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    throttle_classes = (
        AnonRateThrottle, 
    )

class FromIFSCView(generics.RetrieveAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    throttle_classes = (
        AnonRateThrottle, 
    )

    def get(self, request, *args, **kwargs):
        try:
            bank = self.queryset.get(ifsc=kwargs["pk"].upper())
            return Response(BankSerializer(bank).data)

        except Bank.DoesNotExist:
            return Response(
                data={
                    "message": "Bank does not exist"
                },
                status=status.HTTP_404_NOT_FOUND
            )

class FromBankInfoView(generics.RetrieveAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    throttle_classes = (
        AnonRateThrottle, 
    )

    def get(self, request, *args, **kwargs):
        try:
            bank_name = request.GET['bank_name'].upper()
            city = request.GET['city'].upper()
            print(bank_name, city)
            bank = self.queryset.filter(bank_name=bank_name, city=city).all()
            if bank:
                return Response(BankSerializer(bank, many=True).data)
            else:
                return Response(
                    data={
                        "message": "Does Not Exist"
                    },
                    status=status.HTTP_404_NOT_FOUND
                )
        except:
            return Response(
                data={
                    'message': "Error! Make sure the name of params is correct."
                },
                status=status.HTTP_404_NOT_FOUND
            )