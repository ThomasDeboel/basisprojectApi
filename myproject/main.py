from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import os
import crud
import models
import schemas
from database import SessionLocal, engine

print("We are in the main.......")
if not os.path.exists('.\sqlitedb'):
    print("Making folder.......")
    os.makedirs('.\sqlitedb')

print("Creating tables.......")
models.Base.metadata.create_all(bind=engine)
print("Tables created.......")

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/platforms/", response_model=schemas.Platform)
def create_platform(platforms: schemas.PlatformCreate, db: Session = Depends(get_db)):
    db_platform = crud.get_program_by_name(db, name=platforms.name)
    if db_platform:
        raise HTTPException(status_code=400, detail="Platform name already exist")
    return crud.create_platform(db=db, platform=platforms)


@app.get("/platforms/", response_model=list[schemas.Platform])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    platforms = crud.get_platforms(db, skip=skip, limit=limit)
    return platforms


@app.get("/platforms/{platform_id}", response_model=schemas.Platform)
def read_user(platform_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_program(db, platform_id=platform_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Platform not found")
    return db_user


@app.post("/platforms/{platform_id}/games/", response_model=schemas.Game)
def create_item_for_user(
    platform_id: int, game_id: schemas.GameCreate, db: Session = Depends(get_db)
):
    return crud.create_platform_game(db=db, game=game_id, platform_id=platform_id)


@app.get("/games/", response_model=list[schemas.Game])
def read_games(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    games = crud.get_games(db, skip=skip, limit=limit)
    return games
