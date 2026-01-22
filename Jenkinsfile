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
                powershell """
                docker build -t $env:IMAGE_NAME .
                """
            }
        }

        stage('Run Application') {
            steps {
                echo "🚀 Running Flask app in Docker container..."
                powershell """
                # Stop container if already exists
                docker stop $env:CONTAINER_NAME -ErrorAction SilentlyContinue
                docker rm $env:CONTAINER_NAME -ErrorAction SilentlyContinue

                # Run container
                docker run -d -p $env:APP_PORT:5000 --name $env:CONTAINER_NAME $env:IMAGE_NAME
                """
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
