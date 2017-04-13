# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-10 07:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flows', '0096_populate_flownodecount'),
        ('api', '0013_webhookresult_request_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='webhookevent',
            name='run',
            field=models.ForeignKey(help_text='The flow run that triggered this event', null=True, on_delete=django.db.models.deletion.CASCADE, to='flows.FlowRun'),
        ),
        migrations.AlterField(
            model_name='webhookevent',
            name='event',
            field=models.CharField(choices=[('mo_sms', 'Incoming SMS Message'), ('mt_sent', 'Outgoing SMS Sent'), ('mt_dlvd', 'Outgoing SMS Delivered to Recipient'), ('mt_fail', 'Outgoing SMS Failed to be Delivered to Recipient'), ('mt_call', 'Outgoing Call'), ('mt_miss', 'Missed Outgoing Call'), ('mo_call', 'Incoming Call'), ('mo_miss', 'Missed Incoming Call'), ('alarm', 'Channel Alarm'), ('flow', 'Flow Step Reached'), ('categorize', 'Flow Categorization')], help_text='The event type for this event', max_length=16),
        ),
        migrations.AlterField(
            model_name='webhookresult',
            name='event',
            field=models.ForeignKey(help_text='The event that this result is tied to',
                                    on_delete=django.db.models.deletion.CASCADE, related_name='results',
                                    to='api.WebHookEvent'),
        ),
    ]