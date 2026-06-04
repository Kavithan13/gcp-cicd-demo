pipeline {
    agent any

    environment {
        PROJECT_ID = "avian-outrider-497411-v9"
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

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME}:latest ."
            }
        }

        // ✅ NEW STAGE: Vulnerability Scan using Trivy
        stage('Vulnerability Scan') {
            steps {
                sh """
                # Install trivy if not already installed
                if ! command -v trivy &> /dev/null
                then
                    echo "Installing Trivy..."
                    curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sh
                fi

                # Run scan
                ./bin/trivy image ${IMAGE_NAME}:latest --severity CRITICAL,HIGH --exit-code 1 --no-progress
                """
            }
        }

        stage('Authenticate GCP') {
            steps {
                withCredentials([file(credentialsId: 'gcp-sa-key', variable: 'GOOGLE_KEY')]) {
                    sh """
                    gcloud auth activate-service-account --key-file=$GOOGLE_KEY
                    gcloud config set project ${PROJECT_ID}
                    """
                }
            }
        }

        stage('Push Image') {
            steps {
                sh """
                gcloud auth configure-docker ${REGION}-docker.pkg.dev --quiet

                docker tag ${IMAGE_NAME}:latest \
                ${REGION}-docker.pkg.dev/${PROJECT_ID}/${REPOSITORY}/${IMAGE_NAME}:latest

                docker push \
                ${REGION}-docker.pkg.dev/${PROJECT_ID}/${REPOSITORY}/${IMAGE_NAME}:latest
                """
            }
        }

        stage('Deploy Cloud Run') {
            steps {
                sh """
                gcloud run deploy ${IMAGE_NAME} \
                --image ${REGION}-docker.pkg.dev/${PROJECT_ID}/${REPOSITORY}/${IMAGE_NAME}:latest \
                --platform managed \
                --region ${REGION} \
                --allow-unauthenticated
                """
            }
        }
    }
}
