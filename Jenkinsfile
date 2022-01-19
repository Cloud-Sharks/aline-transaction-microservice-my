pipeline{

    agent any

    environment{
        //TODO: set env vars
        COMMIT_HASH = "${sh(script: 'git rev-parse --short HEAD', returnStdout: true).trim()}"
        AWS_ID = credentials('AWS_ID')
        SERVICE_NAME = 'transaction-ms'
        REGION = 'us-west-1'
        APP_NAME = 'alinefinancialmy'
        APP_ENV = 'dev'
        ORGANIZATION = 'Aline-Financial-MY'
        PROJECT_NAME = 'aline-transaction-microservice-my'
    }

    stages{
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
                sh'aws ecr get-login-password --region ${REGION} | docker login --username AWS --password-stdin --password-stdin ${AWS_ID}.dkr.ecr.${REGION}.amazonaws.com'
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