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
        sh "docker ps"
      }
    }

    stage('Test execution') {

      steps{
        script {
          docker.image('jeffrycardona/test_automator:latest').inside("-u root") {  

            echo "Running inside Docker"
            //sh "automate.sh  -a \"${params.ARGS}\" -p \"${params.PARAMS}\" -n \"${params.PROJNAME}\" -m \"${params.APPNAME}\" -V \"${params.VERSION}\""

          }
        }
        sh "docker ps"
      }
    
    }

    stage('Ending execution') {

      steps{

        echo 'The JMeter tests were successfully executed'

      }

    }
  
  }
  
}
