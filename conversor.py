from decimal import Decimal

def to_readable(bytes) -> str:
    KB = Decimal(1024)
    MB = Decimal(KB ** 2)  # 1,048,576
    GB = Decimal(KB ** 3)  # 1,073,741,824
    TB = Decimal(KB ** 4)  # 1,099,511,627,776
    PB = Decimal(KB ** 5)  # 1,125,899,906,842,624
    EB = Decimal(KB ** 6)  # 1.152921504606847e+18
    ZB = Decimal(KB ** 7)  # 1.1805916207174113e+21
    YB = Decimal(KB ** 8)  # 1.2089258196146292e+24

    if bytes < KB:
        return '{0:.2f} bytes'.format(bytes)
    elif KB <= bytes < MB:
        return '{0:.2f} KB'.format(bytes/KB)
    elif MB <= bytes < GB:
        return '{0:.2f} MB'.format(bytes/MB)
    elif GB <= bytes < TB:
        return '{0:.2f} GB'.format(bytes/GB)
    elif TB <= bytes < PB:
        return '{0:.2f} TB'.format(bytes/TB)
    elif PB <= bytes < TB:
        return '{0:.2f} PB'.format(bytes/PB)
    elif EB <= bytes < PB:
        return '{0:.2f} EB'.format(bytes/EB)
    elif ZB <= bytes < EB:
        return '{0:.2f} ZB'.format(bytes/ZB)
    else:
        return '{0:.2f} YB'.format(bytes/YB)