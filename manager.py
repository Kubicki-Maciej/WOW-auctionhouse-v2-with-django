from auction_house import AuctionHouse
from blizzard_api_connect import get_auction_data, get_auction_commodities_data

# get data
# data = get_auction_data('1084','eu')

data = get_auction_commodities_data('eu')

# AuctionHouse Object

AH_Object = AuctionHouse(data, 'eu')

AH_Object.get_item_by_id(222799)



# 222798 bolt