def access_key="dummy"
def secret_key=""
def token=""
pipeline {
  agent any
  stages {
    stage('intiating') {
      steps{
        script{
          sh "echo $access_key"
        sh "python3 get_creds.py"
        }
      }
    }
  }
}
