import csv
from django.core.management.base import BaseCommand, CommandError
from api.models import Customer


# pd.read_csv(filename).to_sql(Customer, con)
class Command(BaseCommand):
    """
        Load a customers csv file into the database
    """

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        try:
            with open(path, 'rt') as csv_file:
                reader = csv.DictReader(csv_file)
                for customer in reader:
                    Customer.objects.create(**customer)
                    print(customer)
            self.stdout.write(self.style.SUCCESS('Successfully added customers'))
        except FileNotFoundError:
            raise CommandError("file does not exist")
