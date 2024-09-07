from collections import defaultdict

class AuctionHouse:
    
    def __init__(self , auction_house_json, region):
        self.auction_house_json =auction_house_json
        self.region = region
        self.sorted_data_by_item_id = self.sort_data_by_item_id(auction_house_json['auctions'])
        self.grouped_data_items = defaultdict(list)
        for entry in self.sorted_data_by_item_id:
            item_id = entry['item']['id']
            self.grouped_data_items[item_id].append(entry)
        # self.grouped_list_items = list(self.grouped_data_items.values())
    
    def sort_data_by_item_id(self, data):
        sorted_data = sorted(data, key=lambda x: x['item']['id'])
        return sorted_data
    
    def get_item_by_id(self, id):
        found_items = self.grouped_data_items.get(id, None)
        if found_items:
            print(found_items)
            return found_items
        else:
            print(f"Items id:{id} not found.")
    
    def create_items_object_list(self):
        self.Items_Object_list = [Items(item_id, group) for item_id , group in self.grouped_data_items.items()]
    
    
class Items:
    
    def __init__(self, item_id, list_items):
        self.id = item_id
        self.list_items = list_items
        
    def sort_data_price(self):
        pass