MiStay Events Developer API Documentation
-
This documentation will contain the details about the API end-points.
To see the live demo, access below links/

Frontend UI:
https://events.therkv.tech/
   
Backend UI:
https://mistay-events.herokuapp.com/

GitHub Repo:
https://github.com/praveenyen/events-mistay/

`Credentials: username=admin, password=admin`

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
    10. /api/user/register/
    11. /api/auth/jwt/
```
The about end-points will be discussed one by one.

1 ```/api/events/create/```

    Method: POST
    Headers: JWT Token
    Description: This end-point is use to create event, Only authorized user
                can create events. JWT Token should be passed.
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
    Description: This end-point is use to delete event, Only authorized user
                can delete events. JWT Token should be passed.
                Inorder to delete an event, the requested user should be owner
                of the event.
    Request: {
        "event_id": 10
    }
    Response: {
        "details":"Successfully Deleted"
    }

3 ```/api/events/public/```

    Method: GET
    Headers: None
    Description: This end-point is used to get the public events, any user
                can view public events.
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
    Description: This end-point is used to get the events, which he got invitations.
                , Only authorized user can get the events.
                JWT Token should be passed.
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
    Description: This end-point is used to the events, which was created by him.
                JWT Token should be passed.
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
    Description: This end-point is used to create event, Only authorized user
                can create events. 
                JWT Token should be passed.
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
    Description: This end-point is used to de-register to the event.
                Only authorized user can de-register to the event.
                JWT Token should be passed.
    Request: {
        "event_id": 1
    }
    Response: {
        "details": "You have un-registered for the event."
    }
8 ```/api/events/invite/```

    Method: POST
    Headers: JWT Token
    Description: This end-point is used to send invitation to the event.
                Only owner of the event can send invites.
                JWT Token should be passed.
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
    Description: This end-point is used to get the registered events, Only 
                authorized user can get the events. JWT Token should be passed.
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
10 ```/api/user/register/```

    Method: POST
    Headers: None
    Description: This end-point is used to create user.
    Request: {
        "username": "",
        "firstname": "",
        "lastname": "",
        "email": "",
        "password": ""
    }
    Response: {
        "details":"Successfully Registered"
    }
11 ```/api/auth/jwt/```

    Method: POST
    Headers: None
    Description: This end-point is used to login to the system.
    Request: {
        "username": "username",
        "password": "password"
    }
    Response: {
    "token": "token",
    "user_id": 1,
    "user_name": "username"
}
