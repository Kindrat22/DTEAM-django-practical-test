from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from .models import CV
import weasyprint
from rest_framework import viewsets
from .serializers import CVSerializer
from django.contrib import messages
from .tasks import send_cv_pdf_to_email


def cv_list(request):
    cvs = CV.objects.all()
    return render(request, 'main/cv_list.html', {'cvs': cvs})


def cv_detail(request, pk):
    cv = get_object_or_404(CV, pk=pk)
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            send_cv_pdf_to_email.delay(cv.pk, email)
            filename = f"cv_{cv.firstname}_{cv.lastname}.pdf"
            messages.success(
                request, f'File "{filename}" is being sent to {email}.')
            return redirect('cv_list')
    return render(request, 'main/cv_detail.html', {'cv': cv})


def cv_pdf(request, pk):
    cv = get_object_or_404(CV, pk=pk)
    html = render_to_string('main/cv_pdf.html', {'cv': cv})
    pdf = weasyprint.HTML(string=html).write_pdf()
    filename = f"cv_{cv.firstname}_{cv.lastname}.pdf"
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    return response


def settings_page(request):
    return render(request, 'main/settings.html')


class CVViewSet(viewsets.ModelViewSet):
    queryset = CV.objects.all()
    serializer_class = CVSerializer
