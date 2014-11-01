from __future__ import unicode_literals

from django.db import models


class Produser(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True)
    rating = models.IntegerField(blank=True, null=True)
    guitar = models.IntegerField(blank=True, null=True)
    bridge = models.IntegerField(blank=True, null=True)
    pickups = models.IntegerField(blank=True, null=True)
    info = models.TextField(blank=True)
    def __unicode__(self):
        return self.name
    class Meta:
        managed = True
        db_table = 'produser'

class Body(models.Model):
    id = models.IntegerField(primary_key=True)
    material = models.CharField(max_length=45, blank=True)
    color = models.CharField(max_length=45, blank=True)
    type = models.CharField(max_length=45, blank=True)
    form = models.CharField(max_length=45, blank=True)
    def __unicode__(self):
        return self.material
    class Meta:
        managed = True
        db_table = 'body'

class Bridge(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True)
    material = models.CharField(max_length=45, blank=True)
    color = models.CharField(max_length=45, blank=True)
    produser = models.ForeignKey('Produser', related_name='bridge_produser', blank=True, null=True)
    def __unicode__(self):
        return self.name
    class Meta:
        managed = True
        db_table = 'bridge'

class Guitar(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True)
    string_amount = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    neck_material = models.CharField(max_length=45, blank=True)
    fretboard_material = models.CharField(db_column='Fretboard_material', max_length=45, blank=True) # Field name made lowercase.
    pick_guard = models.NullBooleanField(db_column='Pick_guard', blank=True, null=True) # Field name made lowercase.
    type = models.ForeignKey('GuitarType', db_column='Type_id', blank=True, null=True) # Field name made lowercase.
    body = models.ForeignKey(Body, db_column='Body_id', blank=True, null=True) # Field name made lowercase.
    bridge = models.ForeignKey(Bridge, db_column='Bridge_id', blank=True, null=True) # Field name made lowercase.
    pickups = models.ForeignKey('Pickup', db_column='Pickups_id', blank=True, null=True) # Field name made lowercase.
    guitar_produser = models.ForeignKey('Produser', related_name='guitar_produser', db_column='Guitar_produser_id', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'guitar'

class GuitarType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True)
    def __unicode__(self):
        return self.name
    class Meta:
        managed = True
        db_table = 'guitar_types'

class Pickup(models.Model):
    id = models.IntegerField(primary_key=True)
    produser = models.ForeignKey('Produser', related_name='pickups_produser', blank=True, null=True)
    type = models.CharField(max_length=45, blank=True)
    set_type = models.CharField(max_length=45, blank=True)
    def __unicode__(self):
        return self.set_type
    class Meta:
        managed = True
        db_table = 'pickups'

class History(models.Model):
    id = models.IntegerField(primary_key=True)
    trigger_action = models.CharField(max_length=45, blank=True)
    guitar_id = models.IntegerField(blank=True, null=True)
    action_time = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'history'

class Variables(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True)
    short_name = models.CharField(max_length=20, blank=True)
    value = models.NullBooleanField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'variables'