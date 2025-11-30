print("=== ПРОГРАММА ЗАПУЩЕНА ===")

class EngineeringTask:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.is_completed = False
        print(f"Создана задача: {title}")

class PendingFilter:
    def filter(self, tasks):
        return [task for task in tasks if not task.is_completed]

class CompletedFilter:
    def filter(self, tasks):
        return [task for task in tasks if task.is_completed]

def show_tasks(tasks, filter_name=""):
    print(f"\n--- {filter_name} ---")
    for task in tasks:
        status_icon = "✅" if task.is_completed else "⏳"
        print(f"{status_icon} {task.title}: {task.description}")

# Создаем задачи
print("Создаем задачи...")
task1 = EngineeringTask('ПРИЕМ', 'Принять 3 сотрудников в инженерный отдел')
task2 = EngineeringTask('ОТЧЕТ', 'Сделать отчет по сотрудникам')
task3 = EngineeringTask('БОЛЬНИЧНЫЕ', 'Обработать данные по больничным за ноябрь')

# Отмечаем ДВЕ задачи как выполненные
print("Отмечаем задачи как выполненные...")
task1.is_completed = True  # ПРИЕМ - выполнен
task2.is_completed = True  # ОТЧЕТ - выполнен
# БОЛЬНИЧНЫЕ - остается невыполненной

tasks_list = [task1, task2, task3]

# Показываем разные варианты
show_tasks(PendingFilter().filter(tasks_list), "НЕВЫПОЛНЕННЫЕ ЗАДАЧИ")
show_tasks(CompletedFilter().filter(tasks_list), "ВЫПОЛНЕННЫЕ ЗАДАЧИ")

print("\n=== ПРОГРАММА ЗАВЕРШЕНА ===")