from rest_framework import serializers
from careers import models as careers_models

class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('career','full_name','phone','cv')
        model = careers_models.Career_Apply
