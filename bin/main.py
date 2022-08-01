import sys, getopt, os
from JMeter import JMeter
from PerformanceExplorer import PerformanceExplorer

short_properties = {"help":"h", "properties": "p", "version": "v", "path": "r", "arguments": "a", "projname": "n", "appname": "m", "versionapp": "V"}
long_properties = {"help":"help", "properties": "properties=", "version": "version", "path": "path", "arguments": "args=", "projname": "projname=", "appname": "appname=", "versionapp": "versionapp="}

help_text = '''

    Please, use the following options:



      -a    Command arguments to execute


      -h    Help


      -n    Project name. It has to be exactly the name of the project you created.


      -m    Application name. The name that represents the application you are testing.


      -p    List of test scenario properties in quotation marks. <"prop1=value1;prop2=value2,propN=valueN">


      -r    Path of JMeter


      -v    Product version


      -V    Version
      
    '''


def main(argv):

   path = ""
   contains_args = False
   proj_name = ""
   app_name = ""
   version_app = ""

   try:
      opts, args = getopt.getopt(argv, f"{short_properties['help']}{short_properties['version']}{short_properties['path']}{short_properties['arguments']}:{short_properties['properties']}:{short_properties['projname']}:{short_properties['appname']}:{short_properties['versionapp']}:",
                    [f"{long_properties['path']}", f"{long_properties['arguments']}", f"{long_properties['properties']}", f"{long_properties['help']}", f"{long_properties['version']}", f"{long_properties['projname']}", f"{long_properties['appname']}", f"{long_properties['versionapp']}"])
      
      if opts.__len__() == 0:
         raise getopt.GetoptError("No argument found")

      for opt, arg in opts:

         if opt in (f"-{short_properties['help']}", f"--{long_properties['help']}"):
            print(help_text)
            sys.exit()
         elif opt in (f"-{short_properties['version']}", f"--{long_properties['version']}"):
            print("Product version: v1.0.0")
            sys.exit()
         elif opt in ("-r", "--path"):
            path = arg
         elif opt in ("-a", "--args"):
            contains_args = True
         elif opt in ("-n", "--projname"):
            proj_name = arg
         elif opt in ("-m", "--appname"):
            app_name = arg
         elif opt in ("-V", "--versionapp"):
            version_app = arg
      print(opts)

      if proj_name != "" and app_name != "" and version_app != "" and contains_args:
         jmeter = JMeter(path)
         jmeter.run_test(opts)

         test_name = os.path.basename(jmeter.pathJMX).replace(".jmx", "")

         perf_explorer = PerformanceExplorer(jmeter.working_dir, jmeter.pathJTL, proj_name, app_name, version_app, test_name)
         perf_explorer.run_command()
      else:
         raise getopt.GetoptError("Incomplete arguments")

   except (getopt.GetoptError, Exception) as e:
      message = ""
      if isinstance(e, getopt.GetoptError):
         message = e.msg
      elif isinstance(e, Exception):
         message = str(e)
      print(
        f'''

    Error: {message}

        {help_text}
      
      ''')

      sys.exit(2)



if __name__ == "__main__":
   main(sys.argv[1:])