from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..serializers import StudentSerializers
from ..models import Student
from django.shortcuts import get_object_or_404

@api_view(['POST'])
def add_student(request):
    if request.method == 'POST':
      serializer  = StudentSerializers(data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response({'message': 'Student Inserted successfully'},status=status.HTTP_201_CREATED)
      else:
         return Response({'message':'Failed to insert data'}, status=status.HTTP_400_BAD_REQUEST)
      
@api_view(['GET'])
def get_student(request):
   if request.method == 'GET':
      student = Student.objects.all()
      serializer = StudentSerializers(student, many=True)
      return Response({'data':serializer.data}, status=status.HTTP_200_OK)
   
@api_view(['PUT'])
def update_student(request, id):
  try:
   student = Student.objects.get(id=id)
  except Student.DoesNotExist:
     return Response({'msg':'Student not found.'})
  
  if request.method == 'PUT':
    serializer = StudentSerializers(student, data = request.data, partial=True)
    if serializer.is_valid():
       serializer.save()
       return Response({'msg':'Student Updated successfully.', 'data':serializer.data}, status=status.HTTP_204_NO_CONTENT)
    else:
       return Response({'err':'Failed to update'},status=status.HTTP_404_NOT_FOUND)
    

@api_view(['DELETE'])
def delete_student(request, id):
   try:
    student = get_object_or_404(Student, id=id)
   except Student.DoesNotExist:
      return Response({'msg':'Student not found.'})
   student.delete()
   return Response({'msg':'Student deleted Successfully.'})

@api_view(['GET'])
def get_student_by(request, id):
   try:
    student = Student.objects.get(id=id)
   except Student.DoesNotExist:
      return Response({'msg':'Student not found.'})
   
   serializer = StudentSerializers(student)
   return Response({'data':serializer.data},status=status.HTTP_200_OK)
      

   