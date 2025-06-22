from django.utils.deprecation import MiddlewareMixin
from .models import RequestLog


class RequestLogMiddleware(MiddlewareMixin):
    def process_request(self, request):
        user = request.user if request.user.is_authenticated else None
        RequestLog.objects.create(
            method=request.method,
            path=request.path,
            query_string=request.META.get('QUERY_STRING', ''),
            remote_ip=request.META.get('REMOTE_ADDR'),
            user=user
        )
