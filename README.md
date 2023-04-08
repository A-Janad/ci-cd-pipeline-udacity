# Overview

In this project, you will build a Github repository from scratch and create a scaffolding that will assist you in performing both Continuous Integration and Continuous Delivery. You'll use Github Actions along with a Makefile, requirements.txt and application code to perform an initial lint, test, and install cycle. Next, you'll integrate this project with Azure Pipelines to enable Continuous Delivery to Azure App Service.

## Project Plan

It is critical to have an effective project plan and task tracking, In this section you find:
* A [trello](https://trello.com/b/7QrYdgzR/udacity-building-a-ci-cd-pipeline) board for the project
* A spreadsheet that includes the original and final project plan

## Instructions

<TODO:  
* Architectural Diagram (Shows how key parts of the system work)>

in Azure Cloud Shell, clone the repo:

```bash
git clone git@github.com:A-Janad/ci-cd-pipeline-udacity.git
```
<img width="793" alt="Screenshot 2023-04-07 183931" src="https://user-images.githubusercontent.com/126161000/230645445-f2147e78-e05c-449a-888d-5829da7966b1.png">

Change into the new directory:
```bash
aaaljanad [ ~ ]$ cd ci-cd-pipeline-udacity/
```

Create a virtual environment:
```bash
aaaljanad [ ~/ci-cd-pipeline-udacity ]$ python3 -m venv ~/.myrepo
```

Activate the virtual environment:
```bash
aaaljanad [ ~/ci-cd-pipeline-udacity ]$ source ~/.myrepo/bin/activate
```

Install dependencies in the virtual environment and run tests:

```bash
(.myrepo) aaaljanad [ ~/ci-cd-pipeline-udacity ]$ make all
```
<img width="917" alt="Screenshot 2023-04-07 190351" src="https://user-images.githubusercontent.com/126161000/230648496-e4d60487-265e-4459-9188-cbb9a68aede4.png">

Start the application in the local environment:
```bash
(.myrepo) aaaljanad [ ~/ci-cd-pipeline-udacity ]$ flask run
```
<img width="915" alt="Screenshot 2023-04-07 191204" src="https://user-images.githubusercontent.com/126161000/230649554-31850a3a-acaf-4858-ac13-c5ecc48bb46b.png">

Open a separate Cloud Shell and test that the app is working:
```bash
(.myrepo) aaaljanad [ ~/ci-cd-pipeline-udacity ]$ ./make_prediction.sh
``` 
<img width="915" alt="Screenshot 2023-04-07 191404" src="https://user-images.githubusercontent.com/126161000/230651196-a2ca14d5-a4a9-40d9-a13a-1eab26c8e49e.png">

## CI : Configure GitHub Actions
You will configure GitHub Actions to test your project upon change events in GitHub. This is a necessary step to perform Continuous Integration remotely.

From the top bar of GitHub click on 'Actions', then click on "set up a workflow yourself' and use the GitHub Actions template yaml file located in [.github/workflows/main.yml]

Once you create this workflow, it will run automatically to build code in Repo:

<img width="913" alt="Screenshot 2023-04-05 002534" src="https://user-images.githubusercontent.com/126161000/230685645-df0e7610-871a-42b1-9ba9-fea47cbc212c.png">

## Deploy the app to an Azure App Service
Now is time to deploy the app to an azure app service...

Create an App Service in Azure. In this example the App Service is called `flask-webapp-udacity` and the resource group is called `ci-cd-rg`.

```bash
(.myrepo) aaaljanad [ ~/ci-cd-pipeline-udacity ]$ az webapp up --name flask-webapp-udacity -g ci-cd-rg -l westeurope --sku B2 
``` 
Next, create the pipeline in Azure DevOps. More information on this process can be found here. The basic steps to set up the pipeline are:

* Go to https://dev.azure.com and sign in.
* Create a new private project.
* Under Project Settings create a new service connection to Azure Resource Manager, scoped to your subscription and resource group.
* Create a new pipeline linked to your GitHub repo.

Screenshot of the App Service in Azure:
<img width="918" alt="Screenshot 2023-04-08 002633" src="https://user-images.githubusercontent.com/126161000/230686417-78534c3f-1f4d-4a02-a820-9178256f7efb.png">

Screenshot of a successful run of the project in Azure Pipelines:

<img width="918" alt="Screenshot 2023-04-08 171621" src="https://user-images.githubusercontent.com/126161000/230729209-e31596ef-d500-4c6a-b8b8-de678199587c.png">

Now, we can test the app. For you case, edit the make_predict_azure_app.sh script with the DNS name of your app. Then run the script on the cloud shell:

```bash
(.myrepo) aaaljanad [ ~/ci-cd-pipeline-udacity ]$ ./make_predict_azure_app.sh 
```

you should see the following output:

<img width="914" alt="Screenshot 2023-04-08 172331" src="https://user-images.githubusercontent.com/126161000/230729390-012a0643-4f45-4a29-ac9d-7e3aff8ef107.png">


for testing the deployed webapp, a new text is added at the end of page title (`from Azure`)You can also visit the URL of the App Service via the browser and you should see the following page:

<img width="960" alt="Screenshot 2023-04-08 171245" src="https://user-images.githubusercontent.com/126161000/230729718-31be1ce5-9ed6-4e89-af9b-7dab37ecf414.png">

* Output of streamed log files from deployed application

```bash
(.myrepo) aaaljanad [ ~/ci-cd-pipeline-udacity ]$ az webapp log tail -g ci-cd-rg --name flask-webapp-udacity
```

<img width="916" alt="Screenshot 2023-04-08 173327" src="https://user-images.githubusercontent.com/126161000/230729877-3bd04d08-7713-4db4-90cc-dd783576eb08.png">
> 

## Load Test
We can use locust to do a load test against our application. In this example we will do a load test against the app running in azure rather than locally.

Install locust and then run locust:



Open a browser and go to http://localhost:8089. Enter the total number of users to simulate, spawn rate, set the host to https://jose-flaskpipelines.azurewebsites.net/, and click Start Swarming:


## Demo 

<TODO: Add link Screencast on YouTube>


