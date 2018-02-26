import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('white')
sns.set_context('talk')

import pyNetLogo

netlogo = pyNetLogo.NetLogoLink(gui=False)
url1 = r'Netlogo-files/Wolf Sheep Predation_v6.nlogo'
url2 = r'C:\Users\user\Desktop\Proyecto sergio\actual\EstudioCodigoL.nlogo'

netlogo.load_model(url2)
netlogo.command('setup')
netlogo.command('repeat 100000 [go]')
energy_wolves = netlogo.report('MSD')
print(energy_wolves)
