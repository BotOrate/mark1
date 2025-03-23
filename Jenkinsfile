pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                // Checkout the source code from the Git repository
                git branch: 'main', url: 'https://github.com/BotOrate/mark1.git'  
            }
        }
        // stage('Install Dependencies') {
        //     steps {
        //         // Install dependencies if needed (optional if you have a requirements.txt)
        //         // sh 'pip install -r requirements.txt'  // Uncomment if using dependencies
        //     }
        // }
        stage('Run Tests') {
            steps {
                bat 'python3 test.py'
            }
        }
    }
    post {
        success {
            echo 'Python script ran successfully.'
        }
        failure {
            echo 'Python script failed.'
        }
    }
}
