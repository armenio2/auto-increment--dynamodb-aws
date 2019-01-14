# auto-increment--dynamodb-aws

This project can fix logic problem in auto increment in dynamodb or other non relational database.

<!--![alt text](https://i.imgur.com/gWZf41Z.jpg)-->

## Getting Started

``` 
-git clone https://github.com/armenio2/auto-increment--dynamodb-aws.git

```

##### TO START DYNAMO LOCAL
``` 
-winzip dynamo
-java -D"java.library.path=./DynamoDBLocal_lib" -jar DynamoDBLocal.jar

```

### TO CREATE TABLE
``` 
-pip install
-python createTable.py

```

### TO INSERT TABLE
``` 
-python insertTable.py

```

### TO GET TABLE
``` 
-python getTable.py

```

## Obs

```
-Ever u go test, delete dynamo and winzip a new dynamo
-I need finish this project add get and put table in btn!!
-Open Issue if u find bug, rember u need clone project, start dynamo, create table, insert table, and get table, next u can open html to test btn.
```

## Built With

* [HTML5]
* [PYTHON]
* [JAVASCRIPT]
* [BOTO3]
* [FLASK]
* [DYNAMODB]

## Contributing

https://docs.aws.amazon.com/pt_br/amazondynamodb/latest/developerguide/DynamoDBLocal.DownloadingAndRunning.html

https://docs.aws.amazon.com/pt_br/amazondynamodb/latest/developerguide/GettingStarted.Python.01.html

https://docs.aws.amazon.com/pt_br/amazondynamodb/latest/developerguide/SQLtoNoSQL.WriteData.html