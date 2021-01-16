from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.generics import GenericAPIView

from api.models import Customer
from api.serializers import CustomerSerializer


class CustomerAPIView(GenericAPIView, ListModelMixin, RetrieveModelMixin):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    lookup_field = "id"

    def get(self, request, id=None):
        if id:
            return self.retrieve(request=request)
        else:
            return self.list(request=request)
