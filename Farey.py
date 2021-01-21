def Farey(number:float, max:int = 100000, confirmation = True, error_messages:bool = True, logs:bool = False):
    """
    number: number for which a fraction is seek
    max: the boundary given to the denominator of the fraction (in order to avoid infinte loops)
    confirmation: if true, then a bool value will also be returned indicating if the numerical value is an approximation ar an exact fraction
    error_messages: prints a message in console in such cases where no fraction was found
    logs: prints in console every step of the process

    The algorithm returns a list with the first element being the numerator and the second element being the denominator.
    A boolean value is also returned, if the value is false then the fraction returned is just an approximate
    In case that no fraction is found (boundary passed) then the function returns None
    """
    #The number is split in integers and decimals in order to only work with the later  and get better precision
    number = str(number).split(".")
    if len(number) == 2:
        decimals = float("0." + number[1])
    else:
        decimals = 0
    if number[0] == "0" or number[0] == "":
        integers = 0
    else:
        integers = int(number[0])
    return __Farey(integers, decimals, max, confirmation, error_messages, logs)
    

def Farey_fracc(numerator:float, denominator:float, max:int = 100000, confirmation = True, error_messages:bool = True, logs:bool = False):
    """
    numerator: numerator of the fraction
    denominator: denominator of the fraction
    max: the boundary given to the denominator of the fraction (in order to avoid infinte loops)
    confirmation: if true, then a bool value will also be returned indicating if the numerical value is an approximation ar an exact fraction
    error_messages: prints a message in console in such cases where no fraction was found
    logs: prints in console every step of the process


    Use this function in order to use the alorithm with a fraction
    The algorithm returns a list with the first element being the numerator and the second element being the denominator.
    A boolean value is also returned, if the value is false then the fraction returned is just an approximate
    In case that no fraction is found (boundary passed) then the function returns None
    """
    whole = numerator // denominator
    decimal = (numerator - whole * denominator) / denominator
    return __Farey(whole, decimal, max, confirmation, error_messages, logs)
    

def __Farey(integers:int, decimals:float, max:int, confirmation, error_messages:bool, logs:bool):
        #The number is split in integers and decimals in order to only work with the later  and get better precision
    #as the sequences mandates, the first evaluated values are 0 and 1
    den_superior = 1
    nom_superior = 1
    nom_inferior = 0
    den_inferior = 1
    if decimals != 0 and decimals != 0.0:
        while True:
            new_nom = nom_superior + nom_inferior
            new_den = den_superior + den_inferior

            #logs
            if logs:
                #prints the evaluation
                print("{} / {} --> {} / {} <-- {} / {}".format(nom_inferior, den_inferior, new_nom, new_den, nom_superior, den_superior))
                #prints the changed fraction for the next cycle
                print("{} --> {}".format(new_nom / new_den, decimals))

            if decimals == (new_nom / new_den):
                #Result found
                if confirmation:
                    return __found_farey(new_nom, new_den, integers), True
                else:
                    return __found_farey(new_nom, new_den, integers)
                break
            elif decimals > (new_nom / new_den):
                nom_inferior = new_nom
                den_inferior = new_den
            elif decimals < (new_nom / new_den):
                nom_superior = new_nom
                den_superior = new_den

            #out of boundaries
            if new_den >= max:
                if error_messages:
                    print("No match found within the max boundaries")
                    print("{} + {}".format(integers, decimals))
                if confirmation:
                    return __found_farey(new_nom, new_den, integers), False
                else:
                    return __found_farey(new_nom, new_den, integers)
                break
    else:
        if confirmation:
            return __found_farey(0, 1, integers), True
        else:
            return __found_farey(0, 1, integers)    


def __found_farey(nom : int, den : int, integers : int):
    nom = nom + integers * den
    return [nom, den]
