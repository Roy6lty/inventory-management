from fastapi import (
    APIRouter,
    HTTPException,
)
from app.database.session import db_dependency, db_client
from app.response import UserResponse
from app.schema import UserSchema
from app.crud import TableData, UserData
from fastapi.encoders import jsonable_encoder
from pydantic import Extra, TypeAdapter, create_model, BaseModel, Field, field_validator
from bson.objectid import ObjectId
from datetime import date
from typing import List, Optional, Type
import json
from bson.objectid import ObjectId

router = APIRouter(tags=["Create User"])


def create_dynamic_model(fields: dict) -> List[BaseModel]:
    # Create a new class dynamically
    class DynamicModel(BaseModel):
        id: str = Field(validation_alias="_id")

        @field_validator("id", mode="before")
        def stringfy(cls, value):
            if value is None:
                return None
            value = str(value)
            return value.strip()

        class Config:
            extra = "allow"

        pass

    # Add fields to the newly created class
    for field_name, field_type in fields.items():
        setattr(DynamicModel, field_name, Optional[field_type])

    class ModelList(BaseModel):
        result_data: List[DynamicModel]

    return ModelList


# fields = {"name": (str, Field(..., max_length=10)), "age": (int, Field(..., gt=0))}


class voters(BaseModel):
    id: str = Field(validation_alias="_id")
    name: str
    date_of_birth: str
    gender: str
    nationality: str
    registration_number: str
    address_street: str
    address_city: str
    address_postcode: str
    email: str
    phone_number: str
    picture: str
    registered_age: int
    address_country: str

    @field_validator("id", mode="before")
    def stringfy(cls, value):
        if value is None:
            return None
        value = str(value)
        return value.strip()


class TableSchema(BaseModel):
    table_name: str
    table_schema: dict


@router.post("/add-account", summary="Create a new account", status_code=201)
async def create_user(db_conn: db_dependency, userdata: UserSchema):
    UserData.create_user(
        name=userdata.name, age=userdata.age, address=userdata.address, db_conn=db_conn
    )
    return {"message": "successful"}


@router.get(
    "/get-accounts",
    summary="Get created Accounts",
    status_code=200,
    response_model=list[UserResponse],
)
async def get_users(db_conn: db_dependency):
    result = UserData.get_all_users(db_conn=db_conn)
    return result


@router.get("/get-voters")
async def get_voters(table_name: str):
    result = TableData.create_table(mongodb_conn=db_client)
    # result = db_client.list_database_names()
    election_db = db_client.election
    result = list(election_db.voters.find({}))
    schema_db = db_client.schema

    schema = schema_db.schema_collection.find_one({"table_name": table_name})
    if schema is None:
        raise HTTPException(status_code=404, description="Table Not found")
    print(schema)

    values_list = list(schema.values())
    keys_list = list(schema.keys())

    cleaned_values = [  # strip out the "" and ''  from the  values if value is a string
        value.strip("'\"") if isinstance(value, str) else value for value in values_list
    ]
    my_dict = {key: value for key, value in zip(keys_list, cleaned_values)}

    model = create_dynamic_model(my_dict)

    result_list = model(result_data=result)

    # k = model.model_validate(result[0])
    # print(k.registered_age, result[0])
    # ta = TypeAdapter(List[model])
    # m = ta.validate_python(result)

    return jsonable_encoder(result_list)


@router.post("/create-voters")
async def create_voters():
    collection = db_client.schema
    result = collection.voter.find({})
    for i in result:
        schema = i
        values_list = list(schema.values())
        keys_list = list(schema.keys())

    cleaned_values = [
        value.strip("'\"") if isinstance(value, str) else value for value in values_list
    ]
    my_dict = {key: value for key, value in zip(keys_list[1:], cleaned_values[1:])}

    create_dynamic_model(my_dict)


"""_summary_

db.createCollection("students", {
validator: {
    $jsonSchema: {
        bsonType: "object",
        title: "Student Object Validation",
        required: [ "address", "major", "name", "year" ],
        properties: {
        name: {
            bsonType: "string",
            description: "'name' must be a string and is required"
        },
        year: {
            bsonType: "int",
            minimum: 2017,
            maximum: 3017,
            description: "'year' must be an integer in [ 2017, 3017 ] and is required"
        },
        gpa: {
            bsonType: [ "double" ],
            description: "'gpa' must be a double if the field exists"
        }
        }
    }
}
} )
"""


@router.post("/create-custom-table")
async def create_voters(data: TableSchema):
    database = db_client.schema  # creates a database
    values_list = list(data.table_schema.values())
    keys_list = list(data.table_schema.keys())

    data.table_schema.update({"table_name": f"{data.table_name}"})

    cleaned_values = [
        value.strip("'\"") if isinstance(value, str) else value for value in values_list
    ]
    my_dict = {key: value for key, value in zip(keys_list, cleaned_values)}
    model = create_dynamic_model(my_dict)
    # use Schema collection
    schema_collection = database.schema_collection
    schema_collection.insert_one(data.table_schema).inserted_id

    return "success"


@router.post("/create-entry", tags=["Custom Tables"])
async def create_voters(data: TableSchema):
    database = db_client.schema  # creates a database
    values_list = list(data.table_schema.values())
    keys_list = list(data.table_schema.keys())

    data.table_schema.update({"table_name": f"{data.table_name}"})

    cleaned_values = [
        value.strip("'\"") if isinstance(value, str) else value for value in values_list
    ]
    my_dict = {key: value for key, value in zip(keys_list, cleaned_values)}
    model = create_dynamic_model(my_dict)
    # use Schema collection
    schema_collection = database.schema_collection
    schema_collection.insert_one(data.table_schema).inserted_id

    return "success"
