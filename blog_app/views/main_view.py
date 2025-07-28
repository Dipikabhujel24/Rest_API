from rest_framework.decorators import api_view, permission_classes
from ..serializers import BlogSerializer, CategorySerializer, productSerializer
from rest_framework.response import Response
from rest_framework import status
from ..models import Blog


# @api_view(['POST', 'GET'])
# def blog(request):
#     if request.method =='POST':
#         serializer = BlogSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':"blog inserted successfully"}, status=status.HTTP_201_CREATED)
#         else:
#             return Response({'msg':"Failed to insert Blog"}, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'GET':
#         blog = Blog.objects.all()
#         serializer = BlogSerializer(blog, many=True)
#         return Response({'data': serializer.data}, status=status.HTTP_200_OK)


# @api_view(['PUT', 'DELETE', 'GET'])
# def blog_by_id(request, id):
#     try:
#          blog = Blog.objects.get(id=id)
#     except blog.DoesNotExist:
#         return Response({'message':"blog not found"})
    
#     if request.method == 'PUT':
#         serializer = BlogSerializer(blog, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':"blog updated successfully", 'data':serializer.data}, status=status.HTTP_204_NO_CONTENT)
#         else:
#             return Response({'msg':"failed to update blog data"},status=status.HTTP_404_NOT_FOUND)
        
#     elif request.method =='DELETE':
#         blog = Blog.objects.get(id=id)
#         blog.delete()
#         return Response({'msg': 'blog delete successfully '}, status=status.HTTP_204_NO_CONTENT)
    
#     elif request.method == 'GET':
#          blog = Blog.objects.get(id=id)
#          serializer = BlogSerializer(blog)
#          return Response({'data':serializer.data}, status=status.HTTP_200_OK)
#     else:
#         return Response({'err':'Failed to fetch.'})

#class-based view
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated

class BlogView(APIView):
    permission_classes = [AllowAny]
    
    def post(self,request):
      serializer = BlogSerializer(data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response({'msg':'Blog posted Successfully'},status=status.HTTP_201_CREATED)
      else:
         return Response({'msg':'Failed to post', 'err':serializer.errors},status=status.HTTP_404_NOT_FOUND)


    class BlogViewDetails(APIView):
     permission_classes= [AllowAny]

    def put(self,request,id):
        try:
            blog = Blog.objects.get(id=id)
        except:
            return Response({'msg':"Blog not found"},status=status.HTTP_404_NOT_FOUND)
        if request.method == 'PUT':
            serializer = BlogSerializer(blog, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response ({'msg':"Blog updated",'updated_data':serializer.data},status=status.HTTP_200_OK)
            else:
                return Response({'msg':"Failed to update Blog"},status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
            blog = Blog.objects.get(id=id)
            blog.delete()
            return Response({'msg':"Blog deleted"},status=status.HTTP_200_OK)
    def get(self,request,id):
            blog = Blog.objects.get(id=id)
            serializer=BlogSerializer(blog)
            return Response({'data':serializer.data},status=status.HTTP_200_OK)
    

@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def product_view(request):
    if request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Category added Suucessfully'},status=status.HTTP_201_CREATED)
        else:
            return Response({'msg': 'Failed To Add', 'err':serializer.errors},status=status.HTTP_404_NOT_FOUND)
        
    if request.method == 'GET':
        category = category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def category_view(request): 
    try:
        category = category.objects.get(id=id)
    except category.DoesNotExist:
        return Response({'msg': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Category updated successfully', 'updated_data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'msg': 'Failed to update category', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        category.delete()
        return Response({'msg': 'Category deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
