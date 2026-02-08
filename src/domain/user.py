from typing import Dict, Any

class User:
    def __init__(self, data: Dict[str, Any]):
        self.id = data.get('id')
        self.name = data.get('name')
        self.username = data.get('username')
        self.email = data.get('email')
        self.phone = data.get('phone')
        self.website = data.get('website')
        self.address = data.get('address', {})
        self.company = data.get('company', {})

    def to_flat_dict(self) -> Dict[str, Any]:
        flat = {
            'id': self.id,
            'name': self.name,
            'username': self.username,
            'email': self.email,
            'phone': self.phone,
            'website': self.website,
            'address_street': self.address.get('street'),
            'address_suite': self.address.get('suite'),
            'address_city': self.address.get('city'),
            'address_zipcode': self.address.get('zipcode'),
            'address_geo_lat': self.address.get('geo', {}).get('lat'),
            'address_geo_lng': self.address.get('geo', {}).get('lng'),
            'company_name': self.company.get('name'),
            'company_catchPhrase': self.company.get('catchPhrase'),
            'company_bs': self.company.get('bs'),
        }
        return flat
