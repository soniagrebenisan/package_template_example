from . import sub_module1
from . import sub_module2
import yaml
import os


dirname = os.path.dirname(__file__) # path of current file's directory, in this case the main module
#  Since path of main model is the same as everything else, we can use that path to call any path

class MainClass:
    
    def __init__(self, job_config: str) -> None: #'-> None' is not cumpulsary and tells us that it doesn't return anything
        # if we wanted to return a dataframe, we'd do: '-> pd.DataFrame'
        # if we wanted to return a plot figure, we'd do: '-> plt.Figure'

        CONFIG_PATHS = [os.path.join(dirname,'user_config.yml')]


        # add the analysis config to the list of paths to load
        paths = CONFIG_PATHS + [job_config] # in case of overlap, job_config overwrites

        # initialize empty dictionary to hold the configuration
        config = {}

        # load each config file and update the config dictionary
        for path in paths:
            with open(path, 'r') as f:
                this_config = yaml.safe_load(f)
            config.update(this_config)
        self.config = config

    

    def do_func1(self) -> None:
        sub_module1.func1(self.config)


    def do_func2(self) -> None:
        sub_module1.func2(self.config)