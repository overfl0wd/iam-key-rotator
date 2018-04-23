# IAM Key Rolling
The focus of this project is on the programmatic "rolling" of AWS IAM access keys. This involves creating new keys to replace previous ones, on a regular basis. This process shortens the period an access key is active and therefore reduces the business impact if one becomes compromised.

This script follows the procedure suggested in the [AWS Security Blog.](https://aws.amazon.com/blogs/security/how-to-rotate-access-keys-for-iam-users/)

Functionality has been added to work with the new [AWS Secrets Manager service](https://aws.amazon.com/blogs/aws/aws-secrets-manager-store-distribute-and-rotate-credentials-securely/), storing the newly created keys in a secret of your choosing. 

##### This script currently follows the following work flow:
- Get the existing key-pair for a user.
- Create a new key-pair.
- Store the new access and secret key in Secrets Manager.
- Disable the previous key-pair.
- Delete the previous key-pair.

#### Next Steps:
- Handle if the user has more than one key-pair to be rolled.
- Add error handling (ex: check for functionality with new key-pair before deleting previous)

## Requirements
- [Python3](https://www.python.org/downloads/)
- [AWS SDK for Python (Boto3)](https://aws.amazon.com/sdk-for-python/)
