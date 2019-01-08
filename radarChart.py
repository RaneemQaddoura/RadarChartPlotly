""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""                                                                        """
"""                              Radar Chart                               """
"""              Plot a radar chart from a data file using plotly          """
"""                         @author: Raneem Qaddoura                       """
"""   @email: rqaddoura@philadelphia.edu.jo, raneem.qaddoura@gmail.com     """
"""                                 v1.0                                   """
"""                                                                        """
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Radar Chart Plotly
# Plot a radar chart from a data file using plotly
# The CSV file is of a single measure for the performace of each dataset against several algorithms
# Columns in the CSV file represent data sets. 
# The last column is the same as the first column to make the figure connected
# Rows in the CSV file represent the algorithms

import plotly.graph_objs as go
import plotly.io as pio
import numpy as np
import os

def readDataFile(directory, filename):
    """
    Reads the data file and store a list of Point ............

    Parameters
    ----------
    directory : str
        The file location of the dataset
    filename : str
        The dataset file name

    Returns
    -------
    ndarray
        The data as a numpy matrix
    """
    global nPoints, nValues, k, points, labelsTrue
    rawData = open(os.path.join(directory + filename), 'rt')  
    data = np.loadtxt(rawData, delimiter=",")
    return data

directory = ""

dataset_List = ['DS1',"DS2","DS3", "DS4","DS5","DS6","DS7", "DS8","DS9","DS10","DS11","DS12","DS13", "DS14","DS15","DS16", "DS17", "DS18","DS19","DS20","DS1"]
radar_List = ["Alg1","Alg2","Alg3","Alg4","Alg5","Alg6","Alg7","Alg8"]

measure = ["M1"]

for p in range(len(measure)):    
    filename = measure[p] + ".csv"
    
    #cols represent data sets. The last column is the same as the first column to make the figure connected
    #rows represent algorithms
    dataFile = readDataFile(directory, filename)
        
    data = []
    for i in range(len(radar_List)):
        data.append(go.Scatterpolar(      
                r = dataFile[i],
                theta = dataset_List,
                fill = None,
                name = radar_List[i]
                )        
        )    
    
    layout = go.Layout(
      font=dict(size=16),
      polar = dict(
        radialaxis = dict(
          visible = True,
          range = [0, 1]
        )
      ),
      margin=go.layout.Margin(
        l=0,
        r=0,
        b=0,
        t=30,
        pad=0
      ),
      showlegend = True,
      legend=dict(orientation="h",xanchor='center',x=0.5)
    )
    
    fig = go.Figure(data=data, layout=layout)
    pio.write_image(fig, directory + str(measure[p]) + '.pdf')