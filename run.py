# from parser import driver
import parser
from parser import get_lot_images
from parser.helpers import check_info_fullness, combine_dicts
from time import sleep



# plates = [
#     'KA8330EK',
#     'KA0905CB',
#     'KA8334EK',
#     'AE1196KM',
#     'KA0505CB',
#     'KA8234EK',
#     'AE1296KM',
#     'KA0515CB',
#     'KA7234EK',
#     'MACIK'
# ]
#
#
# for p in plates:
#     # sleep(3)
#     result = parser.get_plates_info(p)
#     if not check_info_fullness(result):
#         additional_data = parser.get_plates_info_mtsbu(p)
#         result = combine_dicts(result, additional_data)
#         # sleep(1)
#
#     print(result)

# if __name__ == "__main__":
#     parser.get_google_images('JN1CV6EL7EM131837')




