pipeline {
<<<<<<< HEAD
    agent any
  
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t login-app .'
            }
        }

        stage('Test') {
            steps {
                echo 'Build Successful'
            }
        }
    }
=======
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t login-app .'
            }
        }

        stage('Test') {
            steps {
                echo 'Build Successful'
            }
        }
    }
>>>>>>> aa837a3 (Fix Jenkinsfile)
}
