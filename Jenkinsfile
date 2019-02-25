pipeline {
  agent { label 'linux' }

  environment {
    env_name = 'notebooks'
    deploy_branch = 'gh-pages'
  }

  stages {
    stage('Setup') {
      steps {
        checkout scm
        sh("conda env update --file=environment.yml")
      }
    }

    stage('Convert/Check') {
      steps {
        sh("with_env -n ${env_name} python convert.py")
        sh("with_env -n ${env_name} python -m 'nbpages.check_nbs'")
      }
    }

    stage('Deploy') {
      steps {
        script {
          if(env.JOB_NAME.toLowerCase().contains('pr')) {
            echo "Pull Request, Not deploying..."
          } else {
            echo "Deploying to Github Pages"
            dir('../pages') {
              sshagent (credentials: ['jenkins-ghpages-deploy']) {
                // TODO: Update url (ssh url for repo)
                sh("git clone -b ${deploy_branch} --single-branch git@github.com:obviousrebel/notebooks.git")
                dir('./notebooks') {
                  sh("""cp -aR ${env.WORKSPACE}/* .
                    git config --global user.email jenkins-deploy@stsci.edu
                    git config --global user.name jenkins-deploy
                    git add .""")
                    //git commit -m 'Automated deployment to GitHub Pages: ${env.BUILD_TAG}' --allow-empty
                    //git push origin ${deploy_branch}""")
                }
              }
              deleteDir()
            }
            archiveArtifacts artifacts: '**/*.html', onlyIfSuccessful: true, allowEmptyArchive: true
          }
        } // end of script
      } // end of deploy steps
    } // end of deploy stage

  } // end of stages
} // end of pipeline
