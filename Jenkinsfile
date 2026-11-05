stage('Publish Docker Image') {
    steps {
        withCredentials([usernamePassword(
            credentialsId: 'dockerhub-creds',
            usernameVariable: 'DOCKER_USER',
            passwordVariable: 'DOCKER_PASS'
        )]) {
            sh '''
                set +x
                echo "$DOCKER_PASS" | docker login \
                    -u "$DOCKER_USER" --password-stdin

                docker push ${DOCKERHUB_USER}/${IMAGE_NAME}:${BUILD_NUMBER}
                docker push ${DOCKERHUB_USER}/${IMAGE_NAME}:latest

                docker logout
            '''
        }
    }
}
