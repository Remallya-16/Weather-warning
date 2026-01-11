from weather_warning import weather_warning

def test_heatwave():
    assert weather_warning("Delhi", "clear", 45, 20, 10) == "Delhi: Heatwave Warning"

def test_heavy_rain():
    assert weather_warning("Mumbai", "rain", 30, 120, 20) == "Mumbai: Heavy Rain Warning"

def test_storm():
    assert weather_warning("Chennai", "rain", 28, 40, 70) == "Chennai: Storm Warning"

def test_fog():
    assert weather_warning("Bangalore", "fog", 22, 10, 5) == "Bangalore: Fog Alert"

def test_normal():
    assert weather_warning("Pune", "clear", 25, 20, 10) == "Pune: Normal Weather"
