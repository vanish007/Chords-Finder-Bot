def ErrorMessage(num: int) -> str:
    if num == 1:
        print(color.RED + color.BOLD + '####################################################')
        print('#   Wrong input! Please enter number from 1 to 4   #')
        print('####################################################' + color.END)
    elif num == 2:
        print(color.RED + color.BOLD + '##########################################')
        print('#   Wrong input! Please enter a number   #')
        print('##########################################' + color.END)
    elif num == 3:
        print(color.RED + color.BOLD + '#############################################')
        print('#   Wrong input! Please enter digit 1 or 2  #')
        print('#############################################' + color.END)