
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out Python application'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv ci-venv
                    . ci-venv/bin/activate
                    pip install -r app/requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . ci-venv/bin/activate
                    python -m pytest tests/ -v
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build -t python-cicd-demo:${BUILD_NUMBER} .
                    docker tag python-cicd-demo:${BUILD_NUMBER} python-cicd-demo:latest
                '''
            }
        }
    }

    post {
        success {
            echo 'CI pipeline completed successfully!'
        }
        failure {
            echo 'CI pipeline failed. Check the build logs.'
        }
    }
}

