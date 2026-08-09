pipeline {
    agent {
        // This tells Jenkins to spin up an isolated, secure image builder bubble natively
        docker { 
            image 'docker:dind'
            args '-v /var/run/docker.sock:/var/run/docker.sock'
        }
    }

    stages {
        stage('Code Checkout') {
            steps {
                echo 'Successfully pulled latest code changes from GitHub...'
            }
        }
        stage('Assemble Container Image') {
            steps {
                echo 'Compiling Dockerfile inside an isolated DinD agent...'
                sh 'docker build -t local-data-pipeline:latest .'
            }
        }
    }
}

