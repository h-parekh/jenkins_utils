### Here's a handy way to securely store environment variables using [envchain](https://github.com/sorah/envchain)

1. Install envchain
```console
brew install envchain
```

2. Verify installation
```console
$ envchain
envchain version 1.0.1
```

3. Set variables
This command sets `JENKINS_URL` and `JENKINS_JOB_NAME` in the 'jenkins' namespace
```console
$ envchain --set jenkins JENKINS_URL JENKINS_JOB_NAME
jenkins.JENKINS_URL: https://sample-jenkins-url.com/
jenkins.JENKINS_JOB_NAME: my-job
```
4. Run commands that want to leverage these variables. All you're doing is
prefixing any command with `envchain <namespace>`
```console
$ envchain jenkins python myscript.py
```

5. [Optional] Set your variables to be available globally, and then you won't
have to prefix command with `envchain <namespace>`
```console
export $(envchain jenkins env | grep JENKINS)
```
