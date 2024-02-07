from Tasks.models import Tasks
from rest_framework import serializers

class taskSerializer(serializers.ModelSerializer):
    Created_at = serializers.ReadOnlyField()
    Updated_at = serializers.ReadOnlyField()
    class Meta:
        model =  Tasks
        fields = ['id','Name','Description','Status','Created_at','Updated_at']