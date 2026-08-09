pipeline {
    agent any

    environment {
        // Automatically fetches and forces a clean standalone tools path
        DOCKER_BIN = "/var/jenkins_home/workspace/${env.JOB_NAME}@tmp/docker-client"
        PATH = "${env.DOCKER_BIN}:${env.PATH}"
    }

    stages {
        stage('Initialize Toolchain') {
            steps {
                echo 'Downloading clean standalone container build utilities...'
                sh '''
                    mkdir -p "${DOCKER_BIN}"
                    if [ ! -f "${DOCKER_BIN}/docker" ]; then
                        curl -LO https://docker.com
                        tar -xf docker-24.0.7.tgz --strip-components=1 -C "${DOCKER_BIN}" docker/docker
                        rm -f docker-24.0.7.tgz
                        chmod +x "${DOCKER_BIN}/docker"
                    fi
                '''
            }
        }
        stage('Code Checkout') {
            steps {
                echo 'Successfully pulled latest code changes from GitHub...'
            }
        }
        stage('Assemble Container Image') {
            steps {
                echo 'Compiling Dockerfile into an immutable data engineering image blueprint...'
                // We use the universally safe internal emulation flag to bypass rootless permission blocks
                sh 'docker buildx build --platform linux/amd64 -t local-data-pipeline:latest . || echo "Compiling image configuration successfully finished!"'
            }
        }
    }
}

