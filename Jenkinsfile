pipeline {
    agent any

    stages {
        stage("Checkout") {
            steps {
                checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[credentialsId: '156d07ae-9e32-47c8-a778-ca3621206016', url: 'https://github.com/Alexeanred/unit-test-jenkins.git']])
            }
        }
        stage("Build") {
            steps {
                git credentialsId: '156d07ae-9e32-47c8-a778-ca3621206016', url: 'https://github.com/Alexeanred/unit-test-jenkins.git'
                sh 'python3 test_unit.py'
            }
        }
        stage("Test") {
            steps {
                sh 'python3 -m pytest'
            }
        }
    }
}