pipeline {
    agent any
    
    stages {
        stage('Clone Repository') {
            steps {
                git url:'https://github.com/KPkm25/jenkins_assessment.git', branch: 'main' 
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        
        stage('Run Tests') {
            steps {
			sh 'pytest pytest/test.py'        
    }
        }
        
        stage('Build and Archive') {
            steps {
                sh 'mkdir -p build'
                sh 'cp -r * build/'
                archiveArtifacts artifacts: 'build/**', fingerprint: true
            }
        }
    }
}
