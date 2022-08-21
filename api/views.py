from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework import generics

from mailings.models import Contact, Mailing, Message

from .serializers import (ContactSerializer, MailinglistSerializer,
                          MailingSerializer, MessageSerializer)

from rest_framework.response import Response

from django.shortcuts import render
from django.urls import reverse

class APIRootView(generics.GenericAPIView):
    def list(self, request):
        return Response({
            'contacts': reverse('contact-list', request=request),
            'mailings': reverse('mailing-list', request=request),
            'messages': reverse('message-list', request=request),
        })


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('tag', 'code')


class MailingViewSet(viewsets.ModelViewSet):
    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return MailinglistSerializer
        return MailingSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


def index(request):
    return render(request, 'index.html')