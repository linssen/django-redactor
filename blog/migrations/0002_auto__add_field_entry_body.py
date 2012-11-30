# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Entry.body'
        db.add_column('blog_entry', 'body',
                      self.gf('django.db.models.fields.TextField')(default=' '),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Entry.body'
        db.delete_column('blog_entry', 'body')


    models = {
        'blog.entry': {
            'Meta': {'object_name': 'Entry'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['blog']