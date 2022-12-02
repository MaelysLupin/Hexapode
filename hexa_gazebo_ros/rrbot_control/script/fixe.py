#!/usr/bin/env python3

from turtle import bgcolor
import rospy
import numpy as np
from std_msgs.msg import Float64
import math 
from tkinter import *
from sensor_msgs.msg import Imu
import tf.transformations

fenetre = Tk()
fenetre.configure(background='#AEAEAE')
fenetre.title("Interface Hexapode")
fenetre.geometry("800x820")


def boutonQuit():

    exit()


def boutonValide():
    global rotax, rotay, rotaz
    global translx, transly, translz
    rotax = rot2x.get()
    rotay = rot2y.get()
    rotaz = rot2z.get()

    translx = transx.get()
    transly = transy.get()
    translz = transz.get()

    fenetre.destroy()

    return(0)

def reset():
    global rotax, rotay, rotaz
    global translx, transly, translz
    rotax = 0.0
    rotay = 0.0
    rotaz = 0.0

    translx = 0.0
    transly = 0.0
    translz = 0.0

    fenetre.destroy()

    return(0)

#ZONE BOUTON

label = Label(fenetre, text="Rotation (en radian)",height = 2, width = 20,background='#088897', anchor=CENTER)
label.pack(padx=10,pady=10)

#Saisir angle

zone0 = Frame(fenetre)
zone0.pack(fill=Y)
zone0.configure(background='#AEAEAE')
        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Zone 1

libelle_rot2x = Label(zone0, text='\n Autour de x :',background='#AEAEAE')
libelle_rot2x.grid()

x = DoubleVar() 

rot2x = Entry(zone0, textvariable=x, width=10)
rot2x.grid()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Zone 2

libelle_rot2y = Label(zone0, text='\n Autour de y :',background='#AEAEAE')
libelle_rot2y.grid()

y = DoubleVar() 

# boite de saisie
rot2y = Entry(zone0, textvariable=y, width=10)
rot2y.grid()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Zone 3

libelle_rot2z = Label(zone0, text='\n Autour de z :',background='#AEAEAE')
libelle_rot2z.grid()

z = DoubleVar() 

#Boite de saisie
rot2z = Entry(zone0, textvariable=z, width=10)
rot2z.grid()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#ZONE BOUTON

label = Label(fenetre, text="Translation ",height = 2, width = 20,background='#088897', anchor=CENTER)
label.pack(padx=10,pady=10)

#Saisir angle

zone1 = Frame(fenetre)
zone1.pack(fill=Y)
zone1.configure(background='#AEAEAE')
        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Zone 1

libelle_transx = Label(zone1, text='\n En x :',background='#AEAEAE')
libelle_transx.grid()

x = DoubleVar() 

transx = Entry(zone1, textvariable=x, width=10)
transx.grid()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Zone 2

libelle_transy = Label(zone1, text='\n En y :',background='#AEAEAE')
libelle_transy.grid()

y = DoubleVar() 

# boite de saisie
transy = Entry(zone1, textvariable=y, width=10)
transy.grid()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Zone 3

libelle_transz = Label(zone1, text='\n En z :',background='#AEAEAE')
libelle_transz.grid()

z = DoubleVar() 

# boite de saisie
transz = Entry(zone1, textvariable=z, width=10)
transz.grid()

 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#QUIT 
b6 = Button(fenetre, text="QUIT", highlightbackground='#FF6161',background='#FF6161', highlightthickness = 2,command = boutonQuit)
b6.pack(side=BOTTOM,fill=X, ipadx=20, ipady=6, padx=5,pady=5)

#VALIDER 
b7 = Button(fenetre, text="Confirm", highlightbackground='#AFE7A6',background='#AFE7A6', highlightthickness = 2,command = boutonValide)
b7.pack(side=BOTTOM,fill=X, ipadx=20,ipady=3, padx=5,pady=5)

#RESET
b8 = Button(fenetre, text="Reset", highlightbackground='#FCC06E',background='#FCC06E', highlightthickness = 2,command = boutonValide)
b8.pack(side=BOTTOM,fill=X, ipadx=20,ipady=3, padx=5,pady=5)

mainFrame = Frame(fenetre)
mainFrame.place()                

lmain = Label(mainFrame)
lmain.grid(row=0, column=0)

fenetre.update()
fenetre.mainloop()


def callback1(msg):
    print(tf_to_transform_matrix(msg.orientation))

def tf_to_transform_matrix(tf_msg):
    
    # Make the quaternion a numpy array
    q = np.array([tf_msg.x,
                tf_msg.y,
                tf_msg.z,
                tf_msg.w])
    
    # Form the transform matrix from the translation and the quaternion
    angle = tf.transformations.euler_from_quaternion(q)
    
    return angle


if __name__ == '__main__':

    A = 2.2
    # A = 1.0
    # VALEURS DES ANGLES DE ROTATION

    # thetax = float(input("Rotation x ? "))
    # thetay = float(input("Rotation y ? "))
    # thetaz = float(input("Rotation z ? "))
    thetax = A*float(rotax)
    thetay = A*float(rotay)
    thetaz = A*float(rotaz)
    

    # VALEURS DES TRANSLATIONS

    # Tx = float(input("Translation x ? "))
    # Ty = float(input("Translation y ? "))
    # Tz = float(input("Translation z ? "))
    Tx = float(translx)
    Ty = float(transly)
    Tz = float(translz)


    rospy.init_node('talker2', anonymous=True)
    pub1 = rospy.Publisher('rrbot/verin_joint1_position_controller/command', Float64, queue_size=1)
    pub2 = rospy.Publisher('rrbot/verin_joint2_position_controller/command', Float64, queue_size=1)
    pub3 = rospy.Publisher('rrbot/verin_joint3_position_controller/command', Float64, queue_size=1)
    pub4 = rospy.Publisher('rrbot/verin_joint4_position_controller/command', Float64, queue_size=1)
    pub5 = rospy.Publisher('rrbot/verin_joint5_position_controller/command', Float64, queue_size=1)
    pub6 = rospy.Publisher('rrbot/verin_joint6_position_controller/command', Float64, queue_size=1)
    sub1 = rospy.Subscriber('imu', Imu, callback1, queue_size=1)
    rate = rospy.Rate(50)


    h = 0
    h2 = -1.28


    # x1 = np.array([[0.208], [-0.575], [h], [1]])
    # x01 = np.array([[-0.18], [-0.8], [h2], [1]])

    # x2 = np.array([[0.395], [-0.465], [h], [1]])
    # x02 = np.array([[0.78], [-0.24], [h2], [1]])

    # x3 = np.array([[0.395], [0.465], [h], [1]])
    # x03 = np.array([[0.78], [0.24], [h2], [1]])

    # x4 = np.array([[0.208], [0.575], [h], [1]])
    # x04 = np.array([[-0.18], [0.8], [h2], [1]])

    # x5 = np.array([[-0.6], [0.11], [h], [1]])
    # x05 = np.array([[-0.6], [0.55], [h2], [1]])

    # x6 = np.array([[-0.6], [-0.11], [h], [1]])
    # x06 = np.array([[-0.6], [-0.55], [h2], [1]])

    x1=np.array([[0.197], [-0.578], [h], [1]])
    x01=np.array([[-0.18], [-0.8], [h2], [1]])

    x2=np.array([[0.405], [-0.46], [h], [1]])
    x02=np.array([[0.78], [-0.24], [h2], [1]])

    x3=np.array([[0.405], [0.46], [h], [1]])
    x03=np.array([[0.78], [0.24], [h2], [1]])

    x4=np.array([[0.197], [0.578], [h], [1]])
    x04=np.array([[-0.18], [0.8], [h2], [1]])

    x5=np.array([[-0.6], [0.11], [h], [1]])
    x05=np.array([[-0.6], [0.5395], [h2], [1]])

    x6=np.array([[-0.6], [-0.11], [h], [1]])
    x06=np.array([[-0.6], [-0.5395], [h2], [1]])



    while not rospy.is_shutdown():

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        # MATRICE DE ROTATION VIDE 
        MTH = np.array([
            [0., 0., 0., 0.],
            [0., 0., 0., 0.],
            [0., 0., 0., 0.],
            [0., 0., 0., 0.]])


        # MATRICES ROTATION SELON AXES
        def rotX(theta):
            return np.array([[1,0,0],
                            [0, np.cos(theta), -np.sin(theta)],
                            [0, np.sin(theta), np.cos(theta)]])

        def rotY(theta):
            return np.array([[np.cos(theta),0, np.sin(theta)],
                            [0,1,0],
                            [-np.sin(theta),0, np.cos(theta)]])

        def rotZ(theta):
            return np.array([[np.cos(theta), -np.sin(theta),0],
                            [np.sin(theta), np.cos(theta),0],
                            [0,0,1]])


        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        R1 = np.dot(rotZ(thetaz),rotY(thetay))
        R = np.dot(R1,rotX(thetax))
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        T = np.array([
            [Tx],
            [Ty],
            [Tz],
            [1]])

        MTH[:3,:3] = R
        MTH[:,3:4] = T
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        xp1 = np.dot(MTH,x1)
        xp2 = np.dot(MTH,x2)
        xp3 = np.dot(MTH,x3)
        xp4 = np.dot(MTH,x4)
        xp5 = np.dot(MTH,x5)
        xp6 = np.dot(MTH,x6)

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        #CALCUL NOUVELLE LONGUEUR DES VERINS

        #longueur vérin fermé
        l0 = 1.0

        c1 = math.sqrt(math.pow(x01[0]-xp1[0],2)+math.pow(x01[1]-xp1[1],2)+math.pow(x01[2]-xp1[2],2))-l0
        c2 = math.sqrt(math.pow(x02[0]-xp2[0],2)+math.pow(x02[1]-xp2[1],2)+math.pow(x02[2]-xp2[2],2))-l0
        c3 = math.sqrt(math.pow(x03[0]-xp3[0],2)+math.pow(x03[1]-xp3[1],2)+math.pow(x03[2]-xp3[2],2))-l0
        c4 = math.sqrt(math.pow(x04[0]-xp4[0],2)+math.pow(x04[1]-xp4[1],2)+math.pow(x04[2]-xp4[2],2))-l0
        c5 = math.sqrt(math.pow(x05[0]-xp5[0],2)+math.pow(x05[1]-xp5[1],2)+math.pow(x05[2]-xp5[2],2))-l0
        c6 = math.sqrt(math.pow(x06[0]-xp6[0],2)+math.pow(x06[1]-xp6[1],2)+math.pow(x06[2]-xp6[2],2))-l0
        # print(c1,c2,c3,c4,c5,c6)
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        # EXCEPTIONS

        if (c1 or c2 or c3 or c4 or c5)<0.05 or (c1 or c2 or c3 or c4 or c5)>0.72:
            print("\n ~~~~~~~~~~~~~~~~~ IMPOSSIBLE ~~~~~~~~~~~~~~~~~")
            print("\n ~~~~~~~~~~ Choisir d'autres valeurs ~~~~~~~~~~")
            exit()

        pub1.publish(-c1)
        pub2.publish(-c2)
        pub3.publish(-c3)
        pub4.publish(-c4)
        pub5.publish(-c5)
        pub6.publish(-c6)

        rate.sleep()



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
