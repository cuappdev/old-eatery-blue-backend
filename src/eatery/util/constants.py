from enum import Enum

from eatery.datatype.Eatery import EateryID

CORNELL_DINING_URL = "https://admin-now.dining.cornell.edu/api/1.0/dining/eateries.json"
CORNELL_VENDOR_URL = (
    "https://vendor-api-extra.scl.cornell.edu/api/external/location-count"
)

DAY_OF_WEEK_LIST = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]

DEFAULT_IMAGE_URL = "https://images-prod.healthline.com/hlcmsresource/images/AN_images/health-benefits-of-apples-1296x728-feature.jpg"


class SnapshotFileName(Enum):
    EATERY_STORE = "eatery_store.txt"
    ALERT_STORE = "alert_store.txt"
    CATEGORY_STORE = "category_store.txt"
    MENU_STORE = "menu_store.txt"
    ITEM_STORE = "item_store.txt"
    SUBITEM_STORE = "subitem_store.txt"
    CATEGORY_ITEM_ASSOCIATION = "category_item_association.txt"
    EVENT_SCHEDULE = "event_schedule.txt"
    DAY_OF_WEEK_EVENT_SCHEDULE = "day_of_week_event_schedule.txt"
    DATE_EVENT_SCHEDULE = "date_event_schedule.txt"
    CLOSED_EVENT_SCHEDULE = "closed_event_schedule.txt"
    TRANSACTION_HISTORY = "transaction_history.txt"
    SCHEDULE_EXCEPTION = "schedule_exception.txt"


EATERY_INFO = {
    31: {
        "internal_id": EateryID.ONE_ZERO_FOUR_WEST,
        "image_url": "https://raw.githubusercontent.com/cuappdev/assets/master/eatery/eatery-images/104-West.jpg"
    },
    7: {
        "internal_id": EateryID.LIBE_CAFE,
        "image_url": "https://raw.githubusercontent.com/cuappdev/assets/master/eatery/eatery-images/Amit-Bhatia-Libe-Cafe.jpg"
    },
    8: {
        "internal_id": EateryID.ATRIUM_CAFE,
        "image_url": "https://raw.githubusercontent.com/cuappdev/assets/master/eatery/eatery-images/Atrium-Cafe.jpg"
    },
    1: {
        "internal_id": EateryID.BEAR_NECESSITIES,
        "image_url": "https://raw.githubusercontent.com/cuappdev/assets/master/eatery/eatery-images/Bear-Necessities.jpg"
    },
    25: {
        "internal_id": EateryID.BECKER_HOUSE,
        "image_url": "https://raw.githubusercontent.com/cuappdev/assets/master/eatery/eatery-images/Becker-House-Dining.jpg"
    },
    10: {
        "internal_id": EateryID.BIG_RED_BARN,
        "image_url": "https://raw.githubusercontent.com/cuappdev/assets/master/eatery/eatery-images/Big-Red-Barn.jpg"
    },
    11: {
        "internal_id": EateryID.BUS_STOP_BAGELS,
        "image_url": "https://raw.githubusercontent.com/cuappdev/assets/master/eatery/eatery-images/Bug-Stop-Bagels.jpg"
    },
    12: {
        "internal_id": EateryID.CAFE_JENNIE,
        "image_url": "https://raw.githubusercontent.com/cuappdev/assets/master/eatery/eatery-images/Cafe-Jennie.jpg"
    },
    26: {
        "internal_id": EateryID.COOK_HOUSE,
        "image_url": "https://raw.githubusercontent.com/cuappdev/assets/master/eatery/eatery-images/Cook-House-Dining.jpg"
    },
    14: {
        "internal_id": EateryID.DAIRY_BAR,
        "image_url": "https://raw.githubusercontent.com/cuappdev/assets/master/eatery/eatery-images/Cornell-Dairy-Bar.jpg"
    },
    41: {
        "internal_id": EateryID.CROSSINGS_CAFE,
        "image_url": "https://raw.githubusercontent.com/cuappdev/assets/master/eatery/eatery-images/Crossings-Cafe.jpg"
    },
    32: {
        "internal_id": EateryID.FRANNYS,
        "image_url": "https://raw.githubusercontent.com/cuappdev/assets/master/eatery/eatery-images/frannys.jpg"
    },
    16: {
        "internal_id": EateryID.GOLDIES_CAFE,
        "image_url": "https://raw.githubusercontent.com/cuappdev/assets/master/eatery/eatery-images/Goldies-Cafe.jpg"
    },
    15: {
        "internal_id": EateryID.GREEN_DRAGON,
        "image_url": "https://raw.githubusercontent.com/cuappdev/assets/master/eatery/eatery-images/Green-Dragon.jpg"
    },
    24: {
        "internal_id": EateryID.HOT_DOG_CART,
        "image_url": "https://raw.githubusercontent.com/cuappdev/assets/master/eatery/eatery-images/Hot-Dog-Cart.jpg"
    },
    34: {
        "internal_id": EateryID.ICE_CREAM_BIKE,
        "image_url": "https://raw.githubusercontent.com/cuappdev/assets/master/eatery/eatery-images/icecreamcart.jpg"
    },
    27: {
        "internal_id": EateryID.BETHE_HOUSE,
        "image_url": "https://raw.githubusercontent.com/cuappdev/assets/master/eatery/eatery-images/Jansens-Dining.jpg"
    },
    28: {
        "internal_id": EateryID.JANSENS_MARKET,
        "image_url": "https://raw.githubusercontent.com/cuappdev/assets/master/eatery/eatery-images/Jansens-Market.jpg"
    },
    29: {
        "internal_id": EateryID.KEETON_HOUSE,
        "image_url": "https://raw.githubusercontent.com/cuappdev/assets/master/eatery/eatery-images/Keeton-House-Dining.jpg"
    },
    42: {
        "internal_id": EateryID.MANN_CAFE,
        "image_url": "https://raw.githubusercontent.com/cuappdev/assets/master/eatery/eatery-images/Mann-Cafe.jpg"
    },
    18: {
        "internal_id": EateryID.MARTHAS_CAFE,
        "image_url": "https://raw.githubusercontent.com/cuappdev/assets/master/eatery/eatery-images/Marthas-Cafe.jpg"
    },
    19: {
        "internal_id": EateryID.MATTINS_CAFE,
        "image_url": "https://raw.githubusercontent.com/cuappdev/assets/master/eatery/eatery-images/Mattins-Cafe.jpg"
    },
    33: {
        "internal_id": EateryID.MCCORMICKS,
        "image_url": "https://raw.githubusercontent.com/cuappdev/assets/master/eatery/eatery-images/mccormicks.jpg"
    },
    3: {
        "internal_id": EateryID.NORTH_STAR_DINING,
        "image_url": "https://raw.githubusercontent.com/cuappdev/assets/master/eatery/eatery-images/North-Star.jpg"
    },
    20: {
        "internal_id": EateryID.OKENSHIELDS,
        "image_url": "https://raw.githubusercontent.com/cuappdev/assets/master/eatery/eatery-images/Okenshields.jpg"
    },
    4: {
        "internal_id": EateryID.RISLEY,
        "image_url": "https://raw.githubusercontent.com/cuappdev/assets/master/eatery/eatery-images/Risley-Dining.jpg"
    },
    5: {
        "internal_id": EateryID.RPCC,
        "image_url": "https://raw.githubusercontent.com/cuappdev/assets/master/eatery/eatery-images/Risley-Dining.jpg"
    },
    30: {
        "internal_id": EateryID.ROSE_HOUSE,
        "image_url": "https://raw.githubusercontent.com/cuappdev/assets/master/eatery/eatery-images/Rose-House-Dining.jpg"
    },
    21: {
        "internal_id": EateryID.RUSTYS,
        "image_url": "https://raw.githubusercontent.com/cuappdev/assets/master/eatery/eatery-images/Rustys.jpg"
    },
    13: {
        "internal_id": EateryID.STRAIGHT_FROM_THE_MARKET,
        "image_url": "https://raw.githubusercontent.com/cuappdev/assets/master/eatery/eatery-images/StraightMarket.jpg"
    },
    23: {
        "internal_id": EateryID.TRILLIUM,
        "image_url": "https://raw.githubusercontent.com/cuappdev/assets/master/eatery/eatery-images/Trillium.jpg"
    },
    43: {
        "internal_id": EateryID.MORRISON_DINING,
        "image_url": "https://raw.githubusercontent.com/cuappdev/assets/master/eatery/eatery-images/Morrison-Dining.jpg"
    },
    44: {
        "internal_id": EateryID.NOVICKS_CAFE,
        "image_url": "https://raw.githubusercontent.com/cuappdev/assets/master/eatery/eatery-images/novicks-cafe.jpg"
    },
    45: {
        "internal_id": EateryID.VET_CAFE,
        "image_url": "https://raw.githubusercontent.com/cuappdev/assets/master/eatery/eatery-images/vets-cafe.jpg"
    }
}

VENDOR_NAME_TO_INTERNAL = {
    "bearnecessities": EateryID.BEAR_NECESSITIES,
    "northstarmarketplace": EateryID.NORTH_STAR_DINING,
    "jansensmarket": EateryID.JANSENS_MARKET,
    "stockinghallcafe": EateryID.DAIRY_BAR,
    "stockinghall": EateryID.DAIRY_BAR,
    "marthas": EateryID.MARTHAS_CAFE,
    "cafejennie": EateryID.CAFE_JENNIE,
    "goldiescafe": EateryID.GOLDIES_CAFE,
    "alicecookhouse": EateryID.COOK_HOUSE,
    "carlbeckerhouse": EateryID.BECKER_HOUSE,
    "duffield": EateryID.MATTINS_CAFE,
    "greendragon": EateryID.GREEN_DRAGON,
    "trillium": EateryID.TRILLIUM,
    "olinlibecafe": EateryID.LIBE_CAFE,
    "statlerterrace": EateryID.TERRACE,
    "busstopbagels": EateryID.BUS_STOP_BAGELS,
    "kosher": EateryID.ONE_ZERO_FOUR_WEST,
    "jansensatbethehouse": EateryID.BETHE_HOUSE,
    "keetonhouse": EateryID.KEETON_HOUSE,
    "rpme": EateryID.RPCC,
    "rosehouse": EateryID.ROSE_HOUSE,
    "risley": EateryID.RISLEY,
    "frannysft": EateryID.FRANNYS,
    "mccormicks": EateryID.MCCORMICKS,
    "sage": EateryID.ATRIUM_CAFE,
    "straightmarket": EateryID.STRAIGHT_FROM_THE_MARKET,
    "crossingscafe": EateryID.CROSSINGS_CAFE,
    "okenshields": EateryID.OKENSHIELDS,
    "bigredbarn": EateryID.BIG_RED_BARN,
    "rustys": EateryID.RUSTYS,
    "manncafe": EateryID.MANN_CAFE,
    "statlermacs": EateryID.MACS_CAFE,
    "morrisondining": EateryID.MORRISON_DINING,
    "morrison": EateryID.MORRISON_DINING,
    "novickscafe": EateryID.NOVICKS_CAFE,
    "Vet College Cafe": EateryID.VET_CAFE,
}


def get_eatery_info(id: int):
    """Get both internal ID and image URL for a given dining ID"""
    if id in EATERY_INFO:
        return EATERY_INFO[id]
    
    print(f"Missing eatery_id {id}")
    return {
        "internal_id": None,
        "image_url": DEFAULT_IMAGE_URL
    }


def get_eatery_info_by_vendor_name(vendor_eatery_name):
    """Get both internal ID and image URL for a given vendor name"""
    vendor_eatery_name = "".join(c.lower() for c in vendor_eatery_name if c.isalpha())
    
    internal_id = VENDOR_NAME_TO_INTERNAL.get(vendor_eatery_name)
    
    if internal_id is not None:
        for dining_id, info in EATERY_INFO.items():
            if info["internal_id"] == internal_id:
                return info
        
        return {
            "internal_id": internal_id,
            "image_url": DEFAULT_IMAGE_URL
        }
    
    # TODO: Add a slack notif / flag that a wait time location was not recognized
    return {
        "internal_id": None,
        "image_url": DEFAULT_IMAGE_URL
    }


def dining_id_to_internal_id(id: int):
    """Convert dining ID to internal eatery ID"""
    info = get_eatery_info(id)
    return info["internal_id"]


def vendor_name_to_internal_id(vendor_eatery_name):
    """Convert vendor eatery name to internal eatery ID"""
    vendor_eatery_name = "".join(c.lower() for c in vendor_eatery_name if c.isalpha())
    
    if vendor_eatery_name in VENDOR_NAME_TO_INTERNAL:
        return VENDOR_NAME_TO_INTERNAL[vendor_eatery_name]
    
    # TODO: Add a slack notif / flag that a wait time location was not recognized
    return None


def dining_id_to_image_url(id: int):
    """Convert dining ID directly to image URL"""
    if id in EATERY_INFO:
        return EATERY_INFO[id]["image_url"]
    
    print(f"Missing image url for dining_id {id}")
    return DEFAULT_IMAGE_URL