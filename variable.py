def get_summ(one, two, delimiter='&'):
    return str(one).upper() + str(delimiter).upper() + str(two).upper()

print(get_summ("Hello","World",delimiter="_ok_"))


