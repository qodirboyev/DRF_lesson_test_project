from django.shortcuts import render
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from .models import Student
from .serializer import StudentSerializer
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
# Create your views here.


###############---------------- funksiya bilan api view yozish
#
# @api_view(['GET','POST'])
# def students(request):
#     if request.method=='GET':
#         students = Student.objects.all()
#         serializer = StudentSerializer(students, many=True)
#         return Response(serializer.data)
#     elif request.method=='POST':
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
#
#
#
# @api_view(['GET','PUT','PATCH','DELETE'])
# def student_detail(request,pk):
#     try:
#         student = Student.objects.get(pk=pk)
#     except Student.DoesNotExist:
#         return Response({"error":"topilmadi"},status=status.HTTP_404_NOT_FOUND)
#
#     if request.method=='GET':
#         serializer = StudentSerializer(student)
#         return Response(serializer.data)
#
#     elif request.method=='PUT':
#         serializer = StudentSerializer(student,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'PATCH':
#         serializer=StudentSerializer(student,data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method=='DELETE':
#         student.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
###############---------------- funksiya bilan api view yozish


#############--------APIView kilasi bilan yaratish
#
# class Student_APIview(APIView):
#     def get(self, request):
#         students = Student.objects.all()
#         serializer = StudentSerializer(students, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
#
# class Student_Detail(APIView):
#     def get_object(self, pk):
#         try:
#             return Student.objects.get(pk=pk)
#         except Student.DoesNotExist:
#             return None
#
#     def get(self, request, pk):
#         student = self.get_object(pk)
#         if student is None:
#             return Response(
#                 {"error": "Student not found"}
#             ,status=status.HTTP_404_NOT_FOUND)
#         serializer = StudentSerializer(student)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         student = self.get_object(pk)
#         if student is None:
#             return Response(
#                 {"error": "Student not found"}
#             )
#         serializer = StudentSerializer(student, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def patch(self, request, pk):
#         student = self.get_object(pk)
#         if student is None:
#             return Response({"error": "Student not found"},status=status.HTTP_404_NOT_FOUND)
#         serializer = StudentSerializer(student, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         student = self.get_object(pk)
#         if student is None:
#             return Response({"error": "Student not found"},status=status.HTTP_404_NOT_FOUND)
#         student.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#############--------APIView kilasi bilan yaratish





########------------Tayor generics viewlar
# class StudentList(ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#
#
# class StudentDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
########------------Tayor generics viewlar




#################------------------ModelViewSet bilan ishlash
class StudentModelViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = (DjangoFilterBackend,SearchFilter,OrderingFilter)
    filterset_fields=["name"]
    search_fields = ["name"]
    ordering_fields = ["id","name"]

#################------------------ModelViewSet bilan ishlash


class ProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,format=None):
        return Response({"username":request.user.username,"id":request.user.id})