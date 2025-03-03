from rest_framework import viewsets
from .models import News,Contact
from .serializers import NewsSerializer,ContactSerializer

class NewsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = News.objects.all().order_by('-created_at')
    serializer_class = NewsSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all().order_by('-created_at')
    serializer_class = ContactSerializer
    http_method_names = ['get', 'post']  # Faqat GET va POST ruxsat