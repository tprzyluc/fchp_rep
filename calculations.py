import scipy.interpolate
from debug import *

def interpolation(array_x, array_y):
    y_interp = scipy.interpolate.interp1d(array_x, array_y)
    info = "Interpolation result: "
    debug(info) 


x = [3,2,3,4,1,2,3,4]
y = [2,2,1,6,7,8,32,4]
interpolation(x,y)