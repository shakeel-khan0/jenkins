pipeline {
    agent any

    stages {
        stage('Git-Checkout') {
            steps {
                echo 'Checking out from GitHub'
                git branch: 'main', url: 'https://github.com/shakeel-khan0/jenkins.git'
            }
        }
        stage('Build') {
            steps {
                echo 'Building the checked-out project'
                sh 'python3 countdown.py'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing the project'
                // Uncomment the line below to run your previous test
                // sh 'python3 -m unittest test.py'
                sh 'python3 -m unittest test_default.py'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying the project' 
                // Add deployment commands here, if any
            }
        }
    }

    post {
        always {
            echo "This will always run"
        }
        success {
            echo "Pipeline executed successfully"
        }
        failure {
            echo "Pipeline execution failed"
        }
    }
}
