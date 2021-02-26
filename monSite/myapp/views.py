from django.shortcuts import render
from django.http import HttpResponse, JsonResponse,Http404
from .models import book
from rest_framework.views import APIView
from rest_framework import status,serializers
from .serializers import bookSerializer
def index(request):
    return HttpResponse("hello, bienvenue dans le site")

class bookList(APIView):
    """ list all books, or create a book
    """
    def get(self, request, format=None):
        books=book.objects.all()
        #book.object.all() fait la requete pour nous pour recuperer tous les livres
        serializer=bookSerializer(books,many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, format=None):
        serializer=bookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse (serializer.data,safe=false,status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, safe=False,status= status.HTTP_400_BAD_REQUEST)
""" les méthodes get(...) et put(...) sont définit pour dire qu'on va maitenant utiliser dans cette page
 ces méthodes là pour récuperer ou envoyer quelques choses au serveur (à l'url). du coup maintenat qu'ils ont 
 été définit, on ne peut plus utiliser POST. car c'est que GET et PUT qui sont redéfinit et ce sont qu'eux qui sont
 disponible. quand on va faire GET["id"] dans la page booklist, c'est la méthode get() qui sera appelé.
 """
    
class bookDetail(APIView):
    """ retrieve, update or delete a book
    """
    def get_object(self,pk):
      try:
         return book.objects.get(pk=pk)
      except book.DoesNotExist:
         raise Http404
    def get(self, request,pk, format=None):
        book=self.get_object(pk)
        serializer=bookSerializer(book)
        return JsonResponse(serializer.data, safe=False)
    
    
    def put(self, request,pk, format=None):
        book=self.get_object(pk)
        serializer=bookSerializer(book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse (serializer.data, safe=false)
        return JsonResponse(serializer.errors, safe=False,status= status.HTTP_400_BAD_REQUEST)

    def delete(self, request,pk, format=None):
        book=self.get_object(pk)
        book.delete()
        return JsonResponse({},safe=False, status=status.HTTP_204_NO_CONTENT)
    

# Create your views here.
