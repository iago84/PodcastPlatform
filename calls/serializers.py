from rest_framework import serializers
from .models import *


class CallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Call
        fields = "__all__"

class VideoCallSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoCall
        fields = "__all__"

class CallHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CallHistory
        fields = "__all__"
