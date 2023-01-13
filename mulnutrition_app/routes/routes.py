from fastapi import APIRouter
from mul_practice.mulnutrition_app.model.model import Mul
from mul_practice.mulnutrition_app.config.database import collection
from mul_practice.mulnutrition_app.schemas.schema import mul_serializer, mulnut_serializer
from bson import ObjectId

mulnutrition_router = APIRouter()


@mulnutrition_router.get("/")
async def get_mulnut():
    muln = mulnut_serializer(collection.find())
    return {"status": "ok", "data": muln}


@mulnutrition_router.get("/{id}")
async def get_mulnutrition(id: str):
    muln = mulnut_serializer(collection.find({"_id": ObjectId(id)}))
    return {"status": "ok", "data": muln}


@mulnutrition_router.post("/")
async def post_mulnutrition(mul: Mul):
    _id = collection.insert_one(dict(mul))
    muln = mulnut_serializer(collection.find({"_id": _id.inserted_id}))
    return {"status": "ok", "data": muln}


@mulnutrition_router.put("/{id}")
async def put_mulnutrition(id: str, mul: Mul):
    collection.find_one_and_update({"_id": ObjectId(id)},
                                   {"$set": dict(mul)})
    muln = mulnut_serializer(collection.find({"_id": ObjectId(id)}))
    return {"status": "ok", "data": muln}


@mulnutrition_router.delete("/{id}")
async def delete_mulnutrition(id: str):
    collection.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "ok", "data": []}
