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

The output should match the below:
* Successful deploy of the project in Azure Pipelines.  [Note the official documentation should be referred to and double checked as you setup CI/CD](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops).

* Running Azure App Service from Azure Pipelines automatic deployment

* Successful prediction from deployed flask app in Azure Cloud Shell.  [Use this file as a template for the deployed prediction](https://github.com/udacity/nd082-Azure-Cloud-DevOps-Starter-Code/blob/master/C2-AgileDevelopmentwithAzure/project/starter_files/flask-sklearn/make_predict_azure_app.sh).
The output should look similar to this:

```bash
udacity@Azure:~$ ./make_predict_azure_app.sh
Port: 443
{"prediction":[20.35373177134412]}
```

* Output of streamed log files from deployed application

> 

## Enhancements

<TODO: A short description of how to improve the project in the future>

## Demo 

<TODO: Add link Screencast on YouTube>


