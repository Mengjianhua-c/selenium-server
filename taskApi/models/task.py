"""
CREAT: 2017/12/19
AUTHOR:　HEHAHUTU
"""
from django.db import models
from rest_framework import serializers


class Task(models.Model):
    STATUS_CHOSE = (
        ('waiting', '等待中'),
        ('running', '执行中'),
        ('finished', '结束'),
    )
    ENV_CHOSE = (
        ('test', '测试服务器'),
        ('prod', '正式服务器'),
    )
    name = models.CharField('task name', max_length=100)
    status = models.CharField('status', max_length=20, choices=STATUS_CHOSE, default='waiting')
    task_env = models.CharField('task env', max_length=20, choices=ENV_CHOSE, default='test')
    create_time = models.DateTimeField('create time', auto_now_add=True)
    start_time = models.DateTimeField('task stat time', auto_now=True)
    end_time = models.DateTimeField('task end time', auto_now=True)
    task_report = models.TextField('task report')

    class Meta:
        ordering = ('-create_time',)


class TaskSerializers(serializers.Serializer):
    name = serializers.CharField()
    status = serializers.ChoiceField(default='waiting', choices=Task.STATUS_CHOSE)
    task_env = serializers.ChoiceField(default='test', choices=Task.ENV_CHOSE)
    create_time = serializers.DateTimeField(read_only=True)
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'name', 'task_env', 'status', 'create_time')

    def create(self, validated_data):
        return Task.objects.create(**validated_data)