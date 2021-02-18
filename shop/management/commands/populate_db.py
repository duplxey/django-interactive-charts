# shop/management/commands/populate_db.py

import random
from datetime import datetime, timedelta

import pytz
from django.core.management.base import BaseCommand

from shop.models import Item, Purchase


class Command(BaseCommand):
    help = 'Populates the database with random generated data.'

    def add_arguments(self, parser):
        parser.add_argument('--amount', type=int, help='The number of purchases that should be created.')

    def handle(self, *args, **options):
        names = ['James', 'John', 'Robert', 'Michael', 'William', 'David', 'Richard', 'Joseph', 'Thomas', 'Charles']
        surname = ['Smith', 'Jones', 'Taylor', 'Brown', 'Williams', 'Wilson', 'Johnson', 'Davies', 'Patel', 'Wright']
        items = [
            Item.objects.get_or_create(name='Socks', price=6.5), Item.objects.get_or_create(name='Pants', price=12),
            Item.objects.get_or_create(name='T-Shirt', price=8), Item.objects.get_or_create(name='Boots', price=9),
            Item.objects.get_or_create(name='Sweater', price=3), Item.objects.get_or_create(name='Underwear', price=9),
            Item.objects.get_or_create(name='Leggings', price=7), Item.objects.get_or_create(name='Cap', price=5),
        ]
        amount = options['amount'] if options['amount'] else 2500
        for i in range(0, amount):
            dt = pytz.utc.localize(datetime.now() - timedelta(days=random.randint(0, 1825)))
            purchase = Purchase.objects.create(
                customer_full_name=random.choice(names) + ' ' + random.choice(surname),
                item=random.choice(items)[0],
                payment_method=random.choice(Purchase.PAYMENT_METHODS)[0],
                successful=True if random.randint(1, 2) == 1 else False,
            )
            purchase.time = dt
            purchase.save()

        self.stdout.write(self.style.SUCCESS('Successfully populated the database.'))
