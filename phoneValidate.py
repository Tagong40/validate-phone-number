import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone


def validate(number):
    x = phonenumbers.parse(number, "GB")
    c = geocoder.description_for_number(x, "en")
    d = carrier.name_for_number(x, "en")
    v = timezone.time_zones_for_number(x)
    is_valid = phonenumbers.is_valid_number(x)

    return {'valid': is_valid, 'country': c, 'countryCode': f"+{x.country_code}", 'phoneNumber': f"{x.national_number}", "carrier": d, "timeZone": v, }
