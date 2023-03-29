def from_kelvin_farenheit(kelvin):
    return round(kelvin * 1.8 - 459.67, 2)

def from_kelvin_celcius(kelvin):
    return round(kelvin - 237.15, 2)

def from_hpa_psi(hpa):
    return hpa * 0.0145037738 

def from_ms_mph(m_s):
    return m_s * 2.2369362920544025

def from_ms_kph(m_s):
    return m_s * 3.6