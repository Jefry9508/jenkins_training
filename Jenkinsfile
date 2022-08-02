pipeline {

  agent {

    label 'standard-slave'

  }

  stages {

    stage('Build docker image') {

      steps{
        script{
          customImage = docker.build("automation_base:latest", "--no-cache --build-arg USER_GIT='${param.USER_GIT}' --build-arg PASS_GIT='${param.PASS_GIT}' --build-arg URL_PERF='${param.URL_PERF}' --build-arg USER_PERF='${param.USER_PERF}' --build-arg PASS_PERF='${param.PASS_PERF}' --build-arg ARGS='${param.ARGS}' --build-arg PARAMS='${param.PARAMS}' --build-arg PROJNAME='${param.PROJNAME}' --build-arg APPNAME='${param.APPNAME}' --build-arg VERSION='${param.VERSION}'")
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
