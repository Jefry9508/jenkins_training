pipeline {

  agent {

    label 'standard-slave'

  }

  stages {

    stage('Build docker image') {

      steps{
        script{
          sh 'cat Jenkinsfile'
          customImage = docker.build("automation_base:latest", "--no-cache --build-arg USER_GIT='${params.USER_GIT}' --build-arg PASS_GIT='$PASS_GIT' --build-arg URL_PERF='${params.URL_PERF}' --build-arg USER_PERF='${params.USER_PERF}' --build-arg PASS_PERF='$PASS_PERF' --build-arg ARGS='${params.ARGS}' --build-arg PARAMS='${params.PARAMS}' --build-arg PROJNAME='${params.PROJNAME}' --build-arg APPNAME='${params.APPNAME}' --build-arg VERSION='${params.VERSION}' .")
        }
      }
    
    }

    stage('Run docker container and execute test') {

      steps{
        script{
          customImage.withRun("automation_base:latest")
        }
      }

    }
  
  }
  
}
