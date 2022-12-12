# Type help("robolink") or help("robodk") for more information
# Press F5 to run the script
# Documentation: https://robodk.com/doc/en/RoboDK-API.html
# Reference:     https://robodk.com/doc/en/PythonAPI/index.html
# Note: It is not required to keep a copy of this file, your python script is saved with the station

from robolink import *    # RoboDK API
from robodk import *      # Robot toolbox
from array import *


# Notify user:
print('To edit this program:\nright click on the Python program, then, select "Edit Python script"')

#load excel file or txt file 
def loadList():
     csvdata = LoadList('threeData.csv')
     values = []
     for i in range(len(csvdata)):
         print(csvdata[i])
         values.append(csvdata[i])
     return csvdata
 

#list=[[259,362,100,180,0,180],
#     [259,362,0,180,0,180]] 

def QuadraticCurve(pointList, t,curveList):
     
     P0_x=pow(1-t,2)*pointList[0][0]
     P0_y=pow(1-t,2)*pointList[0][1]
     
     P1_x=2*(1-t)*t*pointList[1][0]
     P1_y=2*(1-t)*t*pointList[1][1]

     P2_x = t ** 2 * pointList[2][0]
     P2_y = t ** 2 * pointList[2][1]
     
     curve = (P0_x + P1_x + P2_x, P0_y + P1_y + P2_y)
     
     curveList.append((int(curve[0]),int(curve[1])))
     
     return curveList


def changeList(List):
     newList=[]
     newList.append([List[1][0], List[1][1]])
     newList.append([List[2][0],List[2][1]])
     newList.append([List[3][0],List[3][1]])
     return newList
 
def drawing(list):
    home_joints = robot.JointsHome().tolist()
    
    for i in list:
         if i[2]!=0:
             target=KUKA_2_Pose(i)
             print('target: '+str(i))
             print(target)
             robot.MoveJ(target)
         else:
             
             target=KUKA_2_Pose(i)
             print('target: '+str(i))
             print(target)
             robot.MoveL(target)
             
    robot.MoveJ(home_joints)


#---------------------------------------------------------------------------
# Program example:

#Program start
RDK = Robolink()
#get robot and set Home position
robot = RDK.Item('', ITEM_TYPE_ROBOT)
robot.setJoints([0,-90,90,0,0,0])        #set home position 

framedraw=RDK.Item('Frame object')


robot.setPoseFrame(framedraw)
robot.setPoseTool(robot.PoseTool())



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


List=loadList()      #[ [259,362,5,-180,0,-180],
                     #  [259,362,0,-180,0,-180],
                     #  [408,360,0,-180,0,-180],
                     #  [516,461,0,-180,0,-180] ]
                     
curveList=[]
t=0
run =True 
speed=0.05
count = 0
newList= changeList(List)
LastList=[[259, 362, 5, -180, 0, -180]] 

#newList=changeList(List)      #[(259, 362), (408, 360), (516, 461)]


while run:

      curve= QuadraticCurve(newList,t,curveList)      
      LastList.append( [curve[count][0], curve[count][1], 0, -180, 0, -180])
     
      count+=1

      if t >= 1 :
         t=0
         count =0
         run =False
         curveList.clear() 

      t+=speed 
     

  
drawing(LastList)

raise Exception('Program not edited.')
