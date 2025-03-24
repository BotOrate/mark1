pipeline {
    agent any

    environment {
        // Define environment variables (adjust these as needed)
        GOOGLE_APPLICATION_CREDENTIALS = credentials('gcp-service-account-key')  // GCP service account credentials (Jenkins secret)
        BUCKET_NAME = 'your-bucket-name'
    }

    stages {
        stage('Setup') {
            steps {
                script {
                    echo 'Setting up environment...'
                    sh '''
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Run Model Validation') {
            steps {
                script {
                    echo 'Running model validation...'
                    sh '''
                    source venv/bin/activate
                    python model_validation.py
                    '''
                }
            }
        }

        stage('Run Bias Checking') {
            steps {
                script {
                    echo 'Checking bias...'
                    sh '''
                    source venv/bin/activate
                    python bias_checking.py
                    '''
                }
            }
        }

        stage('Run Model Selection') {
            steps {
                script {
                    echo 'Selecting best model based on validation and bias results...'
                    sh '''
                    source venv/bin/activate
                    python model_selection.py
                    '''
                }
            }
        }

        stage('Push Model to Registry') {
            steps {
                script {
                    echo 'Pushing model to registry...'
                    sh '''
                    source venv/bin/activate
                    python model_registry.py
                    '''
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            sh '''
            rm -rf venv
            '''
        }

        success {
            echo 'Pipeline ran successfully!'
        }

        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
    }
}
