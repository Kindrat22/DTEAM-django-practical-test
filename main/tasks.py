from celery import shared_task
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from weasyprint import HTML
from django.conf import settings
from .models import CV
import tempfile


@shared_task
def send_cv_pdf_to_email(cv_id, email):
    cv = CV.objects.get(pk=cv_id)
    html_string = render_to_string('main/cv_pdf.html', {'cv': cv})
    with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as output:
        HTML(string=html_string).write_pdf(output.name)
        output.seek(0)
        mail = EmailMessage(
            subject=f"CV for {cv.firstname} {cv.lastname}",
            body="Please find attached the requested CV in PDF format.",
            from_email=getattr(settings, 'DEFAULT_FROM_EMAIL',
                               'noreply@example.com'),
            to=[email],
        )
        mail.attach(f"{cv.firstname}_{cv.lastname}_CV.pdf",
                    output.read(), 'application/pdf')
        mail.send()
