pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git '•	https://github.com/OusamaAnsarMohamed/practica5.1'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m unittest test_calculadora.py'
            }
        }
    }
}
