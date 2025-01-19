
from .models import Home

from rest_framework.serializers import ModelSerializer

class HomeSerializer(ModelSerializer):
    class Meta:
        model=Home 
        fields=["title",'subtitle',"call_to_action_text","call_to_action_url","image","created_at","updated_at"]