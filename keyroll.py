import boto3
from datetime import datetime, timezone, timedelta

class iam_user:
	def __init__(self, user):
		self.user = user
		self.client = boto3.Session().client('iam')
		self.curr_keys = []
		self.new_access = ""
		self.new_secret = ""
		self.key_age = ""
		self.secret_id = ""

	def get_current(self):
		_response = self.client.list_access_keys(UserName=self.user)
		for item in _response["AccessKeyMetadata"]:
			self.curr_keys.append(item["AccessKeyId"])

	def request_new(self):
		_response = self.client.create_access_key(UserName=self.user)
		_item = _response['AccessKey']
		self.new_access = _item["AccessKeyId"]
		self.new_secret = _item["SecretAccessKey"]

	def expire_current(self):
		for key in self.curr_keys:
			self.client.update_access_key(AccessKeyId=key, Status="Inactive", UserName=self.user)

	def delete_current(self):
		for key in self.curr_keys:
			self.client.delete_access_key(UserName=self.user, AccessKeyId=key)

	def get_key_age(self):
		_response = self.client.list_access_keys(UserName=self.user)
		for item in _response["AccessKeyMetadata"]:
			self.key_age = item["CreateDate"]

	def get_secret_id(self):
		_response = self.client.list_user_tags(UserName=self.user)
		for tag in _response["Tags"]:
			if tag["Key"] == "rotating-secret-id":
				self.secret_id = tag["Value"]
	
	def rotate_keys(self):
		self.get_secret_id()
		self.get_current()
		self.request_new()
		self.expire_current()
		self.delete_current()
