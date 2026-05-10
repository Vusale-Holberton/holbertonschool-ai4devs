def find_average(numbers):
    # Bu funksiya siyahının ortalamasını tapır
    # Amma sıfıra bölmə xətası ola bilər
    total = sum(numbers)
    count = len(numbers)
    return total / count

print(find_average([])) # Boş siyahı xəta verəcək