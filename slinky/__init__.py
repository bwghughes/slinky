# -*- coding: utf-8 -*-

__author__ = 'Ben Hughes'
__email__ = 'bwghughes@gmail.com'
__version__ = '0.1.0'

import os
import click

from .slinky import create_temp_s3_link

@click.command()
@click.argument('filename')
@click.option('--seconds-available', default=3600, type=int)
@click.option('--bucket-name', default='slinky')
@click.option('--aws-key')
@click.option('--aws-secret')
def slinky(filename, seconds_available, bucket_name, aws_key, aws_secret):
    """Simple program that creates an temp S3 link."""
    if not os.environ.get('AWS_ACCESS_KEY_ID') and os.environ.get('AWS_SECRET_ACCESS_KEY'):
    	print 'Need to set environment variables for AWS access and create a slinky bucket.'
    	exit()
    
    print create_temp_s3_link(filename, seconds_available, bucket_name)

if __name__ == '__main__':
    print slinky()