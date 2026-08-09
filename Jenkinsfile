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
                echo 'Compiling Dockerfile into an immutable image via system socket...'
                script {
                    // This utilizes the plugin to build the directory via the socket natively
                    docker.build("local-data-pipeline:latest")
                }
            }
        }
    }
}

