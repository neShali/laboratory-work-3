def move(n, source, target, auxiliary):
    if n == 1:
        print(f"Перенести диск 1 со стержня {source} на стержень {target}")
        return
    move(n - 1, source, auxiliary, target)
    print(f"Перенести диск {n} со стержня {source} на стержень {target}")
    move(n - 1, auxiliary, target, source)

def hanoi_tower(num_disks):
    if num_disks <= 0:
        print("Количество дисков должно быть больше нуля")
    else:
        move(num_disks, 1, 3, 2)

# Введите количество дисков
num_disks = int(input("Введите количество дисков: "))
hanoi_tower(num_disks)