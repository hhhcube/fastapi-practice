git init 
git add README.md 
git commit -m "first commit" 
git branch -M main 
git remote add origin <repo url>
git push -u origin main 


Make a request in the console:

fetch('http://localhost:8000/').then(res => res.json()).then(console.log)

pip install -r requirments.txt

venv\Scripts\activate.bat
deactivate
ctrl/shft/p 
    enter interpeter path powershell
     ./venv/scripts/python 

pip freeze (show all dependencies)

start server---
name of file <>:name of fast API instance
    uvicorn main:app
    uvicorn main:app --reload

When accesing file in a pacakage you write using the folder name <src> followed with dot notation 
uvicorn src.main:app --reload


Make use of Pydantic to define what our scheme should look like and validation.

Create --- POST -- /posts -- @app.post("/posts")
Read --- GET -- /posts/:id -- @app.get("/posts/{id}")
Read --- GET -- /posts -- @app.get("/posts")
Update --- PUT/PATCH -- /posts/:id -- @app.post("/posts/{id}")
Delete --- DELETE -- /posts/:id -- @app.post("/posts/{id}")

WE should always raise HTTPException
Anytime we create something we should send back a 201
Anytime we delete something we should send back a 204
Anytime we cant find something we should send back a 404

A package is nothing more than a folder with a dummy file __init__.py

Documentation:
http://127.0.0.1:8000/redoc
http://127.0.0.1:8000/doc


Authentication:
Two types of Authentication
1. Session based, we store something on our backend server (our API in this case) to track wether a user is logged in.
There will be some sort of informaton to keep track of whether or not a user is logged in, adn when the user has logged out.

2. JWT token Authentication -  it is stateless. There is nothing on our backend, there is nothing on our API, there is nothing in our database 
that keeps track or stores some kind of information on whether or not a user is logged out or in. The token itself is stored on the front end
and that keeps track of whther or not a user is logged in or not.

JWT token contains:
HEADER: {"alg": "HS256", "typ": JWT}
PAYLOAD: {"<whatevery you want returned to client": "data", "<return value>": "data"},
VERIFY SIGNATURE: HMACSHA256(base64UrlEncode(header) + "." + base64UrlEncode(payload), <your-256-bit-secret>) secret base64 encoded 
eg. ggygyygkgugh767568tygt87686g.eyugkggbkjkhhggbkjggugukjhbjkhjkhuhgukhbjkhjkhhhnjh.Sf12Kyghbh78gkuohjiohu89ybljy8nk_adxdQ766tyfvhygh

No encryption, secret is there only for data integrity. 
***************Secret only resides on our API server, no one does or should have acces to it!!!!
Anybody can see the data of a token, anybody can change the data of a token they just can't generate a brand new signature becaue they don't ahve access to the secret.






