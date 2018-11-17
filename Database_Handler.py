import Ad
import re
import boto3
import datetime

# Helper class to convert a DynamoDB item to JSON.

# Database
dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")
table = dynamodb.Table('Ads')

# Initialize new Ad object
ad_object = Ad.Ad()

# Update it to latest ad entry. This should be scheduled in future versions.
ad_object.update()

ad_json = ad_object.toJSON()

table.put_item(
        Item={
            'ad_id': ad_object.ad_id,
            'ad_title': ad_object.ad_title,
            'ad_description': ad_object.ad_description,
            'ad_price': ad_object.ad_price,
            'ad_timestamp': str(datetime.datetime.now()).split('.')[0]
        }
    )
    #add to db.
# Convert the updated object to JSON
# TODO, send ad_json to some database.