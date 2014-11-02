import django_tables2 as tables
from guitar_app import models
from django_tables2.utils import A

class GuitarTable(tables.Table):
    name = tables.LinkColumn('guitar_detail', args=[A('pk')])
    selection = tables.CheckBoxColumn(accessor='pk', attrs={"th__input": {"onclick": "toggle(this)"}}, orderable=False)
    class Meta:
        model = models.Guitar
        attrs = {"class": "paleblue"}

class HistoryTable(tables.Table):
    class Meta:
        model = models.History
        attrs = {"class": "paleblue"}

class StatisticsTable(tables.Table):
    id = tables.Column()
    name = tables.Column()
    count = tables.Column()
    class Meta:
        attrs = {"class": "paleblue"}