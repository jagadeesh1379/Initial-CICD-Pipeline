pipeline {
    agent any

    environment {
        IMAGE_NAME = "python-cicd-demo"
        CONTAINER_NAME = "python-cicd-app"
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
                sh """
                    docker build -t $IMAGE_NAME .
                """
            }
        }

        stage('Run Application') {
            steps {
                echo "🚀 Running Flask application..."
                sh """
                    # Stop existing container if running
                    if [ \$(docker ps -q -f name=$CONTAINER_NAME) ]; then
                        docker stop $CONTAINER_NAME
                        docker rm $CONTAINER_NAME
                    fi

                    # Run new container
                    docker run -d --name $CONTAINER_NAME -p $APP_PORT:5000 $IMAGE_NAME
                """
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
