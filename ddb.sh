!/bin/sh
cd $"c:\Program Files\dynamodb_local_latest\"
java -D"java.library.path=./DynamoDBLocal_lib" -jar DynamoDBLocal.jar -sharedDb