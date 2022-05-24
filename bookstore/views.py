from rest_framework import viewsets
from .models import Book, Journal
from .serializers import BookSerializer, JournalSerializer
from rest_framework.permissions import AllowAny, IsAdminUser

class BookViewSet(viewsets.ModelViewSet):
	queryset = Book.objects.all()
	serializer_class = BookSerializer

	def get_permissions(self):
		if self.action == 'list':
			permission_classes = (AllowAny,)
		elif self.action == 'retrieve':
			permission_classes = (AllowAny,)
		elif self.action == 'create':
			permission_classes = (IsAdminUser,)
		elif self.action == 'update':
			permission_classes = (IsAdminUser,)
		elif self.action == 'destroy':
			permission_classes = (IsAdminUser,)

class JournalViewSet(viewsets.ModelViewSet):
	queryset = Journal.objects.all()
	serializer_class = JournalSerializer

	def get_permissions(self):
		if self.action == 'list':
			permission_classes = (AllowAny,)
		elif self.action == 'retrieve':
			permission_classes = (AllowAny,)
		elif self.action == 'create':
			permission_classes = (IsAdminUser,)
		elif self.action == 'update':
			permission_classes = (IsAdminUser,)
		elif self.action == 'destroy':
			permission_classes = (IsAdminUser,)
