def solution(priorities,location):
    queue = [(idx,priority) for (idx,priority) in enumerate(priorities)]
    answer = 0

    while queue:
        front = queue.pop(0)
        if any(front[1] < doc[1] for doc in queue):
            queue.append(front)
        else:
            answer += 1
            if front[0] == location:
                break
    return answer


priorities = [2, 1 ,3, 2]
location = 2
print(solution(priorities,location))

priorities = [1,1,9,2,3,4]
location = 1
print(solution(priorities,location))