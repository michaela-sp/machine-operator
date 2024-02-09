# machine_operator 

Welcome to _machine_operator_ - the cutting edge service that can create, delete and provide 
information about virtual machines. 

The first version (remember - primitive means first!) allows you to:  
- create machines with the following OS templates:
  - `the_always_broken_Windows`
  - `the_unsatisfactory_macOS`
  - `the_obsolete_Linux`
  - `the_never_known_ChromeOS`
- delete the machine based on machine id
- read information about machine based on machine id
- read information about all available machine records  


## Run the app for testing

Although we truly trust this backend, we are happy you will test it! 

Sadly, this backend needs to be run locally.

Here are the prerequisites:
    - Python 3.8 or newer
    - dependencies from the `requirements.txt` file

To run the application locally, run the `main.py` file. The application is set to run on localhost (127.0.0.1), port 8000.
Open your browser at `http://127.0.0.1:8000` to verify it's running by viewing the homepage.

## Documentation

Swagger UI is served at `/docs` E.g., `http://127.0.0.1:8000/docs` if run locally on the localhost 
with port 8000.

The specification of the service contains 4 endpoints:
  - `POST /machines/` - to create new machines based on selected `template` (see above) and optionally `custom_name`
  - `GET /machines/` - to list all machines
  - `GET /machines/{machine_id}` - to retrieve information about the given machine
  - `DELETE /machines/{machine_id}` - to delete the selected machine


_This humble application is written in [FastAPI framework](https://fastapi.tiangolo.com), 
a framework created by [Sebastian Ramirez](https://twitter.com/tiangolo/status/1281946592459853830?lang=cs)._
