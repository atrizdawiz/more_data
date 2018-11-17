import Ad

# Initialize new Ad object
ad_object = Ad.Ad()

# Update it to latest ad entry
ad_object.update()

# Convert the updated object to JSON
ad_json = ad_object.toJSON()

print(ad_json)

# TODO, send ad_json to some database.