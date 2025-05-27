pipeline {
    agent any

    environment {
        SONARQUBE_SCANNER_HOME = tool 'SonarQubeScanner'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/mukesh-ma/web-app-CICD.git'
            }
        }

        stage('Code Quality - SonarQube') {
            steps {
                withSonarQubeEnv('MySonarQube') {
                    sh 'sonar-scanner'
                }
            }
        }

        stage('Test') {
            steps {
                sh 'pytest tests/'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t mukeshma/myapp:latest .'
            }
        }

        stage('Docker Push') {
            steps {
                withCredentials([string(credentialsId: 'docker-hub-pass', variable: 'DOCKER_PASSWORD')]) {
                    sh 'echo $DOCKER_PASSWORD | docker login -u mukeshma --password-stdin'
                    sh 'docker push mukeshma/myapp:latest'
                }
            }
        }

        stage('Deploy to AWS') {
            steps {
                sh './scripts/deploy.sh'
            }
        }
    }
}

