pipeline { agent any
environment {
    PROJECT_ID = "your-project-id"
    REGION = "us-central1"
    REPOSITORY = "docker-repo"
    IMAGE_NAME = "login-app"
}

stages {

    stage('Checkout') {
        steps {
            checkout scm
        }
    }

    stage('Install Dependencies') {
        steps {
            sh 'pip install -r requirements.txt'
        }
    }

    stage('Build Docker Image') {
        steps {
            sh '''
            docker build -t ${IMAGE_NAME}:latest .
            '''
        }
    }

    stage('Security Scan') {
        steps {
            sh '''
            docker scout quickview ${IMAGE_NAME}:latest || true
            '''
        }
    }

    stage('Tag Image') {
        steps {
            sh '''
            docker tag ${IMAGE_NAME}:latest \
            ${REGION}-docker.pkg.dev/${PROJECT_ID}/${REPOSITORY}/${IMAGE_NAME}:latest
            '''
        }
    }

    stage('Push Image') {
        steps {
            sh '''
            docker push \
            ${REGION}-docker.pkg.dev/${PROJECT_ID}/${REPOSITORY}/${IMAGE_NAME}:latest
            '''
        }
    }

    stage('Deploy Cloud Run') {
        steps {
            sh '''
            gcloud run deploy ${IMAGE_NAME} \
            --image ${REGION}-docker.pkg.dev/${PROJECT_ID}/${REPOSITORY}/${IMAGE_NAME}:latest \
            --platform managed \
            --region ${REGION} \
            --allow-unauthenticated
            '''
        }
    }
}

post {
    success {
        echo 'Deployment Successful'
    }

    failure {
        echo 'Pipeline Failed'
    }
}

}
