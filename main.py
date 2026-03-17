# ---------------- App ----------------

from fastapi import FastAPI
from db import engine,Base
from routes import router
from db import SessionLocal
from seed_admin import create_admin


app = FastAPI(title="Role-Based Authentication & Authorization API using FastAPI")
Base.metadata.create_all(bind=engine)
db = SessionLocal()
create_admin(db)
db.close()
# ---------------- Include Router ----------------

app.include_router(router, prefix="/user", tags=["user"])

from exception import global_exception_handler
app.add_exception_handler(Exception, global_exception_handler)