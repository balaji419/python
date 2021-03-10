def access_key="dummy"
def secret_key=""
def token=""
pipeline {
  agent any
  stages {
    stage('intiating') {
      steps{
        script{
          result=sh (
    script: 'python3 get_creds.py',
    returnStdout: true
).trim()
        //sh "python3 get_creds.py"
          echo "$result"
        }
      }
    }
  }
}
