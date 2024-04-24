pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh("docker build -t sicei-${GIT_BRANCH}:1.0.0-${BUILD_NUMBER} .")
                sh("docker images")
            }
        }
    }
}