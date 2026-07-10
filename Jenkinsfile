pipeline {
    agent {
        docker { image 'python:3.10' }
    }

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
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'pytest --maxfail=1 --disable-warnings -q'
            }
        }
    }
}


          
