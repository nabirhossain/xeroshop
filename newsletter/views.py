from django.shortcuts import render
from .forms import NewsUserForm
from . models import NewsUsers
from django.core.mail import send_mail


def newsletter_subscribe(request):
    if request.method == 'POST':
       form = NewsUserForm(request.POST)
       if form.is_valid():
            #cd = form.cleaned_data
            instance = form.save(commit=False)
            if NewsUsers.objects.filter(email=instance.email).exists():
                print('your email is already added to our database')
            else:
               instance.save()
               print('your email has been submitted to our database')
               send_mail('Laughing blog tutorial series', 'welcome', 'nabirhossain13@gmail.com', ['instance.email'],fail_silently=False)
    else:
        form = NewsUserForm()
    context = {'form':form}
    template = 'subscribe.html'
    return render(request, template, context)