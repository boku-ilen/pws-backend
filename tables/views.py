from django.http import HttpRequest, JsonResponse
from tables.models import Table, TableSnapshot
from django.forms.models import model_to_dict
import json
import datetime


def get_all_tables(request: HttpRequest) -> JsonResponse:
    """Returns a list with all tables' static data."""

    tables = Table.objects.all().values()

    return JsonResponse(list(tables), safe=False)


def get_table(request: HttpRequest, table_id: int) -> JsonResponse:
    """Returns the static data of one specific table."""

    try:
        table = Table.objects.get(id=table_id)
        return JsonResponse(model_to_dict(table), safe=False)
    except Table.DoesNotExist:
        return JsonResponse({"success": False})


def get_latest_snapshot(request: HttpRequest, table_id: int) -> JsonResponse:
    """Returns the data in the latest snapshot available for the given table."""

    try:
        latest_table = TableSnapshot.objects.filter(
            table=table_id).values().latest("timestamp")

        return JsonResponse(latest_table, safe=False)
    except TableSnapshot.DoesNotExist:
        return JsonResponse({"success": False})


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
        snapshot.port_voltage = data_dict["port_voltage"]

        snapshot.save()

        return JsonResponse({"success": True})
    except KeyError:
        # Some field was missing from the request
        return JsonResponse({"success": False})
