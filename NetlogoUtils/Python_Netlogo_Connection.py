import seaborn as sns
sns.set_style('white')
sns.set_context('talk')

import pyNetLogo
from NetlogoUtils.Controller import OnOfController
from NetlogoUtils import Graph_utils
from test_gantt import draw_gantt

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
    autonomy_value = []
    autonomy_per_time_value = []
    while finished == 0:
        workspace.command("repeat 10 [ go ]")

        time = workspace.report("time")
        autonomy_value.append(workspace.report("autonomy_value"))
        autonomy_per_time_value.append(autonomy_value[-1]/time)
        workspace.command("set dispatch_method \"" + OnOfController(autonomy_per_time_value[-1], "bio", parameters['setpoint'], parameters['range']) + "\"")
        time_list.append(time)
        MSD.append(workspace.report('MSD'))
        finished = workspace.report("finished")
        load_time.append(workspace.report("map [x -> [load_time] of x] ( sort shuttles )"))
        free_time.append(workspace.report("map [x -> [free_time] of x] ( sort shuttles )"))
        stop_time.append(workspace.report("map [x -> [stop_time] of x] ( sort shuttles )"))
        print('Time' + str(time))
        print('running...')

    debut_scenario = workspace.report("debut_scenario")
    fin_scenario = workspace.report("fin_scenario")
    shuttles = workspace.report("count shuttles")
    # Graph_utils.plot_shuttles(stop_time, free_time, load_time, time_list)
    for index in range(0, int(shuttles)):
        Graph_utils.plot_shuttles2(
            Graph_utils.transform_shuttle_list(stop_time, time_list, index),
            Graph_utils.transform_shuttle_list(free_time, time_list, index),
            Graph_utils.transform_shuttle_list(load_time, time_list, index), time_list)
    Graph_utils.simple_plot(autonomy_value, time_list, 'Autonomy', debut_scenario, fin_scenario)
    Graph_utils.simple_plot(autonomy_per_time_value, time_list, 'Autonomy per time', debut_scenario, fin_scenario)
    Graph_utils.simple_plot(autonomy_per_time_value, autonomy_value, 'Autonomy per time vs Autonomy')
    print(MSD[-1])



def setup_netlogo_env (parameters, workspace):
    workspace.command("set client_order_txt \"" + parameters['client_order_txt'] + "\"")
    workspace.command("set client_product_txt \"" + parameters['client_product_txt'] + "\"")
    workspace.command("set dispatch_method \"" + parameters['dispatch_method'] + "\"")
    workspace.command("set scenario \"" + parameters['scenario'] + "\"")
    workspace.command("set layout \"" + parameters['layout'] + "\"")

    workspace.command("set number_of_shuttles " + parameters['shuttles'])
    workspace.command("set shuttles_selection \"" + parameters['shuttles_selection'] + "\"")
    workspace.command("set pot_field_input \"" + parameters['pot_field_input'] + "\"")
    workspace.command("set bio_input \"" + parameters['bio_input'] + "\"")
    workspace.command("set GanttM " + parameters['GanttM'])
