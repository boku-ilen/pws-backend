from django.shortcuts import render
from django.http import HttpRequest, JsonResponse


def get_all_tables(request: HttpRequest) -> JsonResponse:
    return JsonResponse({"test": True})
