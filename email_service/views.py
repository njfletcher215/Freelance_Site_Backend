from django.http import HttpResponse
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.views import APIView

class ping(APIView):

    def get(self, request):
        return HttpResponse('Hello!', status=status.HTTP_200_OK)

class send(APIView):

    def post(self, request):
        name = request.data['name']
        email = request.data['email']
        message = request.data['message']
        send_mail(
            'Message from {0}'.format(name),
            '{0} ({1}) sent the following message:\n\n\t{2}'.format(name, email, message),
            'from@yourdjangoapp.com',
            [
                'njfletcher215@gmail.com',
                'nathanfletcher@nathanfletcher.dev',
            ],
            fail_silently=False,
        )
        return HttpResponse(status=status.HTTP_200_OK)

        