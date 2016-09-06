from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from jrc_profile.profiles.models import Profile
from jrc_profile.profiles.serializers import ProfileSerializer
from rest_framework import permissions


@api_view(['POST', 'GET'])
@permission_classes((permissions.AllowAny, ))
def profile_list(request):

    if request.method == "POST":
        serializer = ProfileSerializer(date=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'GET':
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_403_FORBIDDEN)


@api_view(['GET', 'PUT', 'DELETE'])
def profile_detail(request, pk):

    try:
        profile = Profile.objects.get(pk=pk)
    except Profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
