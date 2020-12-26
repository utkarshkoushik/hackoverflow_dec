from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

from rest_framework import generics, permissions,viewsets,status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from .models import userData,Hackathon,Group,GroupMember,Team,TeamMember,Messages
from .serializer import HackathonSerializer,userSerializer,GroupSerializer,GroupMemberSerializer,TeamSerializer,TeamMemberSerializer,MessageSerializer
from rest_framework import permissions
from rest_framework import viewsets
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from knox.models import AuthToken
from django.contrib import auth

class userDataApi(viewsets.ModelViewSet):
    queryset = userData.objects.all()
    serializer_class = userSerializer
    permission_classes = [permissions.AllowAny]


csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def create_user(request):
    email = request.data.get("email")
    password = request.data.get("password")
    first_name = request.data.get("first_name")
    last_name = request.data.get("last_name")
    email = email.lower()
    username = email
    try:
        user = User.objects.get(username=username)
    except ObjectDoesNotExist:
        user = User.objects.create_user(username, email, password)
        user = User.objects.get(pk=user.id)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        token = AuthToken.objects.create(user)
    
    return Response({
        'user_id': user.id,
        'name': user.first_name+" "+user.last_name,
        'email': user.email,
    })

csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    email = request.data['email']
    password = request.data['password']
    user_name = email.lower()
    any_user = User.objects.filter(username=user_name)
    if any_user.exists() == False:
        return Response({
            'error_message': 'The email id doesn\'t exist'
        })
    user = authenticate(username=user_name, password=password)
    if user is None:
        return Response({
            'incorrect password'
        })
    else:
        request.session.set_expiry(864000)
        auth.login(request, user)
        token = AuthToken.objects.create(user)
        return Response({
            'user_id': user.id,
            'name': user.first_name+" "+user.last_name,
            'email': user.email,
            
        })

    
csrf_exempt
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def logout(request):
    user = request.user
    auth.logout(request)
    return Response({
        'error_message': 'SUCCESS'
    })

class HackathonAPi(viewsets.ModelViewSet):
    queryset = Hackathon.objects.all()
    serializer_class = HackathonSerializer
    permission_classes = [permissions.IsAuthenticated]

class TeamAPi(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticated]    
csrf_exempt
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_team_memeber(request):
    unique_code = request.data['unique_code']
    team = Team.objects.filter(unique_code=unique_code)
    member = request.user
    team_member = TeamMember()
    team_member.team = team
    team_member.member = member
    team_member.save()
    return Response({
        'team': team.id,
        'error_message': "success"
    })

class GroupAPi(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated] 
csrf_exempt
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_group_memeber(request):
    unique_code = request.data['unique_code']
    group = Group.objects.filter(unique_code=unique_code)
    member = request.user
    team_member = GroupMember()
    team_member.group = group
    team_member.member = member
    team_member.save()
    return Response({
        'team': team.id,
        'error_message': "success"
    })

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_message(request):
    sender = request.user
    group = Group.objects.filter(id=request.data['group_id'])
    msg = request.data['message']
    message = Messages()
    message.message = msg
    message.sender = sender
    message.group = group
    message.save()
    return Response({
        'error_message': 'success'
    })
csrf_exempt
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def get_group_message(request):
    grp = request.data['group_id']
    group = Group.objects.get(id=grp)
    message = Messages.objects.filter(group=group)
    all_msg=[]
    for i in message:
        m={
            'user_name': i.sender.first_name+" "+i.sender.last_name,
            'user_id': i.sender.id,
            'msg': i.message,
            'group_id': i.group.id,
            'time': i.created_at
        }
        all_msg.append(m)
    return Response({
        'msg_list': all_msg
    })
csrf_exempt
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def get_user_grp(request):
    user = request.user
    grps = GroupMember.objects.filter(member=user)
    all_grp = []
    for i in grps:
        g = {
            'name': i.group.name,
            'type': i.group.type,
            'unique_code': i.group.unique_code,
            'id': i.group.id,
        }
        all_grp.append(g)

    return Response({
        'all_grp': all_grp
    })
csrf_exempt
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def get_all_grp_members(request):
    grp = request.data['grp_id']
    all_grp_mem = []
    group = Group.objects.get(id=grp)
    grps = GroupMember.objects.filter(group=group)
    for i in grps:
        g = {
            'name': i.member.first_name+" "+i.member.last_name,
            'email': i.member.email
        }
csrf_exempt
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_user_data(request):
    user = request.user
    if userData.objects.filter(user=user).exists():
        data={
            'name': user.first_name+" "+user.last_name,
            'email': user.email,
            'college': user.userdata.college,
            'gender': user.userdata.gender,
            'year': user.userdata.year,
            'hackathon' : user.userdata.current_hackathon.name,
            'pic': user.userdata.pic,
        }
        return Response({
            'data': data
        })
    else:
        return Response({
            'error_message': 'user not in any hackathon',
        })