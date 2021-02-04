import random
from datetime import datetime, timedelta

import pytz
from django.http import JsonResponse
from django.utils import timezone

from shop.models import Purchase, Item

colorPalette = ["#55efc4", "#81ecec", "#74b9ff", "#a29bfe",
                "#ffeaa7", "#fab1a0", "#ff7675", "#fd79a8"]
colorSuccess = colorPalette[0]
colorDanger = colorSuccess[6]


def generate_color_palette(amount):
    palette = []
    i = 0
    while i < len(colorPalette) and len(palette) < amount:
        palette.append(colorPalette[i])
        print(colorPalette[i])
        i += 1
        if i == len(colorPalette) and len(palette) < amount:
            i = 0
    return palette


def get_sales_chart(request, year):
    return JsonResponse({
        'labels': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
        'backgroundColor': ['#79AEC8'],
        'borderColor': ['#79AEC8'],
        'data': [1, 2, 3, 4, 5],
    })


def spend_per_customer_chart(request, year):
    return JsonResponse({
        'labels': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
        'backgroundColor': ['#79AEC8'],
        'borderColor': ['#79AEC8'],
        'data': [1, 2, 3, 4, 5],
    })


def payment_success_chart(request, year):
    purchases = Purchase.objects.filter(time__year=year)
    successful, unsuccessful = 0, 0

    for purchase in purchases:
        if purchase.successful:
            successful += 1
        else:
            unsuccessful += 1

    return JsonResponse({
        'labels': ['Successful', 'Unsuccessful'],
        'backgroundColor': [colorSuccess, colorSuccess],
        'borderColor': [colorDanger, colorDanger],
        'data': [successful, unsuccessful],
    })


def payment_method_chart(request, year):
    purchases = Purchase.objects.filter(time__year=year)
    payment_method_dict = dict()

    for payment_method in Purchase.PAYMENT_METHODS:
        payment_method_dict[payment_method[1]] = 0

    for purchase in purchases:
        payment_type = dict(Purchase.PAYMENT_METHODS)[purchase.payment_method]
        if payment_type in payment_method_dict:
            payment_method_dict[payment_type] = payment_method_dict[payment_type] + 1

    return JsonResponse({
        'labels': list(payment_method_dict.keys()),
        'backgroundColor': generate_color_palette(len(payment_method_dict)),
        'borderColor': generate_color_palette(len(payment_method_dict)),
        'data': list(payment_method_dict.values()),
    })


def generate(request):
    if Purchase.objects.count() > 50:
        return JsonResponse({'detail': 'generate() has already been run.'})

    names = ["Jack", "John", "Mike", "Chris", "Kyle"]
    surname = ["Jackson", "Smith", "Tyson", "Musk", "Gates"]
    items = [Item.objects.get(pk=1), Item.objects.get(pk=2), Item.objects.get(pk=3),
             Item.objects.get(pk=4), Item.objects.get(pk=5)]

    for i in range(0, 2500):
        dt = pytz.utc.localize(datetime.now() - timedelta(days=random.randint(0, 5)*365))
        purchase = Purchase.objects.create(
            customer_full_name=names[random.randint(0, len(names)-1)] + " " + surname[random.randint(0, len(surname)-1)],
            item=items[random.randint(0, 2)],
            quantity=random.randint(1, 5),
            payment_method=Purchase.PAYMENT_METHODS[random.randint(0, 2)][0],
            time=timezone.now(),
            successful=True if random.randint(1, 2) == 1 else False,
        )
        purchase.time = dt
        purchase.save()

    return JsonResponse({'detail': 'Generated.'})
