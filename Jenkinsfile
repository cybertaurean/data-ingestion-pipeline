pipeline {
    agent any

    stages {
        stage('Code Checkout') {
            steps {
                echo 'Successfully pulled latest code changes from GitHub...'
            }
        }
        stage('Assemble Container Image') {
            steps {
                echo 'Compiling Dockerfile into an immutable Podman image blueprint...'
                // Jenkins instructs your laptop engine to package the code
                sh 'docker build -t local-data-pipeline:latest .'
            }
        }
    }
}

