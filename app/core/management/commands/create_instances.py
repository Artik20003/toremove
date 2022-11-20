from django.core.management.base import BaseCommand
from core.models import Item, Price, Currency, Order


class Command(BaseCommand):

    ITEMS = [
        {
            "name": "Item 1",
            "description": "Description of Item 1",
            "price": {
                "unit_price": 500,
                "currency": {
                    "name": "usd",
                    "symbol": "$"
                }
            }
        },
        {
            "name": "Item 2",
            "description": "Description of Item 2",
            "price": {
                "unit_price": 250,
                "currency": {
                    "name": "usd",
                    "symbol": "$"
                }
            }
        }
    ]

    def create_test_items(self):
        output = {}

        for item in self.ITEMS:
            currency_obj, currency_created = Currency.objects.get_or_create(
                name=item["price"]["currency"]["name"],
                symbol=item["price"]["currency"]["symbol"]
            )
            price_obj, price_created= Price.objects.get_or_create(
                unit_price=item["price"]["unit_price"],
                currency=currency_obj
            )
            item_obj, item_created = Item.objects.get_or_create(
                name=item["name"],
                description=item["description"],
                price=price_obj
            )

            if item_created:
                output[item_obj.id] = item_obj
        
        return output


    def create_test_order(self, order_items:dict):
        if not order_items:
            return 
        
        order_obj = Order.objects.create()
        order_obj.items.add(*list(order_items.values()))
        order_obj.save()
        

    def handle(self, *args, **options):
        print('[LOG] -> Initializing test database...')
        self.create_test_order(self.create_test_items())
        print('[LOG] -> Finished initializing test database')
