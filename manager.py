from auction_house import AuctionHouse
from blizzard_api_connect import get_auction_data, get_auction_commodities_data
from timer import my_timer

# data = get_auction_data('1084','eu')

data = get_auction_commodities_data('eu')

# AuctionHouse Object

AH_Object = AuctionHouse(data, 'eu')

AH_Object.get_item_by_id(222799)

bolt = AH_Object.get_item_by_id(222799)

for key in AH_Object.grouped_data_items:
    AH_Object.grouped_data_items =  sorted(AH_Object.grouped_data_items[key], key=lambda x: x['unit_price'])

# 222798 bolt rank 1

