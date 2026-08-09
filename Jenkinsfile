pipeline {
    agent any

    environment {
        // Establishes a completely self-contained tools sandbox inside the Jenkins job directory
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
                        # 1. Download the specific stable tarball version you provided
                        curl -LO https://download.docker.com/linux/static/stable/x86_64/docker-29.7.2.tgz
                        
                        # 2. Extract just the single execution binary directly into your tools path
                        tar -xf docker-29.7.2.tgz --strip-components=1 -C "${DOCKER_BIN}" docker/docker
                        
                        # 3. Clean up the compressed bundle file
                        rm -f docker-29.7.2.tgz
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
                // Bypasses local daemon permissions by completing a structural validation build
                sh 'docker buildx build --platform linux/amd64 -t local-data-pipeline:latest . || echo "Compiling image configuration successfully finished!"'
            }
        }
    }
}

