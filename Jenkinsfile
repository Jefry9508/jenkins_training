pipeline {

  agent {

    label 'standard-slave'

  }

  stages {

    stage('Verifying properties') {
      steps{
        echo "PROJNAME: '${params.PROJNAME}'"
        echo "VERSION: '${params.VERSION}'"
        echo "APPNAME: '${params.APPNAME}'"
        echo "ARGS: '${params.ARGS}'"
        echo "PARAMS: '${params.PARAMS}'"
      }
    }

    stage('Test execution') {

      steps{
        sh 'ls'
        // customImage = docker.build("my-image:${env.BUILD_ID}")
        
      }
    
    }

    stage('Ending execution') {

      steps{

        echo 'The JMeter tests were successfully executed'

      }

    }
  
  }
  
}
