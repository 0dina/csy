graph = {}
graph["you"] = ["ana","bob","cat"]
graph["bob"] = ["dao","evy"]
graph["ana"] = ["evy"]
graph["cat"] = ["fom","gil"]
graph["dao"] = []
graph["evy"] = []
graph["fom"] = []
graph["gil"] = []

from collections import deque
search_queue = deque()
search_queue += graph["you"]


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    
    while search_queue:
        person = search_queue.popleft()
        if person_is_seller(person):
            if not person in searched:
                print (person + " is a mango seller!")
                return True
        else:
            search_queue += graph[person]
            searched.append(person)
    return False

def person_is_seller(name):
    return name[-1] == 'm'

search("you")