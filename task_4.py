new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
completed_tasks = ['task_002', 'task_012', 'task_006']

completed_tasks.append(new_tasks.pop()) #Перенес задачу из одного списка в другой

new_tasks.pop(2) #Удалил задачу из плана

print(new_tasks[2]) #Вывод на экран последней задачи, которую подняли в приоритете
