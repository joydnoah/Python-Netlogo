import seaborn as sns
sns.set_style('white')
sns.set_context('talk')

import pyNetLogo
from NetlogoUtils import Graph_utils

def run_experiment (parameters):
    workspace = pyNetLogo.NetLogoLink(gui=False)

    workspace.load_model(parameters['document_uri'])

    setup_netlogo_env(parameters, workspace)

    workspace.command("setup")

    finished = 0
    MSD = []
    time_list = []
    load_time = []
    free_time = []
    stop_time = []
    while finished == 0:
        workspace.command("repeat 100 [ go ]")

        time = workspace.report("time")
        time_list.append(time)
        MSD.append(workspace.report('MSD'))
        finished = workspace.report("finished")
        load_time.append(workspace.report("map [x -> [load_time] of x] ( sort shuttles )"))
        free_time.append(workspace.report("map [x -> [free_time] of x] ( sort shuttles )"))
        stop_time.append(workspace.report("map [x -> [stop_time] of x] ( sort shuttles )"))
        print('Time' + str(time))
        print('running...')

    Graph_utils.plot_something(stop_time, free_time, load_time, time_list)

def setup_netlogo_env (parameters, workspace):
    workspace.command("set client_order_txt \"" + parameters['client_order_txt'] + "\"")
    workspace.command("set client_product_txt \"" + parameters['client_product_txt'] + "\"")
    workspace.command("set dispatch_method \"" + parameters['dispatch_method'] + "\"")
    workspace.command("set scenario \"" + parameters['scenario'] + "\"")
    workspace.command("set layout \"" + parameters['layout'] + "\"")

    workspace.command("set number_of_shuttles " + parameters['shuttles'])
    workspace.command("set shuttles_selection \"" + parameters['shuttles_selection'] + "\"")