from rest_framework import serializers
from .models import userData,Hackathon,Group,GroupMember,Team,TeamMember,Messages

class userSerializer(serializers.ModelSerializer):
    class Meta :
        model = userData
        fields = '__all__'

class HackathonSerializer(serializers.ModelSerializer):
    class Meta :
        model = Hackathon
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    class Meta :
        model = Group
        fields = '__all__'

class GroupMemberSerializer(serializers.ModelSerializer):
    class Meta :
        model = GroupMember
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    class Meta :
        model = Team
        fields = '__all__'

class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta :
        model = TeamMember
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta :
        model = Messages
        fields = '__all__'