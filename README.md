# Match Schedules

## Description
CRUD features to manage match schedules. 
- user will able to create new schedule from the web
- users will be able to edit the existing schedule
- user can delete schedule data
- user can see the list of existing schedule data

## Usage

### API List

Base URL
```bash
http://localhost:8000/
```

- #### API List

  - Get all data
    
    ```bash
    Method : GET
    localhost:<port>/rest/
    ```
  
  - Add new data
  
    ```bash
    Method : POST
    localhost:<port>/rest/<id>
    ```
  
  - Update data by 'id'
    
    ```bash
    Method : PUT
    localhost:<port>/rest/<id>
    ```
  
  - Delete data by 'id'
    
    ```bash
    Method : DELETE
    localhost:<port>/rest/<id>
    ```
  
- #### JSON Response
  
   ```json
  [
    {
      "schedule_name": "Bowling",
      "schedule_time": "Friday"
    },
    {
      "schedule_name": "Futsal",
      "schedule_time": "Friday"
    }
  ]
  ```
