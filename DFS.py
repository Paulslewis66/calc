from collections import deque

G = {
    '0': ['7', '5', '3'],
    '7': ['2', '4'],
    '5': ['1'],
    '3': ['6'],
}

queue = deque()
queue.append(G)
checked = []

def algorithm(checked, queue, start):
    checked.append(start)
    # print(checked)
    queue.append(start)
    # print(queue)
    while queue:
        queue.popleft()
        print(queue)

        


algorithm(checked, queue, '4')