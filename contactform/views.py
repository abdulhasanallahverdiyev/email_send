from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail


def index(request):
    if request.method == 'POST':
        name = request.POST.get('full-name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message
        }
        message = '''
          New Message: {}

          From: {}
          Fenn: {}
          
          '''.format(data['message'],data['email'],data['subject'])

        send_mail(data['name'] ,message, '', ['iamabdulhasan9@gmail.com'])
        return HttpResponse('Mesaj göndərildi!!!!')
    return render(request, 'index.html', {})
