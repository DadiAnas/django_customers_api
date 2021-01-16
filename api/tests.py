from django.test import TestCase
from rest_framework.parsers import JSONParser
from rest_framework.test import APIRequestFactory, force_authenticate
from api.models import Customer
from api.views import CustomerAPIView


class CustomerTestCase(TestCase):
    def setUp(self):
        Customer.objects.create(id=1001, first_name="anas", last_name="dadi", email="dadi.anas@hotmail.fr",
                                city="Azrou, Morocco", company="EnsetM", gender="Male", title="Big data Engineer",
                                longitude=0, latitude=1)

    def test_created(self):
        costomer = Customer.objects.get(id=1001)
        self.assertEqual(costomer.first_name, 'anas')


class CustomerAPIViewTestCase(TestCase):
    def setUp(self):
        Customer.objects.create(id=1001, first_name="anas", last_name="dadi", email="dadi.anas@hotmail.fr",
                                city="Azrou, Morocco", company="EnsetM", gender="Male", title="Big data Engineer",
                                longitude=0, latitude=1)

    def test_get_by_id(self):
        factory = APIRequestFactory()
        request = factory.get('/customers/1001')
        view = CustomerAPIView.as_view()
        customer = Customer.objects.get(id=1001)
        force_authenticate(request, user=customer)
        view(request)

    def test_get_many(self):
        factory = APIRequestFactory()
        request = factory.get('/customers')
        customers = Customer.objects.all()
        view = CustomerAPIView.as_view()
        force_authenticate(request,user=customers)
        view(request)
