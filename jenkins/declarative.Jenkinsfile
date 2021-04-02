pipeline {
    agent { docker { image 'gradle:latest' }
    }
stages {
    stage('Clone Git') {
        steps {
            git 'https://github.com/umasuryasai/ci-cd-testing.git'
        }
    }
       stage('Push your docker image') {
        steps {
            sh '''
            
            docker --version

            '''
          }
        }
}
}