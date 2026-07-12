pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'pip install --break-system-packages -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 -m pytest --maxfail=1 --disable-warnings -q'
            }
        }
    }
}

          
