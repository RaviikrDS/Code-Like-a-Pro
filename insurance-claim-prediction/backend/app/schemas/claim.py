from pydantic import BaseModel, Field

class ClaimRequest(BaseModel):
    age: int = Field(..., ge=18)
    annual_income: float = Field(..., gt=0)
    vehicle_age: int = Field(..., ge=0)
    past_claims: int = Field(..., ge=0)
    accident_severity: int = Field(..., ge=1, le=5)
    policy_tenure: int = Field(..., ge=1)
