<h1 align="center">User Registration CRUD API</h1>

This is a simple Flask-based API for performing CRUD operations on a user registration table stored in an SQLite database.

# Requirements
To run this code on your local machine, you'll need the following dependencies installed:
<br>
* Python (version 3.6 or higher)
* Flask (install via pip: pip install Flask)

```python
pip install Flask
```
## Running the Code
1.  Clone this repository to your local machine:
```python
git clone https://github.com/your-username/user-registration-api.git
```
2.  Navigate to the project directory:
```python
cd user-registration-api
```
3.  Run the Flask application:
```python
python main.py
```
<br>
This will start the Flask server locally, and the API will be accessible at 

[http://localhost:5000](http://localhost:5000)

## Testing

I used an online api tester for CRUD operations. Can use postman too..
The one I use :
[https://reqbin.com/](https://reqbin.com/)

### Steps 
1. Open reqbin.
2. Set the request URL to one of the API endpoints (e.g., http://localhost:5000/register).
3. Choose the HTTP method (POST, GET, PUT, DELETE) depending on the operation you want to test.
4. Add request headers (if required).
5. If testing POST or PUT requests, provide request body in JSON format.
6. Send the request and observe the response.

## NOTE: 
Ensure to replace http://localhost:5000 with the appropriate URL if you're running the Flask server on a different port or if you're testing it on a remote server.


