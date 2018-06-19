import jenkins
import xml.etree.ElementTree as ET
import os

url = os.environ['JENKINS_URL']
username = os.environ['JENKINS_USERNAME']
password = os.environ['JENKINS_PASSWORD']
path_to_config_file = os.environ['JENKINS_JOB_CONFIG_FILE_PATH']
job_name = os.environ['JENKINS_JOB_NAME']

def convert_xml_file_to_str():
    tree = ET.parse(path_to_config_file)
    root = tree.getroot()
    return ET.tostring(root, encoding='utf8', method='xml').decode()

def main():
    target_server = jenkins.Jenkins(url, username=username, password=password)
    config = convert_xml_file_to_str()
    # @see http://python-jenkins.readthedocs.io/en/latest/api.html#jenkins.Jenkins.create_job
    target_server.create_job(job_name, config)

main()
