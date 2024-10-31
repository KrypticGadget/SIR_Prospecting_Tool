# utils/address_standardizer.py
import re

class AddressStandardizer:
    """Standardizes address fields with common abbreviations and typos."""

    def standardize(self, address):
        # Comprehensive list of abbreviations and common typos
        abbreviations = {
            "St": "Street", "Str": "Street", "Streeet": "Street", "Sreet": "Street", "St.": "Street",
            "Ave": "Avenue", "Aven": "Avenue", "Avenu": "Avenue", "Avnue": "Avenue", "Avenuee": "Avenue", "Av": "Avenue",
            "Blvd": "Boulevard", "Bld": "Boulevard", "Bulevard": "Boulevard", "Blv": "Boulevard", "Blvd.": "Boulevard",
            "Rd": "Road", "Roa": "Road", "Rode": "Road", "Rd.": "Road",
            "Dr": "Drive", "Drv": "Drive", "Dri": "Drive", "Drve": "Drive", "Dr.": "Drive",
            "Ln": "Lane", "La": "Lane", "Lne": "Lane", "Ln.": "Lane",
            "Pl": "Place", "Plc": "Place", "Pla": "Place", "Pl.": "Place",
            "Ct": "Court", "Crt": "Court", "Cr": "Court", "Court": "Court",
            "Sq": "Square", "Sqre": "Square", "Squr": "Square", "Sqr": "Square", "Square": "Square",
            "Pkwy": "Parkway", "Pkway": "Parkway", "Pky": "Parkway", "Pkw": "Parkway",
            "Cir": "Circle", "Crcle": "Circle", "Circ": "Circle", "Cir.": "Circle",
            "Terr": "Terrace", "Ter": "Terrace", "Tr": "Terrace",
            "Hwy": "Highway", "Hiway": "Highway", "Hyw": "Highway", "Hway": "Highway",
            "Expr": "Expressway", "Expw": "Expressway", "Exp": "Expressway",
            "Ctr": "Center", "Cntr": "Center", "Ctr.": "Center",
            "Mt": "Mountain", "Mtn": "Mountain", "Mntn": "Mountain",
            # Directional abbreviations
            "N": "North", "N.": "North", "No": "North", "No.": "North",
            "S": "South", "S.": "South", "So": "South", "So.": "South",
            "E": "East", "E.": "East",
            "W": "West", "W.": "West",
            "NE": "Northeast", "N.E.": "Northeast", "N.E": "Northeast", "NE.": "Northeast",
            "NW": "Northwest", "N.W.": "Northwest", "N.W": "Northwest", "NW.": "Northwest",
            "SE": "Southeast", "S.E.": "Southeast", "S.E": "Southeast", "SE.": "Southeast",
            "SW": "Southwest", "S.W.": "Southwest", "S.W": "Southwest", "SW.": "Southwest"
        }

        if not address:
            return address

        # Convert to string if not already
        address = str(address)

        # Replace abbreviations using regex with word boundaries
        for abbr, full in abbreviations.items():
            address = re.sub(rf'\b{abbr}\b', full, address, flags=re.IGNORECASE)

        # Remove double spaces
        address = re.sub(r'\s+', ' ', address)
        
        # Remove trailing/leading whitespace
        address = address.strip()

        return address