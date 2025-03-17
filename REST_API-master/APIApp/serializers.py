from rest_framework import serializers
from .models import post_tbl

class post_serial(serializers.ModelSerializer):
    class Meta:
        model = post_tbl
        fields = '__all__'
