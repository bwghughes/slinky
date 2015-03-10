# -*- coding: utf-8 -*-
import boto

def create_temp_s3_link(filename, seconds_available, bucket_name):
	connection = boto.connect_s3()
	bucket = connection.get_bucket(bucket_name)
	key = bucket.new_key(filename)
	key.set_contents_from_filename(filename)
	temp_url = key.generate_url(expires_in=seconds_available, query_auth=True)
	return temp_url