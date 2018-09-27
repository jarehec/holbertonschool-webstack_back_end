# RESTful API - Users - endpoints

## Synopsis
This will be the second part of the RESTful API project: Expose User instance through a JSON API.  

### API
`GET /api/v1/status`  
Returns the status of the api.  
```{"status": "OK"}```  

`GET /api/v1/stats`  
Returns the number of users.  
```{"users": 42}```  

`GET /api/v1/users`  
Returns a list of users.  
```
[
   {
     "created_at": "2017-07-25 01:45:28",
     "email": "james@bond.com",
     "first_name": "james",
     "id": "bb0f5ee4-9c4e-45c5-b059-af8eb7ce488c",
     "last_name": "bond",
     "updated_at": "2017-07-25 01:45:28"
  }
]
```  

`GET /api/v1/users/<user_id>`  
Returns a user by their id.  

`DELETE /api/v1/users/<user_id>`  
Deletes a user by their id.  

`POST /api/v1/users`  
Creates a user.  
Parameters:
  * email [Required]
  * password [Required]
  * first_name
  * last_name  

'PUT /api/v1/users`
Updates user first and last name  
Parameters:
  * first_name
  * last_name  

### Models
* BaseModel
  * `id` (UUID4)
  * `created_at` (datetime)
  * `updated_at` (datetime)
  
* User(BaseModel)
  * `email` (str)
  * `first_name` (str)
  * `last_name` (str)
  * `password` (str)
 
#### Start application
```
jarecec@linux:~$ HBNB_YELP_MYSQL_USER=root HBNB_YELP_MYSQL_PWD=root HBNB_YELP_MYSQL_HOST=localhost HBNB_YELP_MYSQL_DB=hbtn_yelp_dev HBNB_API_HOST=0.0.0.0 HBNB_API_PORT=5050 python3 -m api.v1.app
```
## Authors
* Jared Heck
```
  ________________________/ O  \___/
 <888888888888888888888888_____/   \
 ```
