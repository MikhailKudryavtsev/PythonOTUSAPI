pipeline {
    agent none 
    stages {
        stage('Test') {
            agent { dockerfile true }
            steps {
                sh 'pytest -v testing_api_dog.py'
            }
        }
    }
}
