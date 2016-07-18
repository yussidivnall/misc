#!/usr/bin/python
import json
import re
import operator

# Dictionary of id:
# ID:{ 'cost':N , 'cycle':(F,L) ,dij:{ 'dist':-1, prev:None } , 'nodes':[]}
# only minimal cycles (least cost/duration)
graph=dict()
#graph={ 'cost':None, 'cycle':(), 'nodes':[], 'dij':{ 'dist':-1, 'prev':None } }

# All songs (json object)
songs_json=None;

# Dictionary of id:
# [ID]:{ 'cost':N , cycle:(F,L) }
songs=dict();


def load_json(file_name):
    global songs_json
    global songs 
    # Load the song list json
    with open(file_name) as json_file:
        songs_json=json.load(json_file);
    for song in songs_json:
        song_id = int(song['id'])
        cost=int(song['duration'])
        first_letter, last_letter=get_letters(song['song'])
        if not first_letter or not last_letter:
            print "skipping song "+song['song'];
            next;
        node=(first_letter, last_letter, cost );
        songs[song_id]={'cycle' : (first_letter,last_letter), 'cost': cost  }



def get_letters(title):
    # Get start and end letters of this song name
    first=""
    last=""
    full_title=title;
    clean_title=re.sub(r'\(.*?\)','',full_title).lower().strip();#remove (...)
    p=re.compile("[a-zA-Z]");
    m=p.findall(clean_title);
    if m:
        first=m[0].lower()
        last=m[-1].lower()
    else:
        first=last=None;
    return first,last

def collect(songs,graph):
    # find all unique cycles with minimal cost
    # (a,a), (a,b), (a,...) ... (z,z)
    # ie (first letter,last letter)
    # add best cycles to graph
    
    songs = sorted(songs.items(), key=operator.itemgetter(1))

    for first in range(ord('a'),ord('z')):
        for last in range(ord('a'),ord('z')):
            m={key : value for key, value in songs if value['cycle']==(chr(first),chr(last)) }
            if m == {}: 
                #print "No match for "+chr(first)+" to "+chr(last)
                pass
            else: 
                cheapest=None
                selected=None
                for i,v in m.iteritems():
                    if cheapest==None or int(v['cost']) < cheapest: 
                        selected=v;
                        cheapest=int(v['cost'])
                # add to graph
                graph[i]=selected



def build(graph):
    # add child nodes to nodes[] ,ie nodes that start with last letter of current node
    # Only add array of ID indicies 
    # graph[key]={'cycle':(A,B), 'cost':N, 'dij':{'dist':P, 'prev':Q }, 'nodes'=[] }
    # Sort nodes[] by cheapest first
    for key, value in graph.iteritems():
        last_letter=value['cycle'][1];
        nodes={k:v for k,v in graph.iteritems() if v['cycle'][0]==last_letter}
        sorted_list=sorted(nodes, key=lambda k: nodes[k]['cost'] )
        graph[key]['nodes']=sorted_list

def traceback(graph,end_node,start_node):
    # Trace back and return a list of nodes, using the ['dij']['prev']
    # args:
    #   -   graph dictionary
    #   -   end_node to trace back from
    #   -   start_node to trace to
    # ret:
    #   -   (distance,[nodes ids] )
    ret=[]
    en= end_node[1]['dij']['prev']
    if not en:
        #Single song
        ret=(end_node[1]['cost'],[end_node[0]] )
    else:
        dist=end_node[1]['dij']['dist']
        n=end_node
        chain=[]
        while n[0] != start_node[0]:
            chain.append(n[0])
            prev_id=n[1]['dij']['prev']
            n=(prev_id,graph[prev_id])
        chain.append(start_node[0])
        ret=(dist,chain)
    return ret


def dsp(graph,start,goal):
        # Implements Dijkstra's shortest path algorithm
        # args:
        #   - graph dictionary
        #   - starting node
        #   - first letter of goal (chr)
        # ret:
        #   (dist,[node ids] ) or None if no path found
        # Uses song lengths as cost
        # ref : https://en.wikipedia.org/wiki/Dijkstra's_algorithm#Practical_optimizations_and_infinite_graphs
        

        # Maybe move this to declaration
        for k,v in graph.iteritems():
            graph[k]['dij']={'dist':-1, 'prev':None}
        start[1]['dij']['dist']=start[1]['cost']
        node=start
        que=[node]
        visited=[]
        while True:
            if len(que)==0:
                print "No path found from %s to %s" %(start[1]['cycle'][1], goal)
                return None
            node=que.pop()
            if node[1]['cycle'][1]==goal:
                #print "Found goal "+str(node[1]['cycle']) , str(node[1]['dij']['dist']), str(node[1]['dij']['prev'])
                return traceback(graph,node,start)
            visited.append(node)
            for cid in node[1]['nodes']:
                cn=(cid,graph[cid])
                if cn not in visited:
                    #Seems duplicate code, but too scared to modify
                    if cn not in que:
                        cn[1]['dij']['prev']=node[0]
                        cn[1]['dij']['dist']=node[1]['dij']['dist']+cn[1]['cost']
                        que.append(cn)
                    elif cn in que and (cn[1]['dij']['dist'] > node[1]['dij']['dist']+cn[1]['cost']):
                        cn[1]['dij']['prev']=node[0]
                        cn[1]['dij']['dist']=node[1]['dij']['dist']+cn[1]['cost']
                        
                        


def search(graph, first,last):
    # Search for all paths from first to last
    # run short path search once for every first cycle starting with first.
    # ie (first,'a'), (first,'b')...(first,'z')
    #
    # args:
    #   - graph dictionary
    #   - last letter of first song
    #   - first letter of last song
    # ret:
    #   - pool of all found paths, sorted by cost [ (cost,[node ids]),( ... )]

    #TODO sort by cost for optimisation
    # get nodes with cycles starting with 'first'
    starting_nodes={ k:v for k,v in graph.iteritems() if v['cycle'][0]==first }
    pool=[]
    #TODO Implement threading here
    for k,v in starting_nodes.iteritems():
        g=dict(graph) # New instance for every search, inorder to implement threads
        fin=dsp(g,(k,v),last)
        if fin:
            pool.append(fin)
        else:
            print "no path from %s to %s" %(v['cycle'][0] , last)
    print "Tracing from "+first+" to "+last
    if len(pool)==0:
        raise RuntimeError("No valid paths found")
    return sorted(pool)

def get_song_json_obj(song_id,songs_json):
    # returns the json object for the song_id
    for obj in songs_json:
        if int(obj['id']) == song_id: 
            return obj

def get_cycles(path):
    ret=[]
    for nid in path[::-1]:
        cycle=graph[nid]['cycle']
        ret.append(cycle)
    return ret

def main():
    load_json('song-library.json');
    collect(songs,graph)
    
    first_song="iz a zong that ends in K"
    last_song="C iis the first letter for me"
    a=first_song[-1].lower()   
    z=last_song[0].lower()      
    #a='n'
    #z='l'

    build(graph)
    paths=search(graph,a,z)
    best_route=paths[0]
    cycles=get_cycles(best_route[1])
    print cycles
    print first_song
    for nid in best_route[1][::-1]:
        obj=get_song_json_obj(nid,songs_json)
        print obj['duration'], obj['song']
    print last_song

if __name__=='__main__':
    main();
