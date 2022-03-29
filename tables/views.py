from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from tables.models import Table, TableSnapshot
from django.core import serializers


def get_all_tables(request: HttpRequest) -> JsonResponse:
    response = {
        "tables": []
    }

    tables = Table.objects.all().values()

    return JsonResponse(list(tables), safe=False)
