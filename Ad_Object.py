import get_first
import json
class Ad_Object:
    """ AdObject class represents the interesting ad. """

    def __init__(self):
        """ Create a new point at the origin """
        self.ad_title = get_first.ad_title
        self.ad_description = get_first.ad_description
        self.ad_price = get_first.ad_price
        #self.ad_image_url = get_first.ad_image_url
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

ad_object = Ad_Object()
print(ad_object.toJSON())