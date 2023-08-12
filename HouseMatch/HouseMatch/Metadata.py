from enum import Enum

BASE_URL_SHEYPOOR = "https://www.sheypoor.com/s/"
BASE_URL_DIVAR = 'https://divar.ir/s/'

class CategorySheypoor(Enum):
    HOUSE_SALE = 'houses-apartments-for-sale'
    HOUSE_RENT = 'house-apartment-for-rent'

class LocationSheypoor(Enum):
    TEHRAN = 'tehran-province'
    EAST_AZERBAIJAN = 'east-azerbaijan'
    MAZANDARAN = 'mazandaran'
    WEST_AZERBAIJAN = 'west-azerbaijan'
    ARDABIL = 'ardabil-province'
    ISFAHAN = 'isfahan-province'
    ALBORZ = 'alborz'
    ILAM = 'ilam-province'
    KHORASAN_RAZAVI = 'razavi-khorasan'
    KHOZESTAN = 'khuzestan'
    FARS = 'fars'
    BUSHEHR = 'bushehr-province'
    CHARMAHAL = 'charmahal-bakhtiari'
    SOUTH_KHORASAN = 'south-khorasan'
    NORTH_KHORASAN = 'north-khorasan'
    ZANJAN = 'zanjan-province'
    SEMNAN = 'semnan-province'
    QAZVIN = 'qazvin-province'
    QOM = 'qom-province'
    KURDISTAN = 'kurdistan'
    KERMAN = 'kerman-province'
    KERMANSHAH = 'kermanshah-province'
    GOLESTAN = 'golestan'
    LORESTAN = 'lorestan'
    GILAN = 'gilan'
    MARKAZI = 'markazi'
    HORMOZGAN = 'hormozgan'
    HAMADAN = 'hamadan-province'
    YAZD = 'yazd-province'
    KUHGILUYEH = 'kohgiluyeh-boyerahmad'
    SISTAN = 'sistan-baluchestan'

class CategoryDivar(Enum):
    HOUSE_BALL = 'buy-apartment'
    HOUSE_RENT = 'rent-apartment'

class LocationDivar(Enum):
    TEHRAN = 'tehran-province'
    EAST_AZERBAIJAN = 'azarbaijan-east-province'
    WEST_AZERBIJAN = 'azerbaijan-west-province'
    ARDABIL = 'ardabil-province'
    ISFAHAN = 'isfahan-province'
    ALBORZ = 'alborz-province'
    ILAM = 'ilam-province'
    BUSHEHR = 'bushehr-province'
    CHAHAR = 'chahar-mahaal-and-bakhtiari-province'
    SOUTH_KHORASAN = 'khorasan-south-province'
    RAZAVI = 'khorasan-razavi-province'
    NORTH_KHORASAN = 'khorasan-north-province'
    KHUZESTAN = 'khuzestan-province'
    ZANJAN = 'zanjan-province'
    SEMNAN = 'semnan-province'
    SISTAN = 'sistan-and-baluchestan-province'
    FARS = 'fars-province'
    QAZVIN = 'qazvin-province'
    QOM = 'qom'
    KURDISTAN = 'kurdistan-province'
    KERMAN = 'kerman-province'
    KERMANSHAH = 'kermanshah-province'
    AHMAD = 'kohgiluyeh-and-boyer-ahmad-province'
    GOLESTAN = 'golestan-province'
    GILAN = 'gilan-province'
    LORESTAN = 'lorestan-province'
    MAZANDARAN = 'mazandaran-province'
    MARKAZI = 'markazi-province'
    HORMOZGAN = 'hormozgan-province'
    HAMADAN = 'hamadan-province'
    YAZD = 'yazd-province'
 
def build_urls_divar():
    urls = []
    urls = []
    for location in LocationDivar.__members__.values():
        url_to_add = BASE_URL_DIVAR + location.value + '/'
        for category in CategoryDivar.__members__.values():
            urls.append(url_to_add + category.value + '?sort=sort_date')
    return urls

def build_urls_sheypoor():
    urls = []
    for location in LocationSheypoor.__members__.values():
        url_to_add = BASE_URL_SHEYPOOR + location.value + '/'
        for category in CategorySheypoor.__members__.values():
            urls.append(url_to_add + category.value + "?o=n")
    return urls