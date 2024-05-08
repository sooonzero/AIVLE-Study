def solution(todo_list, finished):
    answer = todo_list.copy()
    for i in range(len(todo_list)):
        if finished[i] == 1:
            answer.remove(todo_list[i])
        else:
            continue

    return answer