pipeline {
    agent any

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
                python3 -m pip install --upgrade pip
                pip3 install flake8 pytest
                '''
            }
        }

        stage('Lint') {
            steps {
                sh 'flake8 app/ --exit-zero'
            }
        }

        stage('Test') {
            steps {
                sh 'pytest tests/ --maxfail=1 --disable-warnings -q || true'
            }
        }

        stage('Deploy') {
            steps {
                withCredentials([sshUserPrivateKey(credentialsId: 'ansible-key', keyFileVariable: 'SSH_KEY')]) {
                    sh '''
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
