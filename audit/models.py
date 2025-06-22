from django.db import models
from django.contrib.auth import get_user_model


class RequestLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    method = models.CharField(max_length=10)
    path = models.CharField(max_length=255)
    query_string = models.TextField(blank=True)
    remote_ip = models.GenericIPAddressField(null=True, blank=True)
    user = models.ForeignKey(get_user_model(), null=True,
                             blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.timestamp} {self.method} {self.path}"
