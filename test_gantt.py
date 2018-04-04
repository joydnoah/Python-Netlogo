import datetime
from plotly.offline import init_notebook_mode
import plotly.offline as py
import plotly.figure_factory as ff
import random

def make_dict(line):
    result_dict = {
        'Machine': line.split()[1][:2],
        'type': get_type(line.split()[1]),
        'content': line.split()
    }
    return result_dict

def get_type(machine_string):
    aux = machine_string.replace(machine_string[:2],"")
    if aux != "":
        return "0"
    else:
        return "1"

def filter_by_param(param_name, param_value, in_list):
    result = []
    for item in in_list:
        if item[param_name] == param_value:
            result.append(item)
    return result

def is_in_list(in_list, test_string):
    aux = False
    for item in in_list:
        aux = aux or (item == test_string)
    return aux

def find_machines(in_list):
    result = []
    for item in in_list:
        if not is_in_list(result, item['Machine']):
            result.append(item['Machine'])
    return result

def create_start_end_dict(in_list, draw_type):
    aux = iter(in_list)
    aux_list = []
    for item in zip(aux, aux):
        aux_dict = {
            'Task': draw_type + ' ' + item[0]['Machine'][1],
            'Start': '2017-01-01 ' + str(datetime.timedelta(seconds=int(float(item[0]['content'][0])))),
            'Finish': '2017-01-01 ' + str(datetime.timedelta(seconds=int(float(item[1]['content'][0])))),
            'Resource': 'Sub product ' + item[1]['content'][2]
        }
        aux_list.append(aux_dict)
    return aux_list

def random_colors():
    brgb = [random.uniform(0, 0.3), random.uniform(0.4, 0.6), random.uniform(0.7, 1)]
    random.shuffle(brgb)
    return tuple(brgb)


def draw_gantt(uri, draw_type):
    result = []
    with open(uri) as f:
        for line in f:
            result.append(make_dict(line))
        f.close()

    machines_list = find_machines(result)

    final = []
    for item in machines_list:
        result_aux = result
        result_aux = filter_by_param('Machine', item, result_aux)
        result_aux = filter_by_param('type', '0', result_aux)
        final.append(result_aux)

    aux = []
    for items in final:
        pre_aux = create_start_end_dict(items, draw_type)
        for item in pre_aux:
            aux.append(item)

    colors = {
        'Sub product 0': random_colors(),
        'Sub product 1': random_colors(),
        'Sub product 2': random_colors(),
        'Sub product 3': random_colors()
    }
    init_notebook_mode(connected=True)
    fig = ff.create_gantt(aux, colors=colors, index_col='Resource', show_colorbar=True, group_tasks=True)
    py.iplot(fig)
