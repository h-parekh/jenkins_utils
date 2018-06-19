### A compilation of Python scripts to manage Jenkins programmatically
These scripts leverage [python-jenkins](https://pypi.org/project/python-jenkins/) library that provides a wrapper for the Jenkins [remote access API](https://wiki.jenkins.io/display/JENKINS/Remote+access+API)

## Setup
1. [Install](https://python-jenkins.readthedocs.io/en/latest/install.html#installing) python-jenkins
2. [envchain](https://github.com/sorah/envchain) (Optional if you have an alternate way to manage environment variables)
3. Clone the repository

## Usage
1. Set environment variables required by the script. See [guidance](setting_env_variables.md) if you are using `envchain`
3. Run script as any other python script
```console
python <script_name>.py
```
