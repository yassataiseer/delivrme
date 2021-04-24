# DlvrMe

## Note This project is now dysfunct
## View new API here https://github.com/yassataiseer/DlvrMe-API
## View Flutter frontend here https://github.com/yassataiseer/DlvrMe-Mobile

DlvrMe is a project made by Yassa Taiseer that is used to make delivering packages with a city easier
  - Users signup/login
  - They can then post an order worldwide and another user can drop it off somewhere else
  - Basically uber eats but anyone can deliver and make money
  - To see a demo of this project just download ```video.mp4```

### Tech Stack:

  - Flask(backend)
  - Google Maps Api
  - VanillaJs(frontend)
  - Html&CSS(frontend)
  - MySQL(Backend)



### Installation

DlvrMe requires the Google Maps Api download [here](https://developers.google.com/maps/documentation)
It also requires python 3
Install the dependencies and devDependencies and start the server.
#### Mac& Linux:
```sh
pip3 install requirements.txt
python3 flask_app.py
```

#### Windows:
```sh
pip install requirements.txt
python flask_app.py
```

### Environment variables
Before running you will need to setup environment variables in a file called .env
This will have all of your database and Api credentials
```
touch .env
```
In this file write the following:
|   |  |
| ------ | ------ |
| HOST | "YOU_DATA_BASE_HOST" |
| USER | "MYSQL_USERNAME" |
| PASSWORD | "YOUR_PASSWORD" |
| DATABASE | "DATA_BASE_NAME" |
| API_KEY | "YOUR-GOOGLE-API-KEY" |

### Building Database
DlvrMe runs on a MySQL databases
There is a need for two tables Users and Deliveries

#### User's Tables
The user's table will look like this:
|VALUE| TYPE  |
| ------ | ------ |
| Username | VARCHAR |
| Password | VARCHAR |
| ID_key | AUTO_INCREMENT_KEY |

#### Deliveries Database
| VALUE  | TYPE |
| ------ | ------ |
| Username | VARCHAR |
| Address | VARCHAR |
| Latitude | FLOAT |
| Longitude | FLOAT |
| Item | VARCHAR |
| Price | FLOAT |
| User_info | VARCHAR |
| ID_key | AUTO_INCREMENT_KEY |



#### Option 2(Easier route):
You can also run ```database_setup.sql``` in Mysql this is much easier but may now work on MacOs/Linux
