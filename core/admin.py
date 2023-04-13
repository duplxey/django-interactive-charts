# core/admin.py

from django.contrib import admin
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.urls import path


@staff_member_required
def admin_statistics_view(request):
    return render(request, 'admin/statistics.html', {
        'title': 'Statistics'
    })


class CustomAdminSite(admin.AdminSite):
    def get_app_list(self, request, _=None):
        app_list = super().get_app_list(request)
        app_list += [
            {
                'name': 'My Custom App',
                'app_label': 'my_custom_app',
                'models': [
                    {
                        'name': 'Statistics',
                        'object_name': 'statistics',
                        'admin_url': '/admin/statistics',
                        'view_only': True,
                    }
                ],
            }
        ]
        return app_list

    def get_urls(self):
        urls = super().get_urls()
        urls += [
            path('statistics/', admin_statistics_view, name='admin-statistics'),
        ]
        return urls
