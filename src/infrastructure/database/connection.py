from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from typing import Optional
import os

class MongoConnection:
    """
    Responsible only for::
    - Opening the connection
    - Exposing the database
    - Closing the connection
    """

    def __init__(self) -> None:
        self.__client: Optional[AsyncIOMotorClient] = None 
        self.__database: Optional[AsyncIOMotorDatabase] = None 

    async def connect(self) -> None:
        mongo_url = os.getenv('MONGO_URL',  'mongodb://mongousr:mongopwd@mongo:27017/?authSource=admin')
        mongo_db_name = os.getenv('MONGO_DATABASE', 'back-end-stores-db')    

        self.__client = AsyncIOMotorClient(mongo_url)
        
        # Connection test
        await self.__client.admin.command("ping")
        
        self.__database = self.__client[mongo_db_name]

        print("MongoDB connected successfully...")


    async def disconnect(self) -> None:
        if self.__client:
            self.__client.close()
            print("MongoDB disconnected successfully...")


    @property
    def get_database(self) -> AsyncIOMotorDatabase:
        if not self.__database:
            raise RuntimeError("")
        return self.__database
    
