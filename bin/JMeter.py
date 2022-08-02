import subprocess
import getopt
import os
import platform
import logging
import traceback
from datetime import datetime
from LoadInjector import LoadInjector

class JMeter(LoadInjector):

    def __init__(self, pathLoadInjector):
        super().__init__("JMeter", pathLoadInjector)

        self.short_args_jmeter = {"jmx": "-t", "jtl": "-l", "version": "-v"}
        self.long_args_jmeter = {"jmx": "--jmx", "jtl": "--jtl", "version": "--version"}
        self.executable_file_linux = "jmeter"
        self.executable_file_win = "jmeter.bat"
        self.jtl_files_dir = "Jtl_Files"
        self.pathJMX = ""
        self.pathJTL = ""
        self.absolute_path = ""
        self.properties = {}
        self.command_base = []
        self.working_dir = ""

        if platform.system() == "Windows":
            if pathLoadInjector != "":
                self.absolute_path = os.path.join(pathLoadInjector, self.executable_file_win)
            else:
                self.absolute_path = self.executable_file_win
        elif platform.system() == "Linux":
            if pathLoadInjector != "":
                self.absolute_path = os.path.join(pathLoadInjector, self.executable_file_linux)
            else:
                self.absolute_path = self.executable_file_linux
        else:
            raise Exception("Unsupported platform")
        
        logging.basicConfig(format='%(asctime)s : %(message)s', level=logging.INFO)
        
    def run_test(self, args):
        self.__validate_arguments(args)
        self.__get_version()
        self.__append_properties_as_arguments()
        logging.info(f"Command to execute => {self.command_base}")
        subprocess.run(self.command_base)

    def __get_version(self):
        subprocess.run([f"{self.absolute_path}", "-v"])

    def __validate_arguments(self, opts):
        for opt, arg in opts:
            if opt in (f"-{self.short_arguments['arguments']}", f"-{self.long_arguments['arguments']}"):
                self.__split_args_test(arg)
            elif opt in (f"-{self.short_arguments['properties']}", f"-{self.long_arguments['properties']}"):
                self.__split_props_test(arg)
            
        if self.properties.__len__() == 0:
            logging.info("No properties were found in the command. The test will be executed with the properties of the jmeter.properties file.\n")

    def __split_args_test(self, args):
        try:
            list_args = args.split(";")

            for arg in list_args:
                specific_arg = arg.split("=")
                
                if specific_arg[0] in (self.short_args_jmeter["jmx"], self.long_args_jmeter["jmx"]):
                    self.pathJMX = specific_arg[1]
                    logging.info(f"Path JMX file: {self.pathJMX}")
                elif specific_arg[0] in (self.short_args_jmeter["jtl"], self.long_args_jmeter["jtl"]):
                    self.working_dir = os.path.join(os.getcwd(), self.jtl_files_dir, "test_results")
                    os.mkdir(self.working_dir)
                    self.pathJTL = os.path.join(self.working_dir, specific_arg[1])
                    logging.info(f"Path JTL file: {self.pathJTL}")
            
            if self.pathJMX == "" or self.pathJTL == "":
                raise Exception()
        except Exception as e:
            logging.error(str(e))
            logging.error(traceback.format_exc())
            raise Exception(f"Error reading the arguments needed to run the {self.name} command. You may have written an argument wrong or missing arguments.")
    

    def __split_props_test(self, args):
        try:
            list_props = args.split(";")
            
            for prop in list_props:
                specific_prop = prop.split("=")
                if specific_prop.__len__() == 2:
                    self.properties[specific_prop[0]] = specific_prop[1]
                    
        except:
            raise Exception(f"Error reading the properties to run the {self.name} command.")

    
    def __append_properties_as_arguments(self):

        self.command_base = [f"{self.absolute_path}", "-n", "-t", f"{self.pathJMX}", "-l", f"{self.pathJTL}"]
        
        if self.properties.__len__() > 0:
            for key,value in self.properties.items():
                self.command_base.append(f"-J{str.upper(key)}={value}")

        
