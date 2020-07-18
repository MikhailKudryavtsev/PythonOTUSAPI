pipeline {
    agent none 
    stages {
        stage('Test') {
            agent { docker 'maven:3-alpine' } 
        }
    }
}
