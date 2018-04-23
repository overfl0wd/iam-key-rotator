import boto3

user = "" # update accordingly
profile = "" # ^
secret = "" # ^

iam_client = boto3.Session(profile_name=profile).client('iam') # connection initialization
sm_client = boto3.Session(profile_name=profile).client('secretsmanager') # ^

def list_previous (client, user): # access existing key, add to global variable
	global existing_key
	response = client.list_access_keys(UserName=user)
	for item in response["AccessKeyMetadata"]:
		existing_key = item["AccessKeyId"]

def create_new (client, user): # create new key, add to global variables
	response = client.create_access_key(UserName=user)
	global access_key, secret_key
	for item in response["AccessKey"]:
		access_key = response["AccessKey"]["AccessKeyId"]
		secret_key = response["AccessKey"]["SecretAccessKey"]

def post_new (client, user, access_key, secret_key): # update secret with new key pair
	client.update_secret(SecretId=secret,SecretString='{"access_key": "%s", "secret_key": "%s"}' % (access_key, secret_key))

def disable_previous (client, user, existing_key): # set old key as inactive
	client.update_access_key(AccessKeyId=existing_key, Status="Inactive", UserName=user)

def delete_previous (client, user, existing_key): # delete the old, inactive key
	 client.delete_access_key(UserName=user, AccessKeyId=existing_key)

def main():
	list_previous(iam_client, user)
	create_new(iam_client, user)
	post_new(sm_client, user, access_key, secret_key)
	disable_previous(iam_client, user, existing_key)
	delete_previous(iam_client, user, existing_key)

main()