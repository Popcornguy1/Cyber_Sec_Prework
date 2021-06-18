


def long(name1, name2, name3):
    if len(name1) > len(name2) and len(name3):
        return name1
    elif len(name2) > len(name3) and len(name1): 
        return name2
    elif len(name3) > len(name2) and len(name1): 
        return name3


big_name = long("Bruce Wayne","Naruto Uzamaki", "Tony Stark")

print(big_name)