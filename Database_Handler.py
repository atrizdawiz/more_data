from __future__ import print_function # Python 2/3 compatibility
import Ad
import json
import test_client
import re
import boto3
import datetime
import decimal
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)
# Database start command
# java -D"java.library.path=./DynamoDBLocal_lib" -jar DynamoDBLocal.jar -sharedDb
dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")
table = dynamodb.Table('Ads')

# Initialize and update new Ad object
#ad_object = Ad.Ad()
#ad_object.update()

# Same but for testing
ad_object = test_client.test_client()

# Update routine¨
last_id = None
last_id = ad_object.ad_id
ad_object.update_test()

#Get latest item from database
try:
    response = table.get_item(
        Key={
            'ad_id': last_id,
            'ad_title': ad_object.ad_title
        }
    )
except ClientError as e:
    print(e.response['Error']['Message'])
else:
    item = response
    print("GetItem succeeded:")
    print(json.dumps(item, indent=4, cls=DecimalEncoder))

if True:
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
        print("Written to database: ")
    else:
        print("Ad does not look that interesting.")
else:
    print("Ad already in database")