from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from tables.models import Table, TableSnapshot
from django.core import serializers


def get_all_tables(request: HttpRequest) -> JsonResponse:
    tables = Table.objects.all().values()

    return JsonResponse(list(tables), safe=False)


def get_latest_snapshot(request: HttpRequest, table_id: int) -> JsonResponse:
    latest_table = TableSnapshot.objects.values().latest("timestamp")

    return JsonResponse(latest_table, safe=False)
