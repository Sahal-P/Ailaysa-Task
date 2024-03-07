from django.http import HttpRequest
from rest_framework import serializers
from rest_framework.request import Request

def get_limit_skip(request: Request) -> str:
    limit = int(request.query_params.get("limit", 10))
    skip = (int(request.query_params.get("page", 1)) - 1) * limit
    
    return limit, skip
