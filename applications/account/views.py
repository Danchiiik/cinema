from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from applications.account.serializer import RegisterSerializer

User = get_user_model()

class RegisterApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    
    
    



