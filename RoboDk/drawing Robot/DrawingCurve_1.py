# Type help("robolink") or help("robodk") for more information
# Press F5 to run the script
# Documentation: https://robodk.com/doc/en/RoboDK-API.html
# Reference:     https://robodk.com/doc/en/PythonAPI/index.html
# Note: It is not required to keep a copy of this file, your python script is saved with the station
from robolink import *    # RoboDK API
from robodk import *      # Robot toolbox
RDK = Robolink()

# Notify user:
print('To edit this program:\nright click on the Python program, then, select "Edit Python script"')

#load excel file or txt file 
#def loadList():
#     csvdata = LoadList('threeData.csv')
#     values = []
#     for i in range(len(csvdata)):
#         print(csvdata[i])
#         values.append(csvdata[i])
#     return csvdata
 


list=[[259,362,5,180,0,180],
      [408,360,0,180,0,180]] 
    
    
def saveList(list):
    robodk.SaveList(list,'list_Coordinate')

def drawing(list):
    for i in list:   
     target=KUKA_2_Pose(i)
     print('target: '+str(i))
     print(target)
     robot.MoveL(target)
     

#---------------------------------------------------------------------------
# Program example:

#Program start
RDK = Robolink()

robot = RDK.Item('', ITEM_TYPE_ROBOT)
robot.setJoints([0,-90,90,0,0,0])        #set home position 




# get the home target and the tool targets:
#home = RDK.Item('Home')
#Start = RDK.Item('Start')


#calculating kinematic     joints to position
#home Joint([0,-90,90,0,0,0])
#print('home joints: ',robot.JointsHome().tolist())
#home position
#robot_position = robot.SolveFK(robot.JointsHome().tolist())
#print('kinematic: ',robot_position)

#calculationg inverse kinematic position to joints 
#new_robot_position = transl([200,0,0])*robot_position
#new_robot_joints = robot.SolveIK(new_robot_position)
#if len(new_robot_joints.tolist()) < 6:
#    print("No robot solution!! The new position is too far, out of reach or close to a singularity")
#print('new joints: ',new_robot_joints)    
    
 
# get the pose of the start (4x4 matrix representing position and orientation):
#start_poseref = Start.Pose()
#print(start_poseref)      #[850,100,400,180,0,-180]

#everytime restart from home and move to start point 

framedraw=RDK.Item('Frame object')
robot.setPoseFrame(framedraw)
#robot.setPoseTool(robot.PoseTool())
#robot.MoveJ(home)
#robot.MoveJ(Start)  
print('=====================================================================')

# delete previous image if any
image = RDK.Item('Board')
if image.Valid() and image.Type() == ITEM_TYPE_OBJECT: image.Delete()
#valid() check if the item is valid 
#Type() return the type of item 
#Delet() delet the item 


# make a drawing board base on the object reference "Blackboard 250mm"
board_1m = RDK.Item('Blackboard 250mm')
board_1m.Copy()                    # Copy the item to the clipboard.
board_draw = framedraw.Paste()     # Paste the copied Item from the clipboard as a child of this item 
board_draw.setVisible(True, False)
board_draw.setName('Board')
board_draw.Scale([4, 7, 1]) # adjust the board size to the image size (scale)


#List=loadList()

#saveList(list)

drawing(list)
#robot.MoveJ(new_robot_joints)


raise Exception('Program not edited.')
