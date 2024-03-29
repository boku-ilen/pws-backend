from django.db import models
from enum import Enum
from django.contrib.postgres.fields import ArrayField


class PortType(Enum):
    USB = "USB"
    QI = "Qi"


class Table(models.Model):
    """Static definition of a table"""

    name = models.CharField(null=False, max_length=50,
                            help_text="Displayable name")

    location_lat = models.FloatField(null=False,
                                     help_text="Latitude of the table's geographic location")
    location_lon = models.FloatField(null=False,
                                     help_text="Longitude of the table's geographic location")

    ports = ArrayField(models.CharField(
        max_length=5,
        choices=[(tag, tag.value) for tag in PortType]
    ), null=False, help_text="Port types")

    # TODO: Max energy production and battery charge? Or do we want to store that in timestamps too?


class TableSnapshot(models.Model):
    """Snapshot of the table's battery, PV, and port usage at a given timestamp"""

    table = models.ForeignKey(Table, on_delete=models.PROTECT,
                              help_text="Table which this snapshot refers to")

    timestamp = models.DateTimeField(null=False,
                                     help_text="Timestamp of this snapshot")

    energy_production = models.FloatField(null=False,
                                          help_text="Current energy production by the PV panel in mA")

    battery_charge = models.FloatField(null=False,
                                       help_text="Current battery charge (expressed as battery voltage)")

    temperature = models.FloatField(null=True, help_text="Temperature in °C")

    port_usage = ArrayField(models.FloatField(null=False, help_text="Power draw at the USB ports in mA"), null=False,
                            help_text="For mapping to port types, refer to the ports field of the corresponding table")

    port_voltage = ArrayField(models.FloatField(null=False, help_text="Voltage at the USB ports"), null=False,
                            help_text="For mapping to port types, refer to the ports field of the corresponding table")
