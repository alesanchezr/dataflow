import os, requests, sys, pytz, datetime
from django.utils import timezone
from django.db.models.expressions import RawSQL
from django.core.management.base import BaseCommand, CommandError
from django.db import models as DM
from django.db.models import Q, F
from ...models import PipelineExecution
from ...tasks import async_run_pipeline


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('pipeline', type=str)

    def handle(self, *args, **options):
        filter_by = sys.argv[2]
        if filter_by == None:
            raise Exception('Invalidad pipeline slug')
        if filter_by == 'all':
            executions = PipelineExecution.objects.all()
            if len(executions) == 0:
                return print('No matching records found in the database.')
            else:
                executions.delete()
                return print('Records deleted successfully')
        if filter_by != None:
            executions = PipelineExecution.objects.filter(pipeline__slug=filter_by).all()
            if len(executions) == 0:
                return print('No matching records found in the database.')
            else:
                executions.delete()
                return print('Records deleted successfully')
        

