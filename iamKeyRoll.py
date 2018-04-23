import boto3

user = "" # update accordingly
profile = "" # ^
existing_keys = [] # empty global initialization

client = boto3.Session(profile_name=profile).client('iam')

def list_previous (client, user, existing_keys): # list existing keys, add them to a list
	response = client.list_access_keys(UserName=user)
	for item in response["AccessKeyMetadata"]:
		existing_keys.append(item["AccessKeyId"])

def create_new (client, user): # create new keys
	creation = client.create_access_key(UserName=user)

def disable_previous (client, user, existing_keys): # set existing keys as inactive
	for key in existing_keys:
		client.update_access_key(AccessKeyId=key, Status="Inactive", UserName=user)

def delete_previous (client, user, existing_keys): # delete the old, inactive keys
	 for key in existing_keys:
	 	client.delete_access_key(UserName=user, AccessKeyId=key)

def main():
	list_previous(client, user, existing_keys)
	create_new(client, user)
	disable_previous(client, user, existing_keys)
	delete_previous(client, user, existing_keys)

main()