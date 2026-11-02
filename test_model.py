from model import predict


def test_prediction():
    result = predict(6)
    assert abs(result - 12) < 0.01