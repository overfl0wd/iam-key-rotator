# IAM Key Rolling
The focus of this project is on the programmatic "rolling" of AWS IAM access keys. This involves creating new keys to replace previous ones, on a regular basis. Changing the keys will limit exposure, and storing them in [AWS Secrets Manager](https://aws.amazon.com/blogs/aws/aws-secrets-manager-store-distribute-and-rotate-credentials-securely/) will allow them to be programmatically queried and used as-needed, rather than stored locally in clear.

At this stage, this script is intended to be a framework for this process. Any other requirements (functionality validation) are going to be use-case-specific, thus are not covered here. There are just too many services and permissions to feasibly cover every scenario. The problem it will solve is that users in my organization store their access keys locally for long periods of time. 

This script follows the procedure suggested in the [AWS Security Blog.](https://aws.amazon.com/blogs/security/how-to-rotate-access-keys-for-iam-users/)

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
