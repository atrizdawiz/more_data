import Ad
import re
import boto3
import datetime
# Database
# java -D"java.library.path=./DynamoDBLocal_lib" -jar DynamoDBLocal.jar -sharedDb
dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")
table = dynamodb.Table('Ads')

# Initialize new Ad object
ad_object = Ad.Ad()
# Update it to latest ad entry. This should be scheduled in future versions.
ad_object.update()
ad_json = ad_object.toJSON()

# Check if it should be persisted
if ad_object.shouldBePersisted():
    table.put_item(
            Item={
                'ad_id': ad_object.ad_id,
                'ad_title': ad_object.ad_title,
                'ad_description': ad_object.ad_description,
                'ad_price': ad_object.ad_price,
                'ad_timestamp': str(datetime.datetime.now()).split('.')[0]
            }
        )
    print("Written to database: " + ad_json)
else:
    print("Ad does not look that interesting.")
    
print(ad_json)