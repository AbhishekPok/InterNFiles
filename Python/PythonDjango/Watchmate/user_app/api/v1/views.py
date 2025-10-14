from rest_framework.decorators import api_view
from user_app.api.v1.serializers import UserRegisterSerializer
from rest_framework.response import Response
from rest_framework.status import  HTTP_201_CREATED ,HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

@api_view(['POST'])
def user_register_view(request):
    serializer =UserRegisterSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user_instance = serializer.save()
        # token = Token.objects.create(user=user_instance)
        token,created_at = Token.objects.get_or_create(user = user_instance)
        serializer.data['token'] = token.key
        return Response({'token':token.key, **serializer.data}, status=HTTP_201_CREATED)
    
    return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])

def user_logout_view(request):
    Token.objects.filter(user= request.user).delete()
    return Response({"logout":"success"},status = HTTP_200_OK)
