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

        // ✅ Security Gate: Trivy Scan
        stage('Vulnerability Scan') {
            steps {
                sh """
                trivy image ${IMAGE_NAME}:latest \
                --severity CRITICAL,HIGH \
                --ignore-unfixed \
                --exit-code 1 \
                --no-progress
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

        stage('Tag & Push Image') {
            steps {
                script {
                    def BUILD_TAG = "${BUILD_NUMBER}"

                    sh """
                    gcloud auth configure-docker ${REGION}-docker.pkg.dev --quiet

                    # ✅ Tag with build number
                    docker tag ${IMAGE_NAME}:latest \
                    ${REGION}-docker.pkg.dev/${PROJECT_ID}/${REPOSITORY}/${IMAGE_NAME}:${BUILD_TAG}

                    # ✅ Also keep latest tag
                    docker tag ${IMAGE_NAME}:latest \
                    ${REGION}-docker.pkg.dev/${PROJECT_ID}/${REPOSITORY}/${IMAGE_NAME}:latest

                    # ✅ Push both
                    docker push ${REGION}-docker.pkg.dev/${PROJECT_ID}/${REPOSITORY}/${IMAGE_NAME}:${BUILD_TAG}
                    docker push ${REGION}-docker.pkg.dev/${PROJECT_ID}/${REPOSITORY}/${IMAGE_NAME}:latest
                    """
                }
            }
        }

        stage('Deploy to Cloud Run') {
            steps {
                script {
                    def BUILD_TAG = "${BUILD_NUMBER}"

                    sh """
                    gcloud run deploy ${IMAGE_NAME} \
                    --image ${REGION}-docker.pkg.dev/${PROJECT_ID}/${REPOSITORY}/${IMAGE_NAME}:${BUILD_TAG} \
                    --platform managed \
                    --region ${REGION} \
                    --allow-unauthenticated
                    """
                }
            }
        }
    }
}
