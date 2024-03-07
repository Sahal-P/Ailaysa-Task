from rest_framework.request import Request
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .serializers import UsersSerializer
from rest_framework.response import Response
from rest_framework.exceptions import APIException, ParseError
from rest_framework import status, serializers
from django.core.paginator import Paginator
from django.http import StreamingHttpResponse
from rest_framework.views import APIView
from django.views.generic import View
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .tasks import count_pathname
from django.db.models import Q
from .models import User
import asyncio
import time


class UserProfileAPIView(APIView):
    """
    API view for managing user profiles.

    Attributes:
        serializer_class: The serializer class for serializing/deserializing user data.
    """

    serializer_class = UsersSerializer

    @method_decorator(cache_page(60 * 15))
    def dispatch(self, request, *args, **kwargs):
        """
        Dispatch method to handle caching.

        Args:
            request: The HTTP request object.
            args: Additional positional arguments.
            kwargs: Additional keyword arguments.

        Returns:
            Response: The HTTP response object.
        """
        return super().dispatch(request, *args, **kwargs)

    def get(self, request: Request) -> Response:
        """
        Get method to retrieve user profiles.

        Args:
            request: The HTTP request object.

        Returns:
            Response: The HTTP response object containing user data.
        """
        try:
            search_query = request.query_params.get("search", None)
            limit = int(request.query_params.get("limit", 10))
            skip = (int(request.query_params.get("page", 1)) - 1) * limit

            if search_query:
                queryset = User.objects.filter(
                    Q(name__icontains=search_query) | Q(email__icontains=search_query)
                ).order_by("name")[skip : skip + limit]

            # Pagination
            # paginator = Paginator(queryset, 10)
            # page_number = request.query_params.get('page', 1)
            # page_obj = paginator.get_page(page_number)

            serializer = UsersSerializer(queryset, many=True)

        except Exception as e:
            raise APIException({"error": str(e)})

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        """
        Post method to create a new user profile.

        Args:
            request: The HTTP request object.

        Returns:
            Response: The HTTP response object containing the newly created user profile data.
        """
        try:
            serializer = UsersSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            pathname = request.query_params.get(
                "pathname", "media/images/category/subcategory/product/profile.jpeg"
            )
            count_pathname.delay(pathname)
        except serializers.ValidationError as error:
            raise error
        except Exception as e:
            raise APIException({"error": str(e)})
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def patch(self, request: Request, pk: int) -> Response:
        """
        Patch method to update an existing user profile.

        Args:
            request: The HTTP request object.
            pk: The primary key of the user profile to be updated.

        Returns:
            Response: The HTTP response object containing the updated user profile data.
        """
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
        """
        Delete method to delete an existing user profile.

        Args:
            request: The HTTP request object.
            pk: The primary key of the user profile to be deleted.

        Returns:
            Response: The HTTP response object indicating successful deletion.
        """
        try:
            user = get_object_or_404(User, pk=pk)
            user.delete()
        except Exception as e:
            raise APIException({"error": str(e)})

        return Response(status=status.HTTP_204_NO_CONTENT)


class StreamSentencesView(View):
    """
    View for streaming sentences.
    """

    def get(self, request):
        """
        Get method to stream sentences.

        Args:
            request: The HTTP request object.

        Returns:
            StreamingHttpResponse: The streaming HTTP response object.
        """

        def event_stream():
            """
            Generator function to yield sentences for streaming.

            Yields:
                str: A sentence for streaming.
            """
            for sentence in self.generate_sentences():
                yield f"data: {sentence}\n\n"

        response = StreamingHttpResponse(
            event_stream(), content_type="text/event-stream"
        )
        response["Cache-Control"] = "no-cache"
        return response

    def generate_sentences(
        self,
    ):
        """
        Method to generate sentences for streaming.

        Returns:
            List[str]: A list of sentences for streaming.
        """
        sentences = [
            "This is the first sentence.",
            "Here comes the second sentence.",
            "And the third one follows.",
            "Next comes the fourth sentence.",
            "Fifth sentence, coming through!",
        ]

        for sentence in sentences:
            yield sentence
            time.sleep(1)
