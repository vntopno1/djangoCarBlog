from rest_framework import serializers
from django.conf import settings
from .models import blog, category

class blogSerializer(serializers.ModelSerializer):
    class Meta:
        model = blog
        fields = '__all__'

class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = '__all__'

#def relative_to_absolute(url):
#    return 'http://127.0.0.1:8000' + url

#class FileFieldSerializer(serializers.Field):
#    def to_representation(self, value):
#        url = value.url
#        if url and url.startswitch('/'):
#            url = relative_to_absolute(url)
#        return url


