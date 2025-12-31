import pytest
from pydantic import ValidationError
from app.schemas.claim import ClaimRequest


def test_claim_schema_valid():
    data = {
        "age": 35,
        "annual_income": 60000,
        "vehicle_age": 4,
        "past_claims": 1,
        "accident_severity": 2,
        "policy_tenure": 3,
    }

    claim = ClaimRequest(**data)
    assert claim.age == 35


def test_claim_schema_invalid_age():
    data = {
        "age": 16,  # invalid
        "annual_income": 60000,
        "vehicle_age": 4,
        "past_claims": 1,
        "accident_severity": 2,
        "policy_tenure": 3,
    }

    with pytest.raises(ValidationError):
        ClaimRequest(**data)
