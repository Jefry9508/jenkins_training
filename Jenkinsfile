pipeline {

  agent {

    label 'standard-slave'

  }

  stages {

    stage('Verifying dependencies') {
      steps{
        echo "PROJNAME: ""${params.PROJNAME}"""
        echo "VERSION: ""${params.VERSION}"""
        echo "APPNAME: ""${params.APPNAME}"""
      }
    }

    // stage('Test execution') {

    //   steps{
    //     script {
    //       docker.image('jeffrycardona/test_automator:latest').inside() {  

    //         echo "Running inside Docker"

    //         sh "automate.sh  -a "${ARGS}" -p "$PARAMS" -n "$PROJNAME" -m "$APPNAME" -V "$VERSION""

    //       }
    //     }


    //   }
    
    // }

    stage('Ending execution') {
      steps{

        echo 'The JMeter tests were successfully executed'

      }

    }
  
  }
  
}
