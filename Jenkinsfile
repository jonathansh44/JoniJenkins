pipeline {
    agent any

    stages {
        // שלב 1: משיכת הקוד מהגיט
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        // שלב 2: בדיקה שהקוד תקין (אופציונלי אבל מומלץ)
        stage('Test') {
            steps {
                echo 'Running tests...'
                // כאן אפשר להריץ פקודות כמו python -m pytest
            }
        }

        // שלב 3: המשימה שלנו - בניית ה-Image
        stage('Docker Build + Tag') {
            steps {
                script {
                    // בניית האימג' עם שם ומספר בילד
                    sh "docker build -t joni-flask:${env.BUILD_NUMBER} ."
                    // תיוג כ-latest
                    sh "docker tag joni-flask:${env.BUILD_NUMBER} joni-flask:latest"
                }
            }
        }
    }
}