pipeline {
    agent any
    
    environment {
        // This injects the new tool path right into the pipeline runtime environment
        PATH = "/var/jenkins_home/tools:${env.PATH}"
    }

    stages {
        stage('Code Checkout') {
            steps {
                echo 'Successfully pulled latest code changes from GitHub...'
            }
        }
        stage('Assemble Container Image') {
            steps {
                echo 'Compiling Dockerfile into an immutable image via system socket...'
                sh 'docker build -t local-data-pipeline:latest .'
            }
        }
    }
}

