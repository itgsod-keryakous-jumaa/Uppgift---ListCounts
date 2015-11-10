def sum(listofnumbers):
    if len(listofnumbers) == 0:
        raise ValueError

    result = 0
    for number in listofnumbers:
        result += number

    return result

  #  index=0
   # lenght= len(lisofnumbers)

    #while index < lenght:
     #   result=result + listofnumbers[index]
      #  index=+1

def min(listofnumbers):
    if len(listofnumbers) == 0:
        raise ValueError

    mini = None

    for number in listofnumbers:
        if mini is None or number < mini:
            mini = number

    return mini

