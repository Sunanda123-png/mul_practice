from fastapi import FastAPI
from mul_practice.mulnutrition_app.routes.routes import mulnutrition_router
app = FastAPI()
app.include_router(mulnutrition_router)