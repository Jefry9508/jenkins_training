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
        script {
          docker.image('jeffrycardona/test_automator:latest').withRun("--name test_aut -u root") {  

            echo "Running inside Docker"
            sh "docker ps"
            //sh "automate.sh  -a \"${params.ARGS}\" -p \"${params.PARAMS}\" -n \"${params.PROJNAME}\" -m \"${params.APPNAME}\" -V \"${params.VERSION}\""

          }
        }
      }
    
    }

    stage('Ending execution') {

      steps{

        echo 'The JMeter tests were successfully executed'

      }

    }
  
  }
  
}
