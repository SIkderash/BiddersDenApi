from rest_framework import serializers 
from users.models import User
 
 
class UserSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = User
        fields = ('id',
                  'name',
                  'phone_number',
                  'email',
                  'address',
                  'username',
                  'password',)