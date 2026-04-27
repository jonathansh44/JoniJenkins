pipeline {
    agent any
    
    // החלק החדש שמוסיף את דוקר ל-PATH של הג'נקינס
    tools {
        dockerTool 'my-docker' 
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Docker Build + Tag') {
            steps {
                script {
                    // עכשיו הפקודה docker תעבוד
                    sh "docker build -t joni-flask:${env.BUILD_NUMBER} ."
                    sh "docker tag joni-flask:${env.BUILD_NUMBER} joni-flask:latest"
                }
            }
        }
    }
}
