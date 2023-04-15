from django.urls import path

from . import views

urlpatterns = [
    path("statistics/", views.statistics_view, name="shop-statistics"),
    path("chart/filter-options/", views.get_filter_options, name="chart-filter-options"),
    path("chart/sales/<int:year>/", views.get_sales_chart, name="chart-sales"),
    path("chart/spend-per-customer/<int:year>/", views.spend_per_customer_chart, name="chart-spend-per-customer"),
    path("chart/payment-success/<int:year>/", views.payment_success_chart, name="chart-payment-success"),
    path("chart/payment-method/<int:year>/", views.payment_method_chart, name="chart-payment-method"),
]
