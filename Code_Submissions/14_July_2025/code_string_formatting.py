# String Formatting H.W | 14th July 2025
def main() -> None:
    num : int = 999999999999
    num1 : int = 999.12345678
    num3 : int = 78

    print(f'{num:,}') # output: 999,999,999,999
    print(f'{num1:,.2f}') # output: 999.12
    print(f'{num3:09}') # output: 000000078

main()