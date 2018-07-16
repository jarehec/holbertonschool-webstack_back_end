# RESTful API - Users - model

## Synopsis
This will be the first part of the RESTful API project: User model with storage in MySQL.

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
 
 ### Methods
 * BaseModel
   * `def __init__(self):` initializes `id`, `created_at`, and `updated_at`
 
 * User(BaseModel)
   * `def display_name(self):` shows the users name or email if there is no name
   * `def is_valid_password(self, pwd):` checks is the value passed is the user's password
   * `def password(self, value)` sets the password to the md5 encrypted value of `value` (very insecure)
 

#### Running tests
```
jarecec@linux:~$ HBNB_YELP_MYSQL_USER=root HBNB_YELP_MYSQL_PWD=root \
HBNB_YELP_MYSQL_HOST=localhost HBNB_YELP_MYSQL_DB=hbtn_yelp_test \
python3 -m unittest discover tests
```
## Authors
* Jared Heck
```
  ________________________/ O  \___/
 <888888888888888888888888_____/   \
 ```
