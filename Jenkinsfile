pipeline{

    agent any

    environment{
        //TODO: set env vars
        COMMIT_HASH = "initial"
        SERVICE_NAME = 'transaction-ms'
        REGION = 'us-east-1'
        APP_NAME = 'my-transaction-microservice'
        APP_ENV = 'dev'
        ORGANIZATION = 'Aline-Financial-MY'
        PROJECT_NAME = 'aline-transaction-microservice-my'
    }

    stages{
        stage('Checkout'){
            steps{
                //TODO: get branch
                git branch: 'dev', url: 'https://github.com/markyates7748/aline-transaction-microservice-my.git'
            }
        }
        stage('Test'){
            steps{
                //TODO: run project tests
                sh'mvn clean test'
            }
        }
        stage('Package'){
            steps{
                //TODO: package project
                sh'mvn package -DskipTests'
            }
        }
        stage('Build Image'){
            steps{
                //TODO: build docker image
                sh'docker build . -t ${APP_NAME}/${APP_ENV}/${SERVICE_NAME}:${COMMIT_HASH}'
                sh'docker tag ${APP_NAME}/${APP_ENV}/${SERVICE_NAME}:${COMMIT_HASH} ${AWS_ID}.dkr.ecr.${REGION}.amazonaws.com/${APP_NAME}/${SERVICE_NAME}'
            }
        }
        stage('Push Image'){
            steps{
                //TODO: push image to cloud
                //sh'aws ecr get-login-password --region ${REGION} | docker login --username AWS --password-stdin --password-stdin ${AWS_ID}.dkr.ecr.${REGION}.amazonaws.com'
                sh'docker push ${AWS_ID}.dkr.ecr.${REGION}.amazonaws.com/${APP_NAME}/${SERVICE_NAME}'
            }
        }
    }

    post{
        always{
            //TODO: clean up
            sh'mvn clean'
            sh'docker image rm ${APP_NAME}/${APP_ENV}/${SERVICE_NAME}:${COMMIT_HASH}'
            sh'docker image rm ${AWS_ID}.dkr.ecr.${REGION}.amazonaws.com/${APP_NAME}/${APP_ENV}/${SERVICE_NAME}:${COMMIT_HASH}'
        }
    }

}