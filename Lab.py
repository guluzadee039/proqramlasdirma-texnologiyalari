"""
Lab.py
İstifadəçidən rəqəmlərdən ibarət bir siyahı alır və arasından
cüt ədədləri ekrana çıxarır.
"""


def get_number_list():
    """İstifadəçidən vergüllə ayrılmış ədədlər alır, int list qaytarır."""
    raw = input("Ədədləri vergüllə ayırıb daxil edin (məs: 3,8,15,22,7): ")
    numbers = []
    for part in raw.split(","):
        part = part.strip()
        if not part:
            continue
        try:
            numbers.append(int(part))
        except ValueError:
            print(f"Xəbərdarlıq: '{part}' düzgün tam ədəd deyil, keçilir.")
    return numbers


def get_even_numbers(numbers):
    """Siyahıdan yalnız cüt ədədləri qaytarır."""
    return [n for n in numbers if n % 2 == 0]


def main():
    numbers = get_number_list()

    if not numbers:
        print("Heç bir düzgün ədəd daxil edilmədi.")
        return

    evens = get_even_numbers(numbers)

    print(f"\nDaxil edilən siyahı: {numbers}")
    if evens:
        print(f"Cüt ədədlər: {evens}")
    else:
        print("Siyahıda cüt ədəd yoxdur.")


if __name__ == "__main__":
    main()
