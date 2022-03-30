from django.http import HttpRequest, JsonResponse
from tables.models import Table, TableSnapshot
import json
import datetime


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


def create_table_snapshot(request: HttpRequest):
    data_string = request.body

    try:
        data_dict = json.loads(data_string.decode("utf-8"))
    except json.JSONDecodeError:
        return JsonResponse({"success": False})

    # TODO: Validate whether the requester is allowed to create an entry

    snapshot = TableSnapshot()

    try:
        snapshot.table_id = data_dict["table_id"]
        snapshot.timestamp = datetime.datetime.fromtimestamp(
            data_dict["timestamp"])
        snapshot.energy_production = data_dict["energy_production"]
        snapshot.battery_charge = data_dict["battery_charge"]
        snapshot.port_usage = data_dict["port_usage"]

        snapshot.save()

        return JsonResponse({"success": True})
    except KeyError:
        # Some field was missing from the request
        return JsonResponse({"success": False})
