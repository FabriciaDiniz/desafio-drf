from rest_framework.response import Response
from rest_framework.decorators import api_view

from medicar.users.serializers import UserSerializer


#TODO: formatar para viewset
@api_view(['POST'])
def registration_view(request):
    serializer = UserSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        user = serializer.save()
        data['response'] = 'Novo usuário registrado com sucesso'
        data['email'] = user.email
        data['username'] = user.username
    else:
        data = serializer.errors
    return Response(data)
