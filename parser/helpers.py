

def check_info_fullness(info_dict: dict):
    for _, value in info_dict.items():
        if value is None:
            return False

    return True


def combine_dicts(primary: dict, secondary: dict):
    for key, value in primary.items():
        if value is None:
            primary[key] = secondary[key]

    return  primary