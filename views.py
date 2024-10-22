from django.shortcuts import render, redirect
from .forms import ApplicationForm
from .models import Application
from django.contrib import messages

def apply(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            email = form.cleaned_data['email']
            # Check if the student has already applied
            if Application.objects.filter(email=email).exists():
                application = Application.objects.get(email=email)
                messages.error(request, f"You have already applied on {application.application_date}.")
            else:
                form.save()
                messages.success(request, "Application submitted successfully!")
                return redirect('view_status')
    else:
        form = ApplicationForm()
    return render(request, 'applications/apply.html', {'form': form})

def view_status(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            application = Application.objects.get(email=email)
            return render(request, 'applications/status.html', {'application': application})
        except Application.DoesNotExist:
            messages.error(request, "No application found for this email.")
    return render(request, 'applications/view_status.html')
