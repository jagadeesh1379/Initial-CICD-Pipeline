pipeline {
    agent any

    environment {
        IMAGE_NAME = "python-cicd-demo"
        CONTAINER_NAME = "python-app"
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Run Python Deploy Script') {
            steps {
                // Use Python to handle all Docker steps
                sh 'python deploy.py'
            }
        }
    }

    post {
        success {
            echo "✅ CI/CD pipeline completed successfully!"
        }
        failure {
            echo "❌ CI/CD pipeline failed. Check logs."
        }
    }
}
