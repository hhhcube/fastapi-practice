from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import func

from typing import List, Optional

from .. import models, schemas, oauth2
from .. database import get_db

# ---------------------------- End Imports --------------------------------------------


router = APIRouter(
    prefix="/posts",
    # This allows you to group path operations in RapidAPI docs
    tags=["Posts"])



# ------------------------- Path Operations -------------------------------------------------
# Add response model to perform validation
# @router.get("/")
# @router.get("/", response_model=List[schemas.Post])
@router.get("/", response_model=List[schemas.PostOut])
def get_posts(
    db: Session = Depends(get_db), 
    current_user: int = Depends(oauth2.get_current_user),
    # building query parameters, called in posts
    limit: int = 7, skip: int = 0, search: Optional[str] = ""
):
     
    print(limit)

    # posts = db.query(models.Post).filter(
    #         models.Post.title.contains(search)).limit(limit).offset(skip).all()
    
    posts = db.query(models.Post, func.count(models.Votes.post_id).label("votes")).join(
        models.Votes, models.Votes.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(
            models.Post.title.contains(search)).limit(limit).offset(skip).all()
    print("type")

    return posts




@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post) 
def create_posts(
    post: schemas.PostCreate, 
    db: Session = Depends(get_db), 
    current_user: schemas.UserOut = Depends(oauth2.get_current_user)
):
    
    new_post = models.Post(owner_id=current_user.id, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post




  
@router.get("/{id}", response_model=schemas.PostOut) # validation with pydantic "id: int"
def get_post(id: int, 
             db: Session = Depends(get_db), 
             current_user: schemas.UserOut = Depends(oauth2.get_current_user)
):
    
    # post = db.query(models.Post).filter(models.Post.id == id).first()

    post = db.query(models.Post, func.count(models.Votes.post_id).label("votes")).join(
        models.Votes, models.Votes.post_id == models.Post.id, isouter=True).group_by(models.Post.id == id).first()
    
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")
    
    return post




@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT) # When you delete you want to send the 204 status code
def delete_post(id: int, 
                db: Session = Depends(get_db), 
                current_user: schemas.UserOut = Depends(oauth2.get_current_user)
):
   
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with id {id} does not exist")

    if post.owner_id != current_user.id: # type: ignore
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, 
                                detail="Not authorized to perform requested action")
    
    post_query.delete(synchronize_session=False)
    db.commit()
    
       
    return Response(status_code=status.HTTP_204_NO_CONTENT) # Need to send 204 whenever we delete from database







@router.put("/{id}", response_model=schemas.Post)
def update_post(id: int, 
                updated_post: schemas.PostCreate, 
                db: Session = Depends(get_db), 
                current_user: schemas.UserOut = Depends(oauth2.get_current_user)):
 
    post_query = db.query(models.Post).filter(models.Post.id == id)
    
    post = post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} does not exist")
  

    if post.owner_id != current_user.id: # type: ignore
        
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="not authorized to perform requested action")
    
    post_query.update(updated_post.dict(), synchronize_session=False) # type: ignore
    db.commit()

    return post_query.first()

# ----------------------------- Path opertions End -------------------
