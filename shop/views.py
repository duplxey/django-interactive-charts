import random
from datetime import datetime, timedelta

import pytz
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Count, F, Sum, Avg
from django.db.models.functions import TruncMonth, ExtractYear
from django.http import JsonResponse
from django.utils import timezone

from shop.models import Purchase, Item

months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']

colorPalette = ["#55efc4", "#81ecec", "#a29bfe", "#ffeaa7", "#fab1a0", "#ff7675", "#fd79a8"]
colorPrimary = "#79aec8"
colorSuccess = colorPalette[0]
colorDanger = colorPalette[5]


def generate_color_palette(amount):
    palette = []
    i = 0
    while i < len(colorPalette) and len(palette) < amount:
        palette.append(colorPalette[i])
        i += 1
        if i == len(colorPalette) and len(palette) < amount:
            i = 0
    return palette


@staff_member_required
def get_filter_options(request):
    grouped_purchases = Purchase.objects.annotate(year=ExtractYear('time'))\
        .values('year').order_by('-year').distinct()

    options = []

    for purchase in grouped_purchases:
        options.append(purchase['year'])

    return JsonResponse({
        'options': options,
    })


@staff_member_required
def get_sales_chart(request, year):
    purchases = Purchase.objects.filter(time__year=year)
    grouped_purchases = purchases.annotate(price=F('item__price')).annotate(month=TruncMonth('time'))\
        .values('month').annotate(average=Sum('item__price')).values('month', 'average').order_by('month')

    sales_dict = dict()

    for month in months:
        sales_dict[month] = 0

    for group in grouped_purchases:
        sales_dict[months[group['month'].month-1]] = round(group['average'], 2)

    return JsonResponse({
        'title': f'Sales in {year}',
        'data': {
            'labels': list(sales_dict.keys()),
            'datasets': [{
                'label': 'Amount ($)',
                'backgroundColor': colorPrimary,
                'borderColor': colorPrimary,
                'data': list(sales_dict.values()),
            }]
        },
    })


@staff_member_required
def spend_per_customer_chart(request, year):
    purchases = Purchase.objects.filter(time__year=year)
    grouped_purchases = purchases.annotate(price=F('item__price')).annotate(month=TruncMonth('time'))\
        .values('month').annotate(average=Avg('item__price')).values('month', 'average').order_by('month')

    spend_per_customer_dict = dict()

    for month in months:
        spend_per_customer_dict[month] = 0

    for group in grouped_purchases:
        spend_per_customer_dict[months[group['month'].month-1]] = round(group['average'], 2)

    return JsonResponse({
        'title': f'Spend per customer in {year}',
        'data': {
            'labels': list(spend_per_customer_dict.keys()),
            'datasets': [{
                'label': 'Amount ($)',
                'backgroundColor': colorPrimary,
                'borderColor': colorPrimary,
                'data': list(spend_per_customer_dict.values()),
            }]
        },
    })


@staff_member_required
def payment_success_chart(request, year):
    purchases = Purchase.objects.filter(time__year=year)

    return JsonResponse({
        'title': f'Payment success rate in {year}',
        'data': {
            'labels': ['Successful', 'Unsuccessful'],
            'datasets': [{
                'label': 'Amount ($)',
                'backgroundColor': [colorSuccess, colorDanger],
                'borderColor': [colorSuccess, colorDanger],
                'data': [
                    purchases.filter(successful=True).count(),
                    purchases.filter(successful=False).count(),
                ],
            }]
        },
    })


@staff_member_required
def payment_method_chart(request, year):
    purchases = Purchase.objects.filter(time__year=year)
    grouped_purchases = purchases.values('payment_method').annotate(count=Count('id'))\
        .values('payment_method', 'count').order_by('payment_method')

    payment_method_dict = dict()

    for payment_method in Purchase.PAYMENT_METHODS:
        payment_method_dict[payment_method[1]] = 0

    for group in grouped_purchases:
        payment_method_dict[dict(Purchase.PAYMENT_METHODS)[group['payment_method']]] = group['count']

    return JsonResponse({
        'title': f'Payment method rate in {year}',
        'data': {
            'labels': list(payment_method_dict.keys()),
            'datasets': [{
                'label': 'Amount ($)',
                'backgroundColor': generate_color_palette(len(payment_method_dict)),
                'borderColor': generate_color_palette(len(payment_method_dict)),
                'data': list(payment_method_dict.values()),
            }]
        },
    })


@staff_member_required
def generate(request):
    if Purchase.objects.count() > 50:
        return JsonResponse({'detail': 'generate() has already been run.'})

    names = ["Jack", "John", "Mike", "Chris", "Kyle"]
    surname = ["Jackson", "Smith", "Tyson", "Musk", "Gates"]
    items = [
        Item.objects.create(name="Socks", price=6.5), Item.objects.create(name="Pants", price=12),
        Item.objects.create(name="T-Shirt", price=8), Item.objects.create(name="Boots", price=9),
        Item.objects.create(name="Sweater", price=3), Item.objects.create(name="Underwear", price=9),
        Item.objects.create(name="Cap", price=5), Item.objects.create(name="Leggings", price=7),
    ]

    for i in range(0, 2500):
        dt = pytz.utc.localize(datetime.now() - timedelta(days=random.randint(0, 1825)))
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
