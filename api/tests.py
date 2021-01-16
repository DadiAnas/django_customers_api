from django.test import TestCase
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
        # Every test needs access to the request factory.
        self.factory = APIRequestFactory()
        # Create a simple customer to validate using it
        Customer.objects.create(id=1001, first_name="anas", last_name="dadi", email="dadi.anas@hotmail.fr",
                                city="Azrou, Morocco", company="EnsetM", gender="Male", title="Big data Engineer",
                                longitude=0, latitude=1)

    def test_get(self):
        """
            This function will test get by id
        """
        # Create an instance of a GET request to get one customer
        request = self.factory.get('/customers/1001')
        # Get the customer created in setUp method
        customer = Customer.objects.get(id=1001)
        # Using the force_authenticate() method To forcibly authenticate the request
        force_authenticate(request, user=customer)
        # Test view() as if it were deployed at /customers/<int:id>
        view = CustomerAPIView.as_view()
        response = view(request)
        # Test if the request works well
        self.assertEqual(response.status_code, 200)

        # Create an instance of a GET request to get all customers
        request = self.factory.get('/customers')
        # Get all created customers
        customers = Customer.objects.all()
        # Test view() as if it were deployed at /customers/
        view = CustomerAPIView.as_view()
        # Using the force_authenticate() method To forcibly authenticate the request
        force_authenticate(request, user=customers)
        response = view(request)
        # Test if the request works well
        self.assertEqual(response.status_code, 200)
