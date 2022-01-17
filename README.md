# CotAPI

This is an API allowing for faster viewing and interaction with data harvested from the [COTI](https://explorer.coti.io/) platform.

***
## How to deploy

First you must clone the code using:

```bash
git clone git@github.com:SkinnyPigeon/cotapi.git
```

Now you can change into the newly created folder:

```bash
cd cotapi
```

It should now be ready to launch via Docker:

```bash
docker-compose up --build
```

If successful, three containers should be created and begin running

***
## Interactive Documentation

The api schema can be found at http://localhost:8000/openapi.json.

With the containers running, the interactive documentation can be found at http://localhost:8000/docs [^1]. **First-time users must call** http://localhost:8000/users/signup in order to create a user within the system. This user can then authenticate themselves by clicking on the ***Authorize*** button or any of the locks on the right hand of the end point name plates.

Once authenticated, the system is ready to save some transactions for later interaction. To achieve this, the user should call http://localhost:8000/transactions/update. This will call the COTI api and gather all of the transactions for the user's given address. They will then be saved to a MongoDB instance running in one of the other containers. This process takes a little while (~60 seconds). With the transactions saved, the user can now interact with their data via the following series of endpoints.

### /transactions/saved

This allows the user to view all of their saved transactions. By default, the end point selects the everything from the last 48 hours and presents it from most recent to oldest. These values can be changed to suit the user's needs

### /transactions/recent

This allows the user to select a finite number of transactions. It defaults to the most recent 3, however, the number can be changed as well as it being starting its results from the oldest records.

### /transactions/hash

This allows the user to search for a particular transaction by the transaction's hash

### /balance/outgoings

Performs a sum of all outgoings from the account over a given period. It defaults to from 01/01/1970 to the current moment, however, these can be changed to allow a specific periods to be covered.

### /balance/income

Performs a sum of all income from the account over a given period. It defaults to from 01/01/1970 to the current moment, however, these can be changed to allow a specific periods to be covered.

### /balance/

Performs a sum of all income, all outgoings, and the balance of these from the account over a given period. It defaults to from 01/01/1970 to the current moment, however, these can be changed to allow a specific periods to be covered.

***
## Scheduler
The daily scheduled call to the API takes place at Midnight. This is handled by the container **cron**. By default, this uses the values:

```bash
username: euan
password: password
```

Users can change these to their desired values in **DockerfileCall**. They should match the details for the user which is registered in the database. To change when the update occurs, users can edit the **crontab_file**. For instance, a user wishing for the database to be updated every 5 minutes would add the line:

```bash
*/5 * * * * source /root/.profile; /bin/bash /root/call_api.sh
```

***
## Notes

When not using the interactive documentation, a registered user should call the endpoint http://localhost:8000/token to retrieve a JWT. This can then be used in the headers of http requests with the format:

```json
{
    "Authorization": "Bearer ey128qjas9ad9suq...."
}
```



[^1]: More detailed documentation can be found at http://localhost:8000/redoc