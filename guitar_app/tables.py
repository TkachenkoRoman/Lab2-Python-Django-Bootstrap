import django_tables2 as tables
from guitar_app import models

class GuitarTable(tables.Table):
    selection = tables.CheckBoxColumn(accessor='pk', attrs={"th__input": {"onclick": "toggle(this)"}}, orderable=False)
    class Meta:
        model = models.Guitar
        attrs = {"class": "paleblue"}