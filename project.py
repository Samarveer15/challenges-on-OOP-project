class RomanConverter:
    def __init__(self):
        self.roman_numerals = {
            1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L',
            90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'
        }

    def int_to_roman(self, num):
        roman_value = ''
        for value in sorted(self.roman_numerals.keys(), reverse=True):
            while num >= value:
                roman_value += self.roman_numerals[value]
                num -= value
        return roman_value

if __name__ == "__main__":
    number = int(input("Enter an integer: "))
    converter = RomanConverter()
    roman_numeral = converter.int_to_roman(number)
    print(f"The Roman numeral for {number} is {roman_numeral}")
