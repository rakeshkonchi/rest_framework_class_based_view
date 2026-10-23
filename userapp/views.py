from rest_framework.response import Response
from rest_framework.views import APIView
from userapp.serializers import UserSerializer,StudentSerializer
from userapp.models import User,Student
from django.shortcuts import get_object_or_404

from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView,RetrieveDestroyAPIView

class UserAPIView(APIView):
    def get(self,request,id=None):
        if id :
            user = get_object_or_404(User,id = id)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        else:
            users = User.objects.all()
            serializers = UserSerializer(users,many=True)
            return Response(serializers.data)

    def post(self,request):
        serializers = UserSerializer(data = request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.validated_data)

    def put(self,request,id):
        user = get_object_or_404(User,id = id)
        serializers = UserSerializer(user,data = request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.validated_data)

    def patch(self,request,id):
            user = get_object_or_404(User,id = id)
            serializers = UserSerializer(user,data = request.data,partial=True)
            serializers.is_valid(raise_exception=True)
            serializers.save()
            return Response(serializers.validated_data)
    def delete(self,request,id):
         user = get_object_or_404(User,id = id)
         user.delete()
         return Response({"message":"user deleted successfully"})


#generic views

class StudentListAPIView(ListAPIView):
     queryset = Student.objects.all()   #work with student model
     serializer_class = StudentSerializer

class StudentCreateAPIView(CreateAPIView):
     queryset = Student.objects.all()   #it's not mandatory for this  (optional)
     serializer_class = StudentSerializer

class StudentRetriveAPIView(RetrieveAPIView):
     queryset = Student.objects.all()   #it's not mandatory for this  (optional)
     serializer_class = StudentSerializer

class StudentUpdateAPIView(UpdateAPIView):
     queryset = Student.objects.all()   #it's not mandatory for this  (optional)
     serializer_class = StudentSerializer

class StudentDestroyAPIView(DestroyAPIView):
     queryset = Student.objects.all()   #it's not mandatory for this  (optional)
     serializer_class = StudentSerializer


#mixin generic view


class GetWithPost(ListCreateAPIView):
     queryset = Student.objects.all()   #it's not mandatory for this  (optional)
     serializer_class = StudentSerializer

class GetWithUpdate(RetrieveUpdateAPIView):
     queryset = Student.objects.all()   #it's not mandatory for this  (optional)
     serializer_class = StudentSerializer

class GetWithDelete(RetrieveDestroyAPIView):
     queryset = Student.objects.all()   #it's not mandatory for this  (optional)
     serializer_class = StudentSerializer

class GetWithUpdateAndDelete(RetrieveUpdateDestroyAPIView):
     queryset = Student.objects.all()   #it's not mandatory for this  (optional)
     serializer_class = StudentSerializer