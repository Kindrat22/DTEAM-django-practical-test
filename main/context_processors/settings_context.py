from django.conf import settings


def settings_context(request):
    return {
        'DEBUG': settings.DEBUG,
        'ALLOWED_HOSTS': settings.ALLOWED_HOSTS,
        'INSTALLED_APPS': settings.INSTALLED_APPS,
        'DATABASES': settings.DATABASES,
        # Add more settings as needed
    }
