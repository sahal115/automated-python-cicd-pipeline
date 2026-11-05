stage('Publish Docker Image') {
    steps {
        withCredentials([
            usernamePassword(
                credentialsId: 'dockerhub-creds',
                usernameVariable: 'DOCKER_USER',
                passwordVariable: 'DOCKER_TOKEN'
            )
        ]) {
            sh '''
                set +x
                echo "$DOCKER_TOKEN" | docker login \
                    -u "$DOCKER_USER" --password-stdin

                docker tag python-cicd-demo:${BUILD_NUMBER} \
                    "$DOCKER_USER/python-cicd-demo:${BUILD_NUMBER}"

                docker tag python-cicd-demo:latest \
                    "$DOCKER_USER/python-cicd-demo:latest"

                docker push "$DOCKER_USER/python-cicd-demo:${BUILD_NUMBER}"
                docker push "$DOCKER_USER/python-cicd-demo:latest"

                docker logout
            '''
        }
    }
}
