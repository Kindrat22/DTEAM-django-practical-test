from django.shortcuts import render
from .models import RequestLog


def recent_logs(request):
    logs = RequestLog.objects.order_by('-timestamp')[:10]
    return render(request, 'audit/recent_logs.html', {'logs': logs})
