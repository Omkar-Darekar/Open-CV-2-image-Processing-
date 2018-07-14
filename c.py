from __future__ import print_function
import matplotlib.pyplot as plt
import cv2
import os
import numpy as np



def obstacle(*mlist):
    print ("mlist",mlist)
    i=0
    j=0
    tmp = len(mlist)
    tmp1=tmp-1
    #print ("tmp",tmp)
    tmp = tmp/2
    tmp = int(tmp)
    #print ("new tmp",tmp)
    #print ("mlist =",mlist[3][1])
    barriers = []
    
    
    for item in mlist:
        for item in mlist:
            if j>1:
                break
            if i>tmp:
                #print (mlist[i][j])
                break
            #print (mlist[i][j])
            barriers.append([(mlist[i][0],mlist[i][1]),(mlist[i+1][0],mlist[i+1][1])])
            
            print ((mlist[i][0],mlist[i][1]),(mlist[i+1][0],mlist[i+1][1]))
            
            j=j+1

        if i>tmp:
            #print (mlist[i][j])
            break
            
        i=i+1
        j=0
            
    barriers.append([(mlist[0][0],mlist[0][1]),(mlist[tmp1][0],mlist[tmp1][1])])
    print ((mlist[0][0],mlist[0][1]),(mlist[tmp1][0],mlist[tmp1][1]))
    for barrier in barriers:
        plt.plot([v[0] for v in barrier], [v[1] for v in barrier])
        plt.xlim(0,1000)
        plt.ylim(0,1000)
        
    plt.show()    
    
    
    '''
    
    
    
    ite = len(mlist)
    ite = int(ite)
    barriers = []
    
    for item in ite:
            for jtem in ite:
                barriers.append([(mlist[i],mlist[j]),(mlist[i+1],mlist[j+1])])
                j=j+1
            i=i+1    
    

    for barrier in barriers:
        plt.plot([v[0] for v in barrier], [v[1] for v in barrier])
        plt.xlim(-1,8)
        plt.ylim(-1,8)
        plt.show()


    '''
            
    '''
    
    
    barriers.append([(ob_x,ob_y),((ob_x)+3,(ob_y)+3)])

    for barrier in barriers:
        plt.plot([v[0] for v in barrier], [v[1] for v in barrier])
    plt.xlim(-1,8)
    plt.ylim(-1,8)
    plt.show()
'''
    

'''
class AStarGraph(p[x],p[y]):
    #Define a class board like grid with two barriers
 
    def __init__(self):
        self.barriers = []
        self.barriers.append([p(x,y),(x,y)])
        
''' 

if __name__=="__main__":

    def read_img(path):
        """Given a path to an image file, returns a cv2 array

        str -> np.ndarray"""
        if os.path.isfile(path):
            return cv2.imread(path)
        else:
            raise ValueError('hiiiiiiiiii')


    path = 'abc.jpg'
    im = read_img(path)
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    #im = cv2.imread("hand_01.jpg")
    #gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    _, bin = cv2.threshold(gray,120,255,1) # inverted threshold (light obj on dark bg)
    bin = cv2.dilate(bin, None)  # fill some holes
    bin = cv2.dilate(bin, None)
    bin = cv2.erode(bin, None)   # dilate made our shape larger, revert that
    bin = cv2.erode(bin, None)
    bin, contours, hierarchy = cv2.findContours(bin, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    rc = cv2.minAreaRect(contours[0])
    box = cv2.boxPoints(rc)
    mylist = []
    for p in box:
        pt = ((p[0],p[1]))
        cv2.circle(im,pt,5,(200,0,0),2)
        
        mylist.append((p[0],p[1]))
        
    graph =obstacle(*mylist)
    
    '''
    graph = AStarGraph()
    '''
    #graph = AStarGraph(p[0],p[1])
    '''
    graph.variable
    variable=(p[0],p[1])
    '''

    #result, cost = AStarSearch((0,0), (6,3), graph)
    #print ("route", result)
    #print ("cost", cost)
    #plt.plot([v[0] for v in result], [v[1] for v in result])
    '''

    for barrier in graph.barriers:
        plt.plot([v[0] for v in barrier], [v[1] for v in barrier])
    plt.xlim(-1,8)
    plt.ylim(-1,8)
    plt.show()
    '''

'''
{{out}}
route [(0, 0), (1, 1), (2, 2), (3, 1), (4, 1), (5, 1), (6, 2), (7, 3), (6, 4), (7, 5), (6, 6), (7, 7)]
cost 
'''
