from pydantic import Field
from pydantic import BaseModel, ConfigDict


class AbstractBaseModel(BaseModel):
    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)

    class config:
        use_enum_values = True
