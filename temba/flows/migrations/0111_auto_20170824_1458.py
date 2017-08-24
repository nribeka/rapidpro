# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-24 14:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('channels', '0076_channel_tps'),
        ('contacts', '0067_auto_20170808_1852'),
        ('orgs', '0036_ensure_anon_user_exists'),
        ('flows', '0110_auto_20170731_1046'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlowSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('connection', models.OneToOneField(help_text='The channel connection used for flow sessions over IVR or USSD', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='session', to='channels.ChannelSession')),
                ('contact', models.ForeignKey(help_text='The contact that this session is with', on_delete=django.db.models.deletion.CASCADE, to='contacts.Contact')),
                ('org', models.ForeignKey(help_text='The organization this session belongs to', on_delete=django.db.models.deletion.CASCADE, to='orgs.Org')),
            ],
        ),
        migrations.RenameField(
            model_name='flowrun',
            old_name='session',
            new_name='connection',
        ),
        # the next 2 operations drop and re-add the index on the renamed flowrun.connection column so the
        # index name won't conflict with the new session column being added below
        migrations.AlterField(
            model_name='flowrun',
            name='connection',
            field=models.ForeignKey(blank=True, db_index=False,
                                    help_text='The session that handled this flow run, only for voice flows', null=True,
                                    on_delete=django.db.models.deletion.CASCADE, related_name='runs',
                                    to='channels.ChannelSession'),
        ),
        migrations.AlterField(
            model_name='flowrun',
            name='connection',
            field=models.ForeignKey(blank=True,
                                    help_text='The session that handled this flow run, only for voice flows', null=True,
                                    on_delete=django.db.models.deletion.CASCADE, related_name='runs',
                                    to='channels.ChannelSession'),
        ),
        migrations.AddField(
            model_name='flowrun',
            name='session',
            field=models.ForeignKey(help_text='The session that handled this flow run, only for voice flows', null=True,
                                    on_delete=django.db.models.deletion.CASCADE, related_name='runs',
                                    to='flows.FlowSession'),
        ),
    ]
