MiStay Events Developer API Documentation
-
This documentation will contain the details about the API end-points.
```
    1. /api/events/create/
    2. /api/events/delete/
    3. /api/events/public/
    4. /api/events/invited/
    5. /api/events/
    6. /api/events/register/
    7. /api/events/un-register/
    8. /api/events/invite/
    9. /api/events/registered/
```
The about end-points will be discussed one by one.

1 ```/api/events/create/```

    Method: POST
    Request: {
        "event_name": "Event from PostMan",
        "starts_on": "2019-12-03 12:12",
        "ends_on": "2019-12-04 12:12",
        "is_public": true,
        "users_limit": 123
    }
    Response: {
        "id":13,
        "event_name":"Event from PostMan",
        "starts_on":"2019-12-03 12:12",
        "ends_on":"2019-12-04 12:12",
        "users_limit":123,
        "is_public":true
    }
2 ```/api/events/delete/```

    Method: POST
    Headers: JWT Token
    Request: {
        "event_id": 10
    }
    Response: {
        "details":"Successfully Deleted"
    }

3 ```/api/events/public/```

    Method: GET
    Headers: None
    Request: None
    Response: [
        {
            "id": 2,
            "event_name": "ReactConf at Hyd",
            "starts_on": "2019-11-29T11:03:41Z",
            "ends_on": "2019-11-30T11:20:46Z",
            "users_limit": 25,
            "is_public": true
        }
    ]

4 ```/api/events/invited/```

    Method: GET
    Headers: JWT Token
    Request: None
    Response: [
        {
            "id": 2,
            "event_name": "ReactConf at Hyd",
            "starts_on": "2019-11-29T11:03:41Z",
            "ends_on": "2019-11-30T11:20:46Z",
            "users_limit": 25,
            "is_public": true
        }
    ]

5 ```/api/events/```

    Method: GET
    Headers: JWT Token
    Request: None
    Response: [
        {
            "id": 2,
            "event_name": "ReactConf at Hyd",
            "starts_on": "2019-11-29T11:03:41Z",
            "ends_on": "2019-11-30T11:20:46Z",
            "users_limit": 25,
            "is_public": true
        }
    ]
6 ```/api/events/register/```

    Method: POST
    Headers: JWT Token
    Request: {
        "event_id": 1
    }
    Response: [
        {
            "user":1,
            "event":4,
            "created_at":"2019-12-02T04:40:50.701471Z"
        }
    ]
7 ```/api/events/un-register/```

    Method: POST
    Headers: JWT Token
    Request: {
        "event_id": 1
    }
    Response: {
        "details": "You have un-registered for the event."
    }
8 ```/api/events/invite/```

    Method: POST
    Headers: JWT Token
    Request: {
        "event_id": 2,
        "user_id": 3
    }
    Response: {
        "details":"Successfully Invited"
    }
9 ```/api/events/registered/```

    Method: GET
    Headers: JWT Token
    Request: None
    Response: [
        {
            "user": 5,
            "event": {
                "id": 2,
                "event_name": "ReactConf at Hyd",
                "starts_on": "2019-11-29T11:03:41Z",
                "ends_on": "2019-11-30T11:20:46Z",
                "users_limit": 25,
                "is_public": true
            },
            "created_at": "2019-12-02T02:57:33.156986Z"
        }
    ]
    