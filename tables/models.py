from django.db import models
from enum import Enum
from django.contrib.postgres.fields import ArrayField


class PortType(Enum):
    USB = "USB"
    QI = "Qi"


class Table(models.Model):
    """Static definition of a table"""

    # Displayable name
    name = models.CharField(null=False, max_length=50)

    # Geographic location
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

    timestamp = models.DateTimeField(null=False, auto_now_add=True,
                                     help_text="Timestamp of this snapshot")

    # TODO: What unit? W?
    energy_production = models.FloatField(null=False,
                                          help_text="Current energy production by the PV panel")

    # TODO: What unit? Percent?
    battery_charge = models.FloatField(null=False,
                                       help_text="Current battery charge")

    # TODO: What unit? W?
    port_usage = ArrayField(models.FloatField(null=False, help_text="Port usage"), null=False,
                            help_text="For mapping to port types, refer to the ports field of the corresponding table")
