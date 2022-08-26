import subprocess, os, logging, json
from enum import Enum
from FrameworkPerformarceCLI import FrameworkPerformanceCLI

class PerformanceExplorer(FrameworkPerformanceCLI):

    def __init__(self, working_dir, path_jtl, proj_name, app_name, version_app, test_name):
        super().__init__("Performance Explorer")
        self.parser_command = ["psl-perfexp", "parse"]
        self.send_command = ["psl-perfexp", "send", "jmeter", "complete", "-inf"]
        self.version_command = ["psl-perfexp", "version"]
        self.info_file = "testInfo.json"
        self.results_name = "test"
        self.endpoint_summary_file = f"endpoint_summary_{self.results_name}.json"
        self.working_dir = working_dir
        self.path_jtl = path_jtl
        self.proj_name = proj_name
        self.app_name = app_name
        self.info_file_content = {}
        self.end_point_name = ""
        self.threads = ""
        self.version_app = version_app
        self.test_name = test_name

        logging.basicConfig(format='%(asctime)s : %(message)s', level=logging.INFO)
        
    
    def run_command(self):
        logging.info("Starting Performance Explorer execution")
        self.complement_command(Command.PARSER)
        logging.info(f"The following version of {self.name} will be used:")
        logging.info(f"Command to execute => {self.parser_command}")
        subprocess.run(self.parser_command)
        self.complement_command(Command.SEND)
        logging.info(f"Command to execute => {self.send_command}")
        subprocess.run(self.send_command)

    
    def get_version(self):
        subprocess.run(self.version_command)



    def complement_command(self, command_type):
        
        if command_type == Command.PARSER:
            self.parser_command.append("-rd")
            self.parser_command.append(self.working_dir)
            self.parser_command.append("-rn")
            self.parser_command.append(self.results_name)
            self.parser_command.append("-json")
            self.parser_command.append("jtl")
            self.parser_command.append(self.path_jtl)
        elif command_type == Command.SEND:
            path_info_file = self.create_info_file()
            self.send_command.append(path_info_file)
            self.send_command.append(self.working_dir)



    def create_info_file(self):

        self.read_endpoint_summary()

        self.info_file_content = {
            "scn_project_name": f"{self.proj_name}",
            "scn_application_name": f"{self.app_name}",
            "scn_transaction_name": f"{self.end_point_name}",
            "scn_job_name": f"{self.end_point_name}_Test",
            "scn_build_number": "1",
            "scn_version": f"{self.version_app}",
            "scn_test_name": f"{self.test_name}",
            "scn_tag": f"Test-{self.proj_name}-{self.app_name}",
            "scn_threads": f"{self.threads}"
        }

        json_file = json.dumps(self.info_file_content, indent=4)
        
        my_file = open(os.path.join(self.working_dir, self.info_file), "w")

        with my_file as out_file:
            out_file.write(json_file)

        my_file.close()

        return os.path.abspath(my_file.name)

    
    def read_endpoint_summary(self):
        my_file = open(os.path.join(self.working_dir, self.endpoint_summary_file), "r")
        data = json.loads(my_file.read())
        for tag in data:
            self.end_point_name += f"-{tag['result_endpoint_label']}"
        self.end_point_name = str(self.end_point_name.split("-", 1)[1])

        self.threads = data[0]["result_max_threads"]
        my_file.close()



class Command(Enum):
    PARSER = 1
    SEND = 2