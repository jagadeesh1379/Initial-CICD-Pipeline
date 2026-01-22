pipeline {
    agent any

    environment {
        IMAGE_NAME = "python-cicd-demo"
        CONTAINER_NAME = "python-app"
        APP_PORT = "5000"
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
                sh '''
                docker build -t $IMAGE_NAME .
                '''
            }
        }

        stage('Run Application') {
            steps {
                echo "🚀 Running Flask app in Docker container..."
                sh '''
                # Stop container if already exists
                docker stop $CONTAINER_NAME || true
                docker rm $CONTAINER_NAME || true

                # Run container
                docker run -d -p $APP_PORT:5000 --name $CONTAINER_NAME $IMAGE_NAME
                '''
            }
        }
    }

    post {
        success {
            echo "✅ CI/CD pipeline finished successfully!"
        }
        failure {
            echo "❌ CI/CD pipeline failed. Check logs."
        }
    }
}
