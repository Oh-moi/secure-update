# NEW

<img src="https://github.com/Oh-moi/kaspersky_learning/blob/main/ARC.png?raw=true" width="1000">

Сценарии (подробнее https://github.com/Oh-moi/kaspersky_learning/wiki/dz1)

**Позитивный сценарий 1 (запрос текущих данных)**

1. Инициализация (включение оборудования и КУМО)
```
### PUSH DATA FROM HARDWARE
POST http://localhost:5003/ingest HTTP/1.1
content-type: application/json
#auth: very-secure-token

[
    {
        "param_name": "temperature",
        "param_units": "C",
        "param_value": 25
    },
        {
        "param_name": "units_per_hour",
        "param_units": "Units",
        "param_value": 1200
    },
        {
        "param_name": "working_machines_per_hour",
        "param_units": "Machines",
        "param_value": 9
    },
        {
        "param_name": "conveyor",
        "param_units": "Boolean",
        "param_value": 0
    }
]
```

2.  Запрос идентификации и аутентификации, запрос на действие: просмотр текущих данных. 
```
### GOOD REQUEST FOR GET DATA
POST http://localhost:5005/auth_and_action HTTP/1.1
content-type: application/json

{
    "login": "Mary", 
    "password": "mary_pass",
    "action": "get_data"
}
```
Получение токена сессии (id)
```
HTTP/1.1 200 OK
Server: Werkzeug/2.2.3 Python/3.10.6
Date: Sun, 12 Mar 2023 10:12:18 GMT
Content-Type: application/json
Content-Length: 97
Connection: close

{
  "id": "5391eb2d-f59d-4ad3-a067-dc4b3fecf245",
  "operation": "new user`s request received"
}
```
Запрос результата по предыдущему запросу.
```
### GET ACTION RESULT 
GET http://localhost:7003/get HTTP/1.1
auth: 5391eb2d-f59d-4ad3-a067-dc4b3fecf245
```
3. Получение результата запроса (предоставление доступа)
```
HTTP/1.1 200 OK
Server: Werkzeug/2.2.3 Python/3.10.6
Date: Sun, 12 Mar 2023 10:12:59 GMT
Content-Type: application/json
Content-Length: 542
Connection: close

[
  {
    "action": "get_data",
    "event": "successful user Ident & Auth",
    "role": "user",
    "source_id": "5391eb2d-f59d-4ad3-a067-dc4b3fecf245"
  },
  {
    "param_name": "temperature",
    "param_units": "C",
    "param_value": 25
  },
  {
    "param_name": "units_per_hour",
    "param_units": "Units",
    "param_value": 1200
  },
  {
    "param_name": "working_machines_per_hour",
    "param_units": "Machines",
    "param_value": 9
  },
  {
    "param_name": "conveyor",
    "param_units": "Boolean",
    "param_value": 0
  }
]
```




**Позитивный сценарий 2 (запрос алертов)**

1. Инициализация (включение оборудования и КУМО)
```
### PUSH DATA FROM HARDWARE
POST http://localhost:5003/ingest HTTP/1.1
content-type: application/json
#auth: very-secure-token

[
    {
        "param_name": "temperature",
        "param_units": "C",
        "param_value": 25
    },
        {
        "param_name": "units_per_hour",
        "param_units": "Units",
        "param_value": 1200
    },
        {
        "param_name": "working_machines_per_hour",
        "param_units": "Machines",
        "param_value": 9
    },
        {
        "param_name": "conveyor",
        "param_units": "Boolean",
        "param_value": 0
    }
]
```
2.  Запрос идентификации и аутентификации, запрос на действие: просмотр алертов. 

```
### GOOD REQUEST FOR GET ALERT
POST http://localhost:5005/auth_and_action HTTP/1.1
content-type: application/json

{
    "login": "Mary", 
    "password": "mary_pass",
    "action": "get_alert"
}
```
Получение токена сессии (id)
```
HTTP/1.1 200 OK
Server: Werkzeug/2.2.3 Python/3.10.6
Date: Sun, 12 Mar 2023 10:14:16 GMT
Content-Type: application/json
Content-Length: 97
Connection: close

{
  "id": "59a175af-24e9-4c60-9349-d7a233df3782",
  "operation": "new user`s request received"
}
```
Запрос результата по предыдущему запросу
```
### GET ACTION RESULT 
GET http://localhost:7003/get HTTP/1.1
auth: 59a175af-24e9-4c60-9349-d7a233df3782
```
3. Получение результата запроса (предоставление доступа)
```
HTTP/1.1 200 OK
Server: Werkzeug/2.2.3 Python/3.10.6
Date: Sun, 12 Mar 2023 10:14:45 GMT
Content-Type: application/json
Content-Length: 498
Connection: close

[
  {
    "action": "get_alert",
    "event": "successful user Ident & Auth",
    "role": "user",
    "source_id": "59a175af-24e9-4c60-9349-d7a233df3782"
  },
  {
    "_event": "broken machines",
    "_source_id": "996e76d5-517f-42d9-bc95-3087e8b57eb7",
    "working_machines_per_hour_threshold": 10,
    "working_machines_per_hour_value": 9
  },
  {
    "_event": "conveyor off",
    "_source_id": "996e76d5-517f-42d9-bc95-3087e8b57eb7",
    "conveyor_threshold": 1,
    "conveyor_value": 0
  }
]
```

**Позитивный сценарий 3 (неправомерный запрос алертов)**

1. Инициализация (включение оборудования и КУМО)
```
### PUSH DATA FROM HARDWARE
POST http://localhost:5003/ingest HTTP/1.1
content-type: application/json
#auth: very-secure-token

[
    {
        "param_name": "temperature",
        "param_units": "C",
        "param_value": 25
    },
        {
        "param_name": "units_per_hour",
        "param_units": "Units",
        "param_value": 1200
    },
        {
        "param_name": "working_machines_per_hour",
        "param_units": "Machines",
        "param_value": 9
    },
        {
        "param_name": "conveyor",
        "param_units": "Boolean",
        "param_value": 0
    }
]
```
2.  Запрос идентификации и аутентификации, запрос на действие: неправомерный просмотр алертов. 
```
### BAD REQUEST FOR GET ALERT
POST http://localhost:5005/auth_and_action HTTP/1.1
content-type: application/json

{
    "login": "Kate", 
    "password": "kate_pass",
    "action": "get_alert"
}
```
Получение токена сессии (id)
```
HTTP/1.1 200 OK
Server: Werkzeug/2.2.3 Python/3.10.6
Date: Sun, 12 Mar 2023 10:16:05 GMT
Content-Type: application/json
Content-Length: 97
Connection: close

{
  "id": "bc208960-97f3-43da-bfd5-975265182dce",
  "operation": "new user`s request received"
}
```
Запрос результата по предыдущему запросу
```
### GET ACTION RESULT 
GET http://localhost:7003/get HTTP/1.1
auth: bc208960-97f3-43da-bfd5-975265182dce
```


3. Получение результата запроса (отказ в предоставлении доступа)
```
HTTP/1.1 200 OK
Server: Werkzeug/2.2.3 Python/3.10.6
Date: Sun, 12 Mar 2023 10:16:31 GMT
Content-Type: application/json
Content-Length: 202
Connection: close

[
  {
    "action": "get_alert",
    "event": "successful admin Ident & Auth",
    "role": "admin",
    "source_id": "bc208960-97f3-43da-bfd5-975265182dce"
  },
  {
    "Message": "Access denied"
  }
]
```

**Позитивный сценарий 4 (запрос на обновление)**

1. Инициализация (получение данных от сервера обновлений)
```
### PUSH UPDATE FROM SERVER
POST http://localhost:5009/push_update HTTP/1.1
content-type: application/json
auth: very-secure-token

{
    "version": 1.8
}
```
2.  Запрос идентификации и аутентификации, запрос на действие: обновление ПО. 
```
### GOOD REQUEST FOR UPDATE
POST http://localhost:5005/auth_and_action HTTP/1.1
content-type: application/json

{
    "login": "Kate", 
    "password": "kate_pass",
    "action": "get_update"
}
```
Получение токена сессии (id)
```
HTTP/1.1 200 OK
Server: Werkzeug/2.2.3 Python/3.10.6
Date: Sun, 12 Mar 2023 10:17:31 GMT
Content-Type: application/json
Content-Length: 97
Connection: close

{
  "id": "ba760bb7-e306-4d6c-8f00-9e25547c55dc",
  "operation": "new user`s request received"
}
```
Запрос результата по предыдущему запросу

```
### GET ACTION RESULT 
GET http://localhost:7003/get HTTP/1.1
auth: ba760bb7-e306-4d6c-8f00-9e25547c55dc
```

3. Получение результата запроса (Обновление ПО)
```
HTTP/1.1 200 OK
Server: Werkzeug/2.2.3 Python/3.10.6
Date: Sun, 12 Mar 2023 10:17:50 GMT
Content-Type: application/json
Content-Length: 191
Connection: close

[
  {
    "action": "get_update",
    "event": "successful admin Ident & Auth",
    "role": "admin",
    "source_id": "ba760bb7-e306-4d6c-8f00-9e25547c55dc"
  },
  {
    "version": 1.8
  }
]
```
**Позитивный сценарий 5 (предоставление неверного пароля)**
1.  Запрос идентификации и аутентификации, запрос на действие: запрос алертов. 
```
### GOOD REQUEST FOR GET ALERT
POST http://localhost:5005/auth_and_action HTTP/1.1
content-type: application/json

{
    "login": "Mary", 
    "password": "mary_pass!@#$%^&",
    "action": "get_alert"
}
```

Получение токена сессии (id)

```
HTTP/1.1 200 OK
Server: Werkzeug/2.2.3 Python/3.10.6
Date: Sun, 12 Mar 2023 11:37:26 GMT
Content-Type: application/json
Content-Length: 97
Connection: close

{
  "id": "97863be2-c58a-4e8c-9488-0e23fcf71a15",
  "operation": "new user`s request received"
}
```


Запрос результата по предыдущему запросу

```
### GET ACTION RESULT 
GET http://localhost:7003/get HTTP/1.1
auth: 97863be2-c58a-4e8c-9488-0e23fcf71a15
```

2. Получение результата запроса (Аутентификация не пройдена)

```
HTTP/1.1 200 OK
Server: Werkzeug/2.2.3 Python/3.10.6
Date: Sun, 12 Mar 2023 11:37:48 GMT
Content-Type: application/json
Content-Length: 152
Connection: close

[
  {
    "action": "get_alert",
    "event": "failure Ident & Auth",
    "role": "none",
    "source_id": "97863be2-c58a-4e8c-9488-0e23fcf71a15"
  }
]
```






## Роли пользователей


| Действие | Администратор | Пользователь |
| ------------- | ------------- | ------------- |
| Предоставление данных от оборудования | - | + |
| Предоставление данных о критических событиях | - | + |
| Обновление версии ПО | + | - |
| Пользователи | Kate | Mary |











# Secure update

## Disclaimer 

This is a demo project and shall not be used in production.
The code is distributed under MIT license (see the LICENSE file).

## Purpose

This is an example of update procedure hardening by using "Security monitor" pattern: all cross-servie requests go through the Monitor service.
The Monitor checks whether particular request is authorized and valid, then delivers it to destination service or drops it without further processing.

## Running the demo

There are two main options for running the demo:
- local (using local development environment), then there shall be installed python (tested with version 3.8) with pip and pipenv, also having *make* tool is recommended
- containerized (using docker containers)

In any case there shall be docker-compose locally available - at least for running message broker (Kafka).

### Running complete demo in containerized mode

execute in VS Code terminal window either
- _make run_
- or _docker-compose up_

then open the requests.rest file in Visual Studio Code editor. If you have the REST client extention installed, you will see 'Send request' active text above GET or POST requests, you can click on it.

If you click on the application GET link, you shall see in the Response window (will open automatically) the following:

```
HTTP/1.1 200 OK
Server: Werkzeug/2.2.2 Python/3.8.13
Date: Wed, 10 Aug 2022 08:23:40 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 39
Connection: close

Hello World! Application version 1.0.3u
```

##### Update demo

Run the POST request in manager section of requests.rest file, then if all services are up and running the following will happen:
- in the output window something like this will appear:
```
HTTP/1.1 200 OK
Server: Werkzeug/2.2.2 Python/3.8.13
Date: Wed, 10 Aug 2022 08:25:33 GMT
Content-Type: application/json
Content-Length: 86
Connection: close

{
  "id": "5b418446-39f2-456b-bef4-99ff347b1748",
  "operation": "update requested"
}

```

- update process will happen and once complete (within a few seconds) the next request in the application section will return
```
HTTP/1.1 200 OK
Server: Werkzeug/2.2.2 Python/3.8.13
Date: Wed, 10 Aug 2022 08:29:38 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 39
Connection: close

Hello World! Application version 1.0.4b
```

The application version will be updated from 1.0.3u to 1.0.4b. This is expected behavior.

##### Changing the application

The application file update is stored in file_server/data folder and is called app-update.py. The data folder is mounted as a volume in the file_server container, so any changes of the file will be immediately available to the running container.

To update the running application with own version of the file one shall do the following:

1. edit the app-update.py file
2. in the get update digest section of requests.rest file send the GET request, the result will look like the following
```
HTTP/1.1 200 OK
Server: Werkzeug/2.2.2 Python/3.8.13
Date: Wed, 10 Aug 2022 08:35:36 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 86
Connection: close

68b7d62551d332e395d2c302fc654d45cf836d576da628a06805d19113a89fea sha256 app-update.zip
```
3. copy the sha256 digest (in the example above it is 68b7d62551d332e395d2c302fc654d45cf836d576da628a06805d19113a89fea) and paste in the update POST request in the manager section of requests.rest, see the digest field:
```
POST http://localhost:6000/update HTTP/1.1
content-type: application/json
auth: very-secure-token

{
    "url":"http://file_server:6001/download-update/app-update.zip", 
    "target": "app", 
    "digest": "68b7d62551d332e395d2c302fc654d45cf836d576da628a06805d19113a89fea", 
    "digest_alg": "sha256"
}
```
4. send the modified POST request, once the update is done (again a few seconds might be required, see the docker-compose logs ouptut), the final lines shall contain something like
```
app_with_updater_1  | [info] handling event 9b66376c-461f-41de-bd58-d224d9782cc3, storage->updater: blob_content
app_with_updater_1  | [info]===== EXECUTING UPDATE 9b66376c-461f-41de-bd58-d224d9782cc3 ====
app_with_updater_1  | Archive:  tmp/9b66376c-461f-41de-bd58-d224d9782cc3
app_with_updater_1  |   inflating: ../app/app.py           
app_with_updater_1  | [info] update result code 0
```
5. send the application GET request and observe the updated application output


#### Troubleshooting

- if kafka or zookeeper containers don't start, make sure you don't have containers with the same name. If you do, remove the old containers and run the demo again.
