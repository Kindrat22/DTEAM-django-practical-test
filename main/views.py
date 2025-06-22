from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from .models import CV
import weasyprint
from rest_framework import viewsets
from .serializers import CVSerializer
from django.contrib import messages
from .tasks import send_cv_pdf_to_email
import openai
from django.conf import settings


def cv_list(request):
    cvs = CV.objects.all()
    return render(request, 'main/cv_list.html', {'cvs': cvs})


def cv_detail(request, pk):
    cv = get_object_or_404(CV, pk=pk)
    translated = None
    selected_language = None
    if request.method == 'POST':
        if 'email' in request.POST:
            email = request.POST.get('email')
            if email:
                send_cv_pdf_to_email.delay(cv.pk, email)
                filename = f"cv_{cv.firstname}_{cv.lastname}.pdf"
                messages.success(
                    request, f'File "{filename}" is being sent to {email}.')
                return redirect('cv_list')
        elif 'translate' in request.POST:
            selected_language = request.POST.get('language')
            if selected_language:
                # Compose text to translate
                text = f"Name: {cv.firstname} {cv.lastname}\nSkills: {cv.skills}\nProjects: {cv.projects}\nBio: {cv.bio}\nContacts: {cv.contacts}"
                # Map language codes to names for prompt
                lang_map = {
                    'kw': 'Cornish', 'gv': 'Manx', 'br': 'Breton', 'iu': 'Inuktitut', 'kl': 'Kalaallisut',
                    'rmy': 'Romani', 'oc': 'Occitan', 'lad': 'Ladino', 'se': 'Northern Sami', 'hsb': 'Upper Sorbian',
                    'csb': 'Kashubian', 'zza': 'Zazaki', 'cv': 'Chuvash', 'liv': 'Livonian', 'tsd': 'Tsakonian',
                    'srm': 'Saramaccan', 'bi': 'Bislama'
                }
                lang_name = lang_map.get(selected_language, selected_language)
                # Call OpenAI API
                openai.api_key = getattr(settings, 'OPENAI_API_KEY', None)
                if openai.api_key:
                    try:
                        client = openai.OpenAI(api_key=openai.api_key)
                        response = client.chat.completions.create(
                            model="gpt-3.5-turbo",
                            messages=[
                                {"role": "system", "content": f"You are a helpful assistant that translates text to {lang_name}."},
                                {"role": "user", "content": text}
                            ]
                        )
                        translated = response.choices[0].message.content.strip(
                        )
                    except Exception as e:
                        messages.error(
                            request, f"Translation error: {str(e)[:100]}")
                else:
                    messages.error(request, "OpenAI API key not configured.")
    return render(request, 'main/cv_detail.html', {'cv': cv, 'translated': translated, 'selected_language': selected_language})


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
