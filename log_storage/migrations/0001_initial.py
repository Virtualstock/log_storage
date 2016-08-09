# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Log'
        db.create_table(u'log_storage_log', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('save_file', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('db_log_data', self.gf('django.db.models.fields.TextField')()),
            ('filename', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'log_storage', ['Log'])


    def backwards(self, orm):
        # Deleting model 'Log'
        db.delete_table(u'log_storage_log')


    models = {
        u'log_storage.log': {
            'Meta': {'object_name': 'Log'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'db_log_data': ('django.db.models.fields.TextField', [], {}),
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'save_file': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        }
    }

    complete_apps = ['log_storage']