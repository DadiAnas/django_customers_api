from geopy.geocoders import Photon
from django.core.management.base import BaseCommand, CommandError
from api.models import Customer



class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            geo_locator = Photon()
            customers = Customer.objects.all()
            a=0
            for customer in customers:
                location = geo_locator.geocode(customer.city, timeout=15)
                if location:
                    customer.latitude = location.latitude
                    customer.longitude = location.longitude
                    print(customer.id)
                    customer.save()
                else:
                    a+=1
                    print(a)
            self.stdout.write(self.style.SUCCESS('Successfully filled addresses'))
        except CommandError:
            raise
