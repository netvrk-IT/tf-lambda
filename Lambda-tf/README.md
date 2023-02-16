This is a terraform script that allows you to provision a Lambda Resource in AWS. 

PREREQUISITES

Before you implement this, please make sure Terraform is installed on your local machine.
First, make sure you know what enviroment you're deploying your function to. 
Make sure the AWS Credentials are configured properly on your local machine. 

Replace the python script in this Folder with your Code Function. 
Make sure the variables.tf file matches the your deployment requirements. 

DEPLOYMENT

Terraform Init (This Initiates Terraform and generates you terraform state and lock files.)

Terraform Plan (This generates a plan of what terraform intends to do within AWS)

Terraform Apply (Apply this command when you are ready to deploy, and not before)

TROUBLESHOOTING

If there is an error with the deployment, Terraform generates and error massage that describes the reason for deployment failure