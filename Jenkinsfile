pipeline {
  agent any
  stages {
    stage('Checkout') { steps { git 'https://github.com/Hrishikesh-2712/jenkin_q3' } }
    stage('Build')    { steps { sh 'docker build -t jenkins-app .' } }

    // TODO: add cleanup (post block) to remove the test container after the stage runs
  }
}
