import sys
import boto3

ssm = boto3.client("ssm")


def get_ssm_secret(parameter_name):
    return ssm.get_parameter(
        Name="/demo/secret/parameter",
        WithDecryption=True
    )


if __name__ == "__main__":
    name = sys.argv[1]

    secret = get_ssm_secret(name)

    print("Secret is")
    print(secret.get("Parameter").get("Value"))

    print("=====")

    print("Parameter details")
    print(secret)
