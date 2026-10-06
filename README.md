<img width="1882" height="907" alt="Screenshot 2026-10-06 185032" src="https://github.com/user-attachments/assets/8297f7a0-111c-430e-be8a-c240c42f253c" />
<img width="1887" height="911" alt="Screenshot 2026-10-06 185006" src="https://github.com/user-attachments/assets/abe128de-134d-4d9b-8de9-e0b625f3abff" />
<img width="1892" height="916" alt="Screenshot 2026-10-06 184906" src="https://github.com/user-attachments/assets/8d7287b5-78b6-4747-8d64-f089bd6b0536" />



# Automated Static Website Hosting Using AWS SDK



## 📌 Project Overview



This project automates the deployment of a static website to Amazon S3 using Python and Boto3 (AWS SDK for Python).



Instead of manually creating an S3 bucket, uploading website files, configuring static website hosting, and applying public access settings through the AWS Console, this project automates the complete process using a Python script.



## 🎯 Objective



The main objective of this project is to automate static website deployment on Amazon S3 using Python and Boto3.



### Deployment Flow



```text

Local Website

&#x20;    ↓

Python deploy.py

&#x20;    ↓

Boto3 (AWS SDK for Python)

&#x20;    ↓

Amazon S3

&#x20;    ↓

Upload index.html

&#x20;    ↓

Static Website Hosting

&#x20;    ↓

Public Access Configuration

&#x20;    ↓

Live Website



🛠️ Technologies Used

Python

Boto3

Amazon S3

AWS CLI

HTML

CSS

JavaScript

Git

GitHub

☁️ AWS Services Used

Amazon S3



Amazon S3 is used to:



Store the website files

Host the static website

Provide public access to the website

📂 Project Structure

aws-static-website-sdk/

│

├── .gitignore

├── README.md

├── deploy.py

│

└── website/

&#x20;   └── index.html

⚙️ How It Works

The deploy.py script performs the following operations:



Checks whether the S3 bucket exists.

Creates the bucket if it does not exist.

Uploads website/index.html to S3.

Enables S3 static website hosting.

Configures public access settings.

Applies a public-read bucket policy.

Generates and displays the website URL.

🚀 How to Run

1\. Install Python



Make sure Python is installed:

python --version



2\. Install Boto3

pip install boto3



3\. Configure AWS CLI



Configure your AWS credentials:

aws configure



Enter:

AWS Access Key ID

AWS Secret Access Key

Default region name: ap-south-1

Default output format: json



4\. Verify AWS Credentials

aws sts get-caller-identity



5\. Run the Deployment Script

From the project directory:

python deploy.py

The script automatically deploys the website to Amazon S3.



🌐 Website URL



After successful deployment, the script displays the S3 website URL.

Example:

http://your-bucket-name.s3-website.ap-south-1.amazonaws.com



🔄 Updating the Website

To update the website:



1:Modify:

website/index.html

2:Run:

python deploy.py

The updated index.html will be uploaded to S3.



🔐 Security Note

This project uses a public S3 bucket policy because the objective is to demonstrate direct S3 static website hosting.



For a production application, it is recommended to use:

Amazon CloudFront

&#x20;       ↓

S3 Bucket

with Origin Access Control (OAC), rather than making the S3 bucket publicly readable.



Never upload AWS access keys or secret credentials to GitHub.



📈 Benefits

Automates website deployment

Reduces manual AWS Console steps

Uses Python for AWS automation

Demonstrates practical Boto3 knowledge

Easy to update and redeploy

Useful for AWS Cloud Engineer portfolio



💡 Learning Outcomes

Through this project, I learned:



Amazon S3

Static website hosting

Python automation

Boto3

AWS CLI

S3 bucket policies

Public access configuration

Git and GitHub

AWS deployment automation

👨‍💻 Author

Aspiring Cloud Engineer



📄 License

This project is created for learning and educational purposes.



Save the file and close Notepad.



\### Then verify



Run:



```cmd

dir /a



You should now see:

.git

.gitignore

README.md

deploy.py

website




