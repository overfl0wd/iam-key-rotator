import boto3

user = "" # update accordingly
profile = "" # ^

client = boto3.Session(profile_name=profile).client('iam') # connection initialization

def list_previous (client, user): # access existing key, add to global variable
	global existing_key
	response = client.list_access_keys(UserName=user)
	for item in response["AccessKeyMetadata"]:
		existing_key = item["AccessKeyId"]

def create_new (client, user): # create new key
	creation = client.create_access_key(UserName=user)

def disable_previous (client, user, existing_key): # set old key as inactive
	client.update_access_key(AccessKeyId=existing_key, Status="Inactive", UserName=user)

def delete_previous (client, user, existing_key): # delete the old, inactive key
	client.delete_access_key(UserName=user, AccessKeyId=existing_key)

def main():
	list_previous(client, user)
	create_new(client, user)
	disable_previous(client, user, existing_key)
	delete_previous(client, user, existing_key)

main()