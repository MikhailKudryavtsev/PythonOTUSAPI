pipeline {
    agent none 
    stages {
        stage('Test') {
            agent { dockerfile true }
            steps {
                sh 'docker run my_tests'
            }
        }
    }
}
