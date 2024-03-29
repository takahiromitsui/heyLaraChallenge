from langchain_core.pydantic_v1 import BaseModel, Field

# std
from typing import Optional
from datetime import datetime


class InvoicePosition(BaseModel):
    description: Optional[str] = Field(
        description="Description of the item", default=None
    )
    amount: Optional[int] = Field(description="Amount of the item", default=None)
    unit: Optional[str] = Field(description="Unit of measurement", default=None)
    single_price: Optional[float] = Field(description="Price per unit", default=None)


class Invoice(BaseModel):
    recipient_name: Optional[str] = Field(
        description="The name of the recipient of the invoice", default=None
    )
    recipient_street: Optional[str] = Field(
        description="The street of the recipient of the invoice", default=None
    )
    recipient_zip: Optional[str] = Field(
        description="The zip code of the recipient of the invoice", default=None
    )
    recipient_city: Optional[str] = Field(
        description="The city of the recipient of the invoice", default=None
    )
    invoice_number: Optional[str] = Field(
        description="The invoice number", default=None
    )
    invoice_date: Optional[datetime] = Field(
        description="The date of the invoice", default=None
    )
    invoice_positions: Optional[list[InvoicePosition]] = Field(
        description="List of invoice positions", default=None
    )
    total_net_amount: Optional[float] = Field(
        description="Total net amount for the item", default=None
    )
