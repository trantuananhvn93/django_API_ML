from rest_framework import serializers
from . models import car

class carSerializers(serializers.ModelSerializer):
	class Meta:
		model=car
		fields='__all__'
