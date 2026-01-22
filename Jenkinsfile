pipeline {
    agent any

    environment {
        IMAGE_NAME = "python-cicd-demo"
        CONTAINER_NAME = "python-app"
        PORT = "5000"
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo "🔄 Checking out code from GitHub"
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "📦 Building Docker image..."
                sh "docker build -t ${IMAGE_NAME} ."
            }
        }

        stage('Run Application') {
            steps {
                echo "🚀 Running Docker container..."
                // Stop and remove previous container if exists
                sh """
                    docker stop ${CONTAINER_NAME} || true
                    docker rm ${CONTAINER_NAME} || true
                    docker run -d -p ${PORT}:5000 --name ${CONTAINER_NAME} ${IMAGE_NAME}
                """
            }
        }
    }

    post {
        success {
            echo "✅ CI/CD pipeline succeeded!"
        }
        failure {
            echo "❌ CI/CD pipeline failed. Check logs."
        }
    }
}
