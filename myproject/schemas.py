from pydantic import BaseModel


class GameBase(BaseModel):
    title: str
    description: str | None = None


class GameCreate(GameBase):
    pass


class Game(GameBase):
    id: int
    platform_id: int
    is_installed: bool

    class Config:
        orm_mode = True


class PlatformBase(BaseModel):
    name: str


class PlatformCreate(PlatformBase):
    pass


class Platform(PlatformBase):
    id: int
    gamelist: list[Game] = []

    class Config:
        orm_mode = True
