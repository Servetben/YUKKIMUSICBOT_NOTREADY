#MIT License
#Copyright (c) 2023, ©NovaNetworks

from async_pymongo import AsyncClient

from config import MONGO_DB_URI

DBNAME = "SHALINI"

mongo = AsyncClient(MONGO_DB_URI)
dbname = mongo[DBNAME]
