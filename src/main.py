from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from src import models
# from .config import settings
from src.database import engine
from src.routers import post, user, auth, vote



# ------------------------------------------------------------------

# Create models
# models.Base.metadata.create_all(bind=engine)  # Creation is now handled by alembic


# create an instance of FastAPI
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#  -------------------------- Get path operations from routers folder----------------------------------

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
async def root():
    return {"message": "Hello World!"}



