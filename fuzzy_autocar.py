import tkinter as tk
import math
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import easygui
import matplotlib.patches as pc
path = easygui.fileopenbox()
file = open(path, mode="r")
lists = []
window = tk.Tk()

for line in file:
    line = line.strip('\n')
    list = line.split(",")
    lists.append(list)
x = []
y = []

figure, axes = plt.subplots()
origin = [int(lists[0][0]),int(lists[0][1])]
head = [origin[0]+4,origin[1]]
headleft45 = [0,0]
headright45 = [0,0]
lenhead = 100
lenheadleft45 = 100
lenheadright45 = 100
len_of_line = [0,0,0]
temp = [0,0]

def rotatecounterclockwise(origin,head,angle):
    global temp
    temp[0] = (head[0]-origin[0])*math.cos(math.radians(angle)) - (head[1]-origin[1])*math.sin(math.radians(angle))+origin[0]
    temp[1] = (head[0]-origin[0])*math.sin(math.radians(angle)) + (head[1]-origin[1])*math.cos(math.radians(angle))+origin[1]
def distance(origin,head):
    global lists
    lenhead = 100
    x1 = origin[0]
    y1 = origin[1]
    x2 = head[0]
    y2 = head[1]
    if(x1 == x2):
        k1 = None
        b1=0
    else:
        k1 = (y2-y1)*1.0/(x2-x1)
        b1=y1*1.0-x1*k1*1.0
    X=0
    Y=0
    minx=0
    miny=0
    for i in range(3,len(lists)-1):
        flag = 0
        x3 = float(lists[i][0])
        x4 = float(lists[i+1][0])
        y3 = float(lists[i][1])
        y4 = float(lists[i+1][1])
        if(x3 == x4):
            flag = 1
        if(x4-x3) == 0:
            k2 = None
            b2 = 0
        else:
            k2=(y4-y3)*1.0/(x4-x3)
            b2=y3*1.0-x3*k2*1.0
        if(k1!=k2):
            if k2==None:
                X=x3
                Y=k1*X*1.0+b1*1.0
            elif k1==None:
                X=x1
                Y=k2*X*1.0+b2*1.0
            else:
                X=(b2-b1)*1.0/(k1-k2)
                Y=k1*X*1.0+b1*1.0
            if(flag == 0):
                if(X<=max(x3,x4) and X>=min(x3,x4)):
                    if (head[0] - X)**2+(head[1]-Y)**2 < (origin[0] - X)**2+(origin[1]-Y)**2:
                        if(((origin[0] - X)**2+(origin[1]-Y)**2)**0.5 < lenhead):
                            minx = X
                            miny = Y
                            lenhead = min(lenhead,((origin[0] - X)**2+(origin[1]-Y)**2)**0.5)
            if (flag == 1):
                if Y>=min(y3,y4) and Y<=max(y3,y4):
                    if (head[0] - X)**2+(head[1]-Y)**2 < (origin[0] - X)**2+(origin[1]-Y)**2:
                        if(((origin[0] - X)**2+(origin[1]-Y)**2)**0.5 < lenhead):
                            minx = X
                            miny = Y
                            lenhead = min(lenhead,((origin[0] - X)**2+(origin[1]-Y)**2)**0.5)

    # plt.scatter(minx,miny,color = "g")
    return lenhead













def fuzzy():
    train_4 = open('train4D.txt', 'w')
    train_6 = open('train6D.txt', 'w')
    change_angle = 0
    t = 100
    while True:
        flag_pause = 0
        for i in range(3,len(lists)-1):
            flag = 0
            line_point1 = [float(lists[i][0]),float(lists[i][1])]
            line_point2 = [float(lists[i+1][0]),float(lists[i+1][1])]
            if(line_point1[0] == line_point2[0]):
                    flag = 1
            point = [origin[0],origin[1]]
            A = line_point2[1] - line_point1[1]
            B = line_point1[0] - line_point2[0]
            C = (line_point1[1] - line_point2[1]) * line_point1[0] + (line_point2[0] - line_point1[0]) * line_point1[1]
            distance_origin = abs(A * point[0] + B * point[1] + C) / (math.sqrt(A**2 + B**2))
            if(distance_origin < 3):
                if(flag == 0):
                    if(point[0]<=max(line_point1[0],line_point2[0]) and point[0]>=min(line_point2[0],line_point1[0])):
                        flag_pause = 1
                else:
                    if(point[1]<=max(line_point1[1],line_point2[1]) and point[1]>=min(line_point2[1],line_point1[1])):
                        flag_pause = 1
        if(flag_pause == 1):
            plt.text(35,20,"unsuccessful",color = "r")
            break
        # plt.cla()
        ##############################################################
        print(lists)
        for i in range(3,len(lists)-1):
            x = []
            y = []
            x = x + [float(lists[i][0])]
            x = x + [float(lists[i+1][0])]
            y = y + [float(lists[i][1])]
            y = y + [float(lists[i+1][1])]
            plt.scatter(x,y,color = "b")
            plt.plot(x,y,color = "r")
        
        endline1 = [float(lists[1][0]),float(lists[1][1])]
        endline2 = [float(lists[2][0]),float(lists[2][1])]
        axes.add_patch(pc.Rectangle(  (min(endline1[0],endline2[0]), min(endline1[1],endline2[1])), abs(endline1[0]-endline2[0]), abs(endline1[1]-endline2[1]),  color='#B2B2B2'  ))
        # draw_circle = plt.Circle((origin[0], origin[1]), 3,fill = False,color = "r")
        # axes.set_aspect(1)
        # axes.add_artist(draw_circle)
        ###########################################################前方向
        if t == 100: 
            angle = float(lists[0][2])
            rotatecounterclockwise(origin,head,angle)
        else:
            head[0] = origin[0]+4
            head[1] = origin[1]
            rotatecounterclockwise(origin,head,angle)
        for i in range(2):
            head[i] = (temp[i])
        x = []
        y = []
        x = x + [(head[0])]
        x = x + [(origin[0])]
        y = y + [(head[1])]
        y = y + [(origin[1])]
        # plt.plot(x,y,color = "r")
        len_of_line[1]= distance(origin,head)

        ###########################################################前方向
        ###########################################################左方向 
        rotatecounterclockwise(origin,head,45)
        for i in range(2):
            headleft45[i] = temp[i]
        x = []
        y = []
        x = x + [(headleft45[0])]
        x = x + [(origin[0])]
        y = y + [(headleft45[1])]
        y = y + [(origin[1])]
        # plt.plot(x,y,color = "r")
        len_of_line[0] = distance(origin,headleft45)
        ###########################################################左方向
        ###########################################################右方向
        rotatecounterclockwise(origin,head,-45)
        for i in range(2):
            headright45[i] = temp[i]
        x = []
        y = []
        x = x + [(headright45[0])]
        x = x + [(origin[0])]
        y = y + [(headright45[1])]
        y = y + [(origin[1])]
        # plt.plot(x,y,color = "r")
        len_of_line[2] = distance(origin,headright45)
        ###########################################################右方向
        ###########################################################角度轉變
        if((len_of_line[2] > 6 and len_of_line[2] < 13) and len_of_line[0] <= 6):
            change_angle = 5
        elif((len_of_line[0] > 6 and len_of_line[0] < 13)and len_of_line[2] <= 6):
            change_angle = -5
        elif(len_of_line[2] >= 13 or len_of_line[0] <= 6):
            change_angle = 10
        elif(len_of_line[0]>= 13 or len_of_line[2] <= 6):
            change_angle = -10
        
        
        ###########################################################角度轉變
        ###########################################################改變位置
        train_4.write(str(len_of_line[1]))
        train_4.write(" ")
        train_4.write(str(len_of_line[2]))
        train_4.write(" ")
        train_4.write(str(len_of_line[0]))
        train_4.write(" ")
        train_4.write(str(change_angle*-1))
        train_4.write(" ")
        train_4.write("\n")
        train_6.write(str(origin[0]))
        train_6.write(" ")
        train_6.write(str(origin[1]))
        train_6.write(" ")
        train_6.write(str(len_of_line[1]))
        train_6.write(" ")
        train_6.write(str(len_of_line[2]))
        train_6.write(" ")
        train_6.write(str(len_of_line[0]))
        train_6.write(" ")
        train_6.write(str(-1*change_angle))
        train_6.write(" ")
        train_6.write("\n")
        plt.text(35,50,"left_45",color = "b")
        plt.text(35,45,len_of_line[0])
        plt.text(35,40,"forward",color = "b")
        plt.text(35,35,len_of_line[1])
        plt.text(35,30,"right_45",color = "b")
        plt.text(35,25,len_of_line[2])
        ox = origin[0]
        oy = origin[1]
        print(change_angle)
        origin[0] += math.cos(math.radians(angle+change_angle)) + math.sin(math.radians(angle))*math.sin(math.radians(change_angle))
        origin[1] += math.sin(math.radians(angle+change_angle)) - math.sin(math.radians(change_angle))*math.cos(math.radians(angle))
        angle -= math.degrees(math.asin(2*math.radians(change_angle)/3))
        print(angle)
        x = []
        y = []
        x = x + [ox]        
        x = x + [origin[0]]
        y = y + [oy]
        y = y + [origin[1]]
        axes.plot(x,y,color = "r")

        t -= 1
        # plt.pause(0.000001)
        if(origin[0]<= max(endline1[0],endline2[0]) and origin[0]>= min(endline1[0],endline2[0])):
            if(origin[1]<= max(endline1[1],endline2[1]) and origin[1]>= min(endline1[1],endline2[1])):
                    plt.text(35,20,"successful",color = "r")
                    break
    plt.show()

lists2 = []
def select_path():
    path = easygui.fileopenbox()
    file = open(path, mode="r")
    for line in file:
        list = line.split()
        lists2.append(list)
    for l in range(len(lists2)):
        plt.cla()
            ##############################################################
        origin[0] = float(lists2[l][0])
        origin[1] = float(lists2[l][1])
        if l == 0:
            angle = float(lists[0][2])
            rotatecounterclockwise(origin,head,angle)
        else:
            head[0] = origin[0]+4
            head[1] = origin[1]
            angle -= math.degrees(math.asin(2*math.radians(-1*float(lists2[l][5]))/3))
            rotatecounterclockwise(origin,head,angle)
        for i in range(2):
            head[i] = (temp[i])
        x = []
        y = []
        x = x + [(head[0])]
        x = x + [(origin[0])]
        y = y + [(head[1])]
        y = y + [(origin[1])]
        plt.plot(x,y,color = "r")

        for i in range(3,len(lists)-1):
            x = []
            y = []
            x = x + [float(lists[i][0])]
            x = x + [float(lists[i+1][0])]
            y = y + [float(lists[i][1])]
            y = y + [float(lists[i+1][1])]
            plt.scatter(x,y,color = "b")
            plt.plot(x,y,color = "r")
        
        endline1 = [float(lists[1][0]),float(lists[1][1])]
        endline2 = [float(lists[2][0]),float(lists[2][1])]
        axes.add_patch(pc.Rectangle(  (min(endline1[0],endline2[0]), min(endline1[1],endline2[1])), abs(endline1[0]-endline2[0]), abs(endline1[1]-endline2[1]),  color='#B2B2B2'  ))

        draw_circle = plt.Circle((origin[0], origin[1]), 3,fill = False,color = "r")
        axes.set_aspect(1)
        axes.add_artist(draw_circle)
        
        plt.pause(0.000001)
    
b1 = tk.Button(window, text='模糊系統', font=('Arial', 12), width=10, height=1,command=fuzzy)
b1.place(x=10,y=50)
b2 = tk.Button(window, text='讀取路徑', font=('Arial', 12), width=10, height=1,command=select_path)
b2.place(x=10,y=100)
l1 = tk.Label(window, text = "一次選一個之後要重開",font=('Arial', 10),bg = "gray", width = 20, height = 2 )
l1.place(x=10,y=10)










window.mainloop()

