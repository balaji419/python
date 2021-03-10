def access_key=""
def secret_key=""
def token=""
pipeline {
  agent any
  stages {
    stage('intiating') {
      steps{
        script{
        sh "python3 get_creds.py"
        }
      }
    }
  }
}
