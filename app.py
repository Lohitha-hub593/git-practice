HEAD
created today for practice
python3
=======
created today for practice 
=======
created today for practice python2

created by another dev
>>>>>>> 021b004304a8fbc34ffeeca1d9b1fec0bde7f1c5
import boto6
client = boto3.client('ec2')
response = client.run_instances(
    ImageId ='ami-0453ec754f44f9a4a',
    InstanceType = 't2.micro',
    KeyName='pem',
    MaxCount=1,
    MinCount=1,
