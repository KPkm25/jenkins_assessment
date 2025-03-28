pipeline {
    agent any
    
    stages {
        stage('Clone Repository') {
            steps {
                git url:'https://github.com/KPkm25/jenkins_assessment.git', branch: 'main' 
            }
        }
        
        stage('Set up Virtual Environment') {
            steps {
                script {
                    sh 'python3 -m venv venv'
                }
            }
        }
        
        stage('Install Dependencies') {
            steps {
                script {
                    sh '''
                        bash -c "source venv/bin/activate"
                        venv/bin/pip install -r requirements.txt
                        venv/bin/pip install setuptools
                    '''
                }
            }
        }
        
        stage('Run Tests') {
            steps {
		script {
    			sh '''
        		bash -c "source venv/bin/activate"
        		export PYTHONPATH=$(pwd)
        		venv/bin/pytest pytest/
    			'''
}
            }
        }
        
        stage('Build and Archive') {
            steps {
                script {
			sh """
    			mkdir -p build
    			cp -r Jenkinsfile app.py pytest requirements.txt venv build/
			"""

                }
                archiveArtifacts artifacts: 'build/**', fingerprint: true
            }
        }
    }
}
