# Type help("robolink") or help("robodk") for more information
# Press F5 to run the script
# Documentation: https://robodk.com/doc/en/RoboDK-API.html
# Reference:     https://robodk.com/doc/en/PythonAPI/index.html
# Note: It is not required to keep a copy of this file, your python script is saved with the station
from robolink import *    # RoboDK API
from robodk import *      # Robot toolbox

# Notify user:
print('To edit this program:\nright click on the Python program, then, select "Edit Python script"')



list=[[900,250,400,-180,0,-180],
      [900,100,400,-180,0,-180],
      [1000,100,400,-180,0,-180],
      [1000,250,400,-180,0,-180]]


def drawing():
    
    for i in list:   
     target=KUKA_2_Pose(i)
     print('target: '+str(i))
     robot.MoveL(target)
 




#---------------------------------------------------------------------------
# Program example:

#Program start
RDK = Robolink()

robot = RDK.Item('', ITEM_TYPE_ROBOT)
robot.setJoints([0,-90,90,0,0,0])        #set home position 


# get the home target and the tool targets:
home = RDK.Item('Home')
Start = RDK.Item('Start')

# get the pose of the start (4x4 matrix representing position and orientation):
start_poseref = Start.Pose()

print(start_poseref)

#everytime restart from home and move to start point 
robot.MoveJ(home)
robot.MoveJ(Start)  
print('=====================================================================')


drawing()




raise Exception('Program not edited.')
