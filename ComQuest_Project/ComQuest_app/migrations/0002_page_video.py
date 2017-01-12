# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ComQuest_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='video',
            field=embed_video.fields.EmbedVideoField(default='1', blank=True),
            preserve_default=False,
        ),
    ]
