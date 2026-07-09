pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Building application...'
                sh 'which python3'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'which python3'
            }
        }
    }
}

          
