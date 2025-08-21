from decimal import Decimal
from pydantic import BaseModel, Field

class BaseSchemaMixin(BaseModel):
    class Config:
        from_attributes = True

class ProductBase(BaseSchemaMixin):
    name: str = Field(..., description="Product name")
    quantity: int = Field(..., description="Product quantity")
    price: Decimal = Field(..., description="Product price")
    status: bool = Field(..., description="Product status")

class ProductIn(ProductBase):
    pass