from rest_framework import viewsets
from .serializer import PropertySerializer
from .models import Property
from rest_framework import authentication, permissions

class PropertyViewSet(viewsets.ModelViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [permissions.AllowAny]
        return super(PropertyViewSet, self).get_permissions()