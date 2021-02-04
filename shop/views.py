from django.http import JsonResponse


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



    return JsonResponse({
        'labels': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
        'backgroundColor': ['#79AEC8'],
        'borderColor': ['#79AEC8'],
        'data': [1, 2, 3, 4, 5],
    })


def payment_method_chart(request, year):
    return JsonResponse({
        'labels': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
        'backgroundColor': ['#79AEC8'],
        'borderColor': ['#79AEC8'],
        'data': [1, 2, 3, 4, 5],
    })
