import boto3,ast,subprocess

from subprocess import PIPE
def main():
        process=subprocess.Popen(["aws","sts","assume-role","--role-arn","arn:aws:iam::712733279313:role/ec2-role","--role-session-name","get-creds"],stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        stdout=stdout.decode()
        stdout=ast.literal_eval(stdout)
        secret_key=stdout['Credentials'].get('SecretAccessKey')
        session_token=stdout['Credentials'].get('SessionToken')
        access_keyid=stdout['Credentials'].get('AccessKeyId')
        return secret_key,session_token,access_keyid
a,b,c=main()
return a,b,c
