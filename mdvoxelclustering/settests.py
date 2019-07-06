#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 12:17:03 2019

@author: bart
"""
from collections import deque
import numpy as np
import matplotlib.pyplot as plt

identity_threshold = 0.0000001
cluster_mutations = {}

cluster1 = {'a1','a2','a3','a4','a5','a6','a7','a8','a9','a10'}
cluster2 = {'b1','b2','b3','b4','b5','b6','b7','b8','b9','b10'}
cluster3 = {'c1','c2','c3','c4','c5','c6','c7','c8','c9'}
cluster4 = {'d1','d2','d3'}
cluster5 = {'e1','e2','e3','e4','e5','e6','e7','e8'}
cluster6 = {'f1','f2','f3','f4','f5','f6','f7','f8','f9','f10'}
cluster7 = {'g1','g2','g3','g4'}
cluster8 = {'d7','d8','d9','d10','d4','d5'}

olddict1 = {
        1 : cluster1,
        2 : cluster2,
        3 : cluster3,
        4 : cluster4,
        5 : cluster5,
        6 : cluster6,
        7 : cluster7}


olddict2 = {
        1 : cluster1,
        2 : cluster2,
        3 : cluster3,
        4 : cluster4,
        5 : cluster5,
        6 : cluster6,
        7 : cluster7,
        8 : cluster8   
        }


olddict3 = {
        1 : cluster1,
        2 : cluster2,
        3 : cluster3,
        4 : cluster8,
        5 : cluster5,
        6 : cluster6,
        7 : cluster7,
        8 : cluster4   
        }

cluster11 = {'a1','a2','a3','a4','a5','a6','a7','a8','a9','a10'}
cluster12 = {'b1','b2','b3','b4','b5'}
cluster13 = {'c1','c2','c3','c4','c5','c6'}
cluster14 = {'d1','d2','d3','d4','d5','d6','d7','d8','d9','d10'}
cluster15 = {'f1','f2','f3','f4','f5','f6','f7','f8','f9','f10'}
cluster16 = {'e1','e2','e3','e4','e5','e6','e7','e8'}
cluster17 = {'g1','g2','g3'}
cluster18 = {'b7','b8','b9','b10'}


frame21 = deque([cluster11,cluster12,cluster13,cluster14,cluster15,cluster16,cluster17,cluster18])
frame22 = deque([cluster11,cluster12,cluster13,cluster14,cluster15,cluster16,cluster17])
frame23 = deque([cluster11,cluster12,cluster13,cluster14,cluster15,cluster16,cluster17])


test1 = {1: {'a8', 'a5', 'a6', 'a4', 'a9', 'a2', 'a10', 'a7', 'a3', 'a1'}, 2: {'b1', 'b4', 'b3', 'b5', 'b2'}, 3: {'c4', 'c5', 'c6', 'c1', 'c2', 'c3'}, 4: {'d9', 'd5', 'd6', 'd8', 'd10', 'd2', 'd7', 'd1', 'd3', 'd4'}, 5: {'e7', 'e5', 'e6', 'e1', 'e2', 'e3', 'e8', 'e4'}, 6: {'f2', 'f1', 'f3', 'f5', 'f6', 'f7', 'f9', 'f10', 'f8', 'f4'}, 7: {'g3', 'g1', 'g2'}, 9: {'b8', 'b9', 'b7', 'b10'}}
test2 = {1: {'a8', 'a5', 'a6', 'a4', 'a9', 'a2', 'a10', 'a7', 'a3', 'a1'}, 2: {'b1', 'b4', 'b3', 'b5', 'b2'}, 3: {'c4', 'c5', 'c6', 'c1', 'c2', 'c3'}, 5: {'e7', 'e5', 'e6', 'e1', 'e2', 'e3', 'e8', 'e4'}, 6: {'f2', 'f1', 'f3', 'f5', 'f6', 'f7', 'f9', 'f10', 'f8', 'f4'},  7: {'g3', 'g1', 'g2'}, 8: {'d9', 'd5', 'd8', 'd10', 'd7', 'd4'}}
test3 = {1: {'a8', 'a5', 'a6', 'a4', 'a9', 'a2', 'a10', 'a7', 'a3', 'a1'}, 2: {'b1', 'b4', 'b3', 'b5', 'b2'}, 3: {'c4', 'c5', 'c6', 'c1', 'c2', 'c3'}, 4: {'d9', 'd5', 'd6', 'd8', 'd10', 'd2', 'd7', 'd1', 'd3', 'd4'}, 5: {'e7', 'e5', 'e6', 'e1', 'e2', 'e3', 'e8', 'e4'},  6: {'f2', 'f1', 'f3', 'f5', 'f6', 'f7', 'f9', 'f10', 'f8', 'f4'}, 7: {'g3', 'g1', 'g2'}}

deprecated_dict = {
        8 : {'b7','b8','b9'}
}

def add_cluster_change(time,change):
   # print(cluster_mutations)
    if time in cluster_mutations:
        cluster_mutations[time].append(change)
    else:
        cluster_mutations[time] = [change]


def compare_clusters (clustersold,clustersnew,deprecated_clusters,clusternumber,frame_number):
    output = {}
    if len(clustersold) > len(clustersnew):
        mergelist = {}
        for key,value in clustersold.items():
            likeness_score=index=0
            for idx, clusternew in enumerate(clustersnew):
                temp_score = len(value.intersection(clusternew))/max(len(value),len(clusternew)) 
                if temp_score > likeness_score:
                    likeness_score = temp_score
                    index = idx
            if index in mergelist:
                if mergelist[index][0] > len(value):
                    print("cluster " + str(key) + " was merged into cluster " + str(mergelist[index][1]) + " at frame " + str(frame_number) + "  1")   
                    add_cluster_change(frame_number,(key,mergelist[index][1],"m"))
                    deprecated_clusters[key] = value
                else:
                    deprecated_clusters[mergelist[index][1]] = output[mergelist[index][1]]
                    print("cluster " + str(mergelist[index][1]) + " was merged into cluster " + str(key) + " at frame " + str(frame_number) + "  2")
                    add_cluster_change(frame_number,(mergelist[index][1],key,"m"))
               


            else:
                mergelist[index] = (len(value),key)
                output[key] = clustersnew[index]

        return output,clusternumber,deprecated_clusters
    else:
        for key,value in clustersold.items():
            likeness_score=index=0
           # if not clustersnew:
                 # If there are still old clusters, but no more new, check which two clusters have merged by comparing each cluster.
            #     for key_out,value_out in output.items():
            #         temp_score = len(value.intersection(value_out))/max(len(value),len(value_out)) 
            #         if temp_score > likeness_score:
            #                likeness_score = temp_score
            #                index = key_out
            #     if len(value) > len(value_out):
            #         output[key] = value 
            #         del output[index]
            #         deprecated_clusters[index] = value_out
            #         print("cluster " + str(index) + " was merged into cluster " + str(key) + " at frame " + str(frame_number))
            #         add_cluster_change(frame_number,(index,key,"m"))
            #     else:
            #         print("cluster " + str(key) + " was merged into cluster " + str(index) + " at frame " + str(frame_number))   
            #         add_cluster_change(frame_number,(key,index,"m"))
             #        deprecated_clusters[key] = value
            #else:
            for idx, clusternew in enumerate(clustersnew):
                temp_score = len(value.intersection(clusternew))/max(len(value),len(clusternew)) 
                if temp_score > likeness_score:
                    likeness_score = temp_score
                    index = idx

            clustersnew.rotate(-index)
            output[key] = clustersnew.popleft()
        while clustersnew:
            likeness_score=index=0
            for key,value in clustersold.items():
                temp_score = len(value.intersection(clusternew))/max(len(value),len(clusternew)) 
                if temp_score > likeness_score:
                    likeness_score = temp_score
                    index = key
            likeness_score = 0
            remerge = False
            if len(clusternew) > len(output[index]):
                clusternew, output[index] = output[index],

            for key, value in deprecated_clusters.items():
                
                temp_score = len(value.intersection(clusternew))/max(len(value),len(clusternew)) 
                if (temp_score > identity_threshold) and (temp_score > likeness_score) :
                    likeness_score = temp_score
                    index_old = key
                    remerge = True
                
            if remerge:
                output[index_old] = clustersnew.popleft()
                print ("cluster " + str(index_old) + " was recreated from cluster " + str(index) + " at frame " + str(frame_number))
                add_cluster_change(frame_number,(index_old,index,"rc"))
                del deprecated_clusters[index_old]
            else:
                newkey = clusternumber + 1
                clusternumber = newkey
                output[newkey ] = clustersnew.popleft()
                print ("cluster " + str(newkey) + " was created from cluster " + str(index) + " at frame " + str(frame_number))
                add_cluster_change(frame_number,(newkey,index,"c"))
        return output,clusternumber,deprecated_clusters

    
                
                  
                
            
            
#if  compare_clusters(olddict1,frame21,deprecated_dict,8,1)== test1 :
#    print(" test1 ok :)")

#if  compare_clusters(olddict2,frame22,{0 : set()},8,1)== test2 :
#    print(" test1 ok :)")
    
# if  compare_clusters(olddict3,frame23,{0 : set()},8,1) == test3:
#    print("test3 ok :)")
        

data = np.load('clusters.npy')

# single frame set creation for all sets
#for frame in data:
#    olddict[clustercount] =set(np.where(data[0] == (idx))[0])
#for frame in data:
#    print(set(frame))


def sort_clusters(data):
    clustercount = 0
    olddict = {0 : set()}
    deprecated_clusters = {}
    plotinfo = {0 : []}
    for idx, frame in enumerate(data):
        newcluster = deque()
        plotvariables = []
        for cluster in set(frame):     
            newcluster.append(set(np.where(frame == cluster)[0]))  
        olddict, clustercount, deprecated_clusters = compare_clusters(olddict, newcluster, deprecated_clusters,clustercount,idx)
        for key, value in olddict.items():
            for index in value:
                frame[index] = key
            plotvariables.append((key,len(value)))
        plotinfo[idx] = plotvariables
    return data,plotinfo
data, plotinfo = sort_clusters(data)

np.save('clusters_ordered', data)
np.save('Visualization_data',plotinfo)
np.save('Cluster_mutations',cluster_mutations)
#
#time = range(len(plotinfo))
#ordered_clusters = plotinfo.values()
#print(time)
#print(ordered_clusters) 
#plt.bar(time, ordered_clusters, align='center')
#plt.xticks(range(len(plotinfo)), list(plotinfo.keys()))
#        
plt.show()
