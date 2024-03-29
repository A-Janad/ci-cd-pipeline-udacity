# Overview

In this project, you will build a Github repository from scratch and create a scaffolding that will assist you in performing both Continuous Integration and Continuous Delivery. You'll use Github Actions along with a Makefile, requirements.txt and application code to perform an initial lint, test, and install cycle. Next, you'll integrate this project with Azure Pipelines to enable Continuous Delivery to Azure App Service.

## Project Plan

It is critical to have an effective project plan and task tracking, In this section you find:
* A [trello](https://trello.com/b/7QrYdgzR/udacity-building-a-ci-cd-pipeline) board for the project
* A [Spreadsheet ](https://github.com/A-Janad/ci-cd-pipeline-udacity/files/11184345/CI-CD_yearly_quarterly_project_plan.xlsx) that includes the original and final project plan

## Instructions

![cicd1](https://user-images.githubusercontent.com/126161000/230734652-4371e78b-26b3-4e77-8096-59871ee96258.png)


The diagram shows the sequence of steps in the construction of the project. The code is pushed to a remote repository provider, in this case GitHub, which triggers the pipeline to be run on a "push" event. GitHub actions is used as our build server. One of the things that makes GitHub Actions extremely convenient is that it is integrated with GitHub, which means that we can have it run builds automatically whenever we commit code to our GitHub repo. In the Continuous Delivery step, the repository on GitHub is connected with Azure Pipelines(a cloud-native build server) to generate the build package after a successful build. This pipeline should connect to a pre-defined Azure webapp and deploy and update the code there. Confirmation that the deployment worked successfully is done by making a POST request, by passing input parameters in JSON and receiving a prediction response. The shell script is responsible for sending some input data to the application via the appropriate port. Each numerical value represents some feature that is important for determining the price of a house in Boston. The source code is responsible for passing that data through a trained, machine learning model, and giving back a predicted value for the house price.

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

Passing GitHub Actions:

[![Python application test with Github Actions](https://github.com/A-Janad/ci-cd-pipeline-udacity/actions/workflows/python-app.yml/badge.svg)](https://github.com/A-Janad/ci-cd-pipeline-udacity/actions/workflows/python-app.yml)

## Deploy the app to an Azure App Service
Now is time to deploy the app to an azure app service...

Create an App Service in Azure. In this example the App Service is called `flask-webapp-udacity` and the resource group is called `ci-cd-rg`.

```bash
(.myrepo) aaaljanad [ ~/ci-cd-pipeline-udacity ]$ az webapp up --name flask-webapp-udacity -g ci-cd-rg -l westeurope --sku B2 
``` 

<img width="918" alt="Screenshot 2023-04-09 005708" src="https://user-images.githubusercontent.com/126161000/230745896-26ad4820-eb8e-4e64-ae33-63a57a508bcf.png">

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

Install locust 

```bash
(.myrepo) aaaljanad [ ~/ci-cd-pipeline-udacity ]$ pip install locust 
```

and then run locust:

```bash
(.myrepo) aaaljanad [ ~/ci-cd-pipeline-udacity ]$ locust -f locustfile.py --headless -u 10 -r 3 -t 10s
```

This is the output after adding your web app name as the host variable 

<img width="919" alt="Screenshot 2023-04-08 185647" src="https://user-images.githubusercontent.com/126161000/230733707-2f786d80-ad57-48f0-9326-05669634e331.png">

## Enhancements
In the future, the project can be configured to work with gitflow, so if you commit to a particular branch, the code can continue to be deployed in the corresponding environment (Development, QA, Staging or production).

## Demo
This is the youtube demo of all project steps: [Demo video](https://www.youtube.com/watch?v=L391HpZXs7g)


