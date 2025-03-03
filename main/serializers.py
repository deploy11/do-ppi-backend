from rest_framework import serializers
from .models import News,Contact

class NewsSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = ['id', 'title', 'content', 'image', 'image_url', 'created_at']

    def get_image_url(self, obj):
        if obj.image:
            return obj.image.url
        return None
    
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'subject', 'telefon', 'message', 'created_at']
