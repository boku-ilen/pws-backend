from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from tables.models import Table, TableSnapshot
from django.core import serializers


def get_all_tables(request: HttpRequest) -> JsonResponse:
    """Returns a list with all tables' static data."""

    tables = Table.objects.all().values()

    return JsonResponse(list(tables), safe=False)


def get_latest_snapshot(request: HttpRequest, table_id: int) -> JsonResponse:
    """Returns the data in the latest snapshot available for the given table."""

    try:
        latest_table = TableSnapshot.objects.filter(
            table=table_id).values().latest("timestamp")
    except TableSnapshot.DoesNotExist:
        return JsonResponse({"success": False})

    return JsonResponse(latest_table, safe=False)
