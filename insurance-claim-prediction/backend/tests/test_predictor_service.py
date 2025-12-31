from app.services.predictor import ClaimPredictor


def test_predictor_returns_positive_value():
    predictor = ClaimPredictor()
    predictor.load()

    data = {
        "age": 45,
        "annual_income": 90000,
        "vehicle_age": 8,
        "past_claims": 2,
        "accident_severity": 5,
        "policy_tenure": 6,
    }

    prediction = predictor.predict(data)

    assert isinstance(prediction, float)
    assert prediction > 0
