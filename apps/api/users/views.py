from rest_framework.request import Request
from rest_framework.views import APIView
from .models import User
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .serializers import UsersSerializer
from rest_framework.response import Response
from rest_framework.exceptions import APIException, ParseError
from rest_framework import status, serializers
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .tasks import my_task

class UserProfileAPIView(APIView):
    serializer_class = UsersSerializer
    
    @method_decorator(cache_page(60 * 15))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request: Request) -> Response:
        try:
            search_query = request.query_params.get('search', None)
            limit = int(request.query_params.get('limit', 10))
            skip = (int(request.query_params.get('page', 1)) - 1) * limit
            my_task.delay()
            if search_query:
                queryset = User.objects.filter(Q(name__icontains=search_query) | Q(email__icontains=search_query)).order_by('name')[skip:skip + limit]
                
            # Pagination
            # paginator = Paginator(queryset, 10)
            # page_number = request.query_params.get('page', 1)
            # page_obj = paginator.get_page(page_number)
            
            serializer = UsersSerializer(queryset, many=True)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        try:
            serializer = UsersSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            print(serializer.data)
        except serializers.ValidationError as error:
            raise error
        except Exception as e:
            return APIException({"error": str(e)})
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def patch(self, request: Request, pk: int) -> Response:
        try:
            if not request.data:
                raise Exception("request body is empty. please provide valid data.")
            
            user = get_object_or_404(User, pk=pk)
            serializer = UsersSerializer(user, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        except serializers.ValidationError as error:
            raise error
        except Exception as e:
            raise APIException({"error": str(e)})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request: Request, pk: int) -> Response:
        try:
            user = get_object_or_404(User, pk=pk)
            user.delete()
        except Exception as e:
            raise APIException({"error": str(e)})
        
        return Response(status=status.HTTP_204_NO_CONTENT)
