def ErrorMessage(num: int) -> str:
    if num == 1:
        return color.RED + color.BOLD + '####################################################\n'+\
        '#   Wrong input! Please enter number from 1 to 4   #\n' +\
        '####################################################' + color.END
    elif num == 2:
        return color.RED + color.BOLD + '##########################################\n'+\
               '#   Wrong input! Please enter a number   #\n'+\
              '##########################################' + color.END
    elif num == 3:
        return color.RED + color.BOLD + '#############################################\n'+\
               '#   Wrong input! Please enter digit 1 or 2  #\n'+\
               '#############################################' + color.END