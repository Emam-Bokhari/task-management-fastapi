from pydantic import BaseModel

class UserSchema(BaseModel):
    name:str 
    user_name:str 
    password:str 
    email:str  
    is_active:bool=True
    is_deleted:bool=False 

class UserResponseSchema(BaseModel):
    id:int
    name:str 
    user_name:str 
    email:str
    is_active:bool 
    is_deleted:bool  