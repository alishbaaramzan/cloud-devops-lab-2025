pipeline {
    agent any  // Run on any available agent

    stages {
        stage('Build') {
            steps {
                echo 'Building the project...'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploy stage (just for test)'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished!'
        }
    }
}
