pipeline {
    agent {
        docker {
            image 'python:3.10'   // official Python image
        }
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    credentialsId: 'github-creds',
                    url: 'https://github.com/alishbaaramzan/cloud-devops-lab-2025.git'
            }
        }

        stage('Install Deps') {
            steps {
                sh '''
                    python -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Lint') {
            steps {
                sh '''
                    . venv/bin/activate
                    flake8 app/ --exit-zero
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest tests/ --maxfail=1 --disable-warnings -q || true
                '''
            }
        }

        stage('Deploy') {
            steps {
                withCredentials([sshUserPrivateKey(credentialsId: 'ansible-key', keyFileVariable: 'SSH_KEY')]) {
                    sh '''
                        . venv/bin/activate
                        ansible-playbook \
                          -i ansible/inventory/hosts.ini \
                          ansible/playbooks/app.yml \
                          --private-key $SSH_KEY
                    '''
                }
            }
        }
    }

    post {
        success {
            echo 'Deployment successful'
        }
        failure {
            echo 'Pipeline failed'
        }
    }
}
