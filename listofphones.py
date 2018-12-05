from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Company, Base, MobilePhones

engine = create_engine('sqlite:///mobilephones.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

#Samsung Mobile Phones

company1 = Company(name = "Samsung")

session.add(company1)
session.commit()

mobilephone1 = MobilePhones(name = "Galaxy Note 9", Specifications = "Display 6.4inch - Camera  12MegaPixel - Processor Exynos 9810 - Storage 128/512GB - Ram 6/8GB ", price = "$900", company = company1)

session.add(mobilephone1)
session.commit()

mobilephone2 = MobilePhones(name = "Galaxy S9 Plus", Specifications = "Display 5.8inch - Camera  12MegaPixel - Processor Exynos 9810 - Storage 64/128/256GB - Ram 6GB ", price = "$700", company = company1)

session.add(mobilephone2)
session.commit()

mobilephone3 = MobilePhones(name = "Galaxy A8(2018)", Specifications = "Display 5.6inch - Camera  16MegaPixel - Processor Exynos 7885 - Storage 32/64GB - Ram 4GB ", price = "$400", company = company1)

session.add(mobilephone3)
session.commit()

mobilephone4 = MobilePhones(name = "Galaxy S8 Plus", Specifications = "Display 6.2inch - Camera  12MegaPixel - Processor Exynos 8895 - Storage 64/128GB - Ram 4/6GB ", price = "$500", company = company1)

session.add(mobilephone4)
session.commit()

mobilephone5 = MobilePhones(name = "Galaxy A9 (2018)", Specifications = "Display 6.3inch - Camera  24MegaPixel - Processor Qualcomm SDM660 Snapdragon 660 - Storage 128GB - Ram 6/8GB ", price = "$650", company = company1)

session.add(mobilephone5)
session.commit()

#Apple Mobile Phones

company2 = Company(name = "Apple")

session.add(company2)
session.commit()

mobilephone6 = MobilePhones(name = "iPhone XS Max", Specifications = "Display 6.5inch - Camera  12MegaPixel - Processor Apple A12 Bionic - Storage 64/256/512GB - Ram 4GB ", price = "$1000", company = company2)

session.add(mobilephone6)
session.commit()

mobilephone7 = MobilePhones(name = "iPhone XR", Specifications = "Display 6.1inch - Camera  12MegaPixel - Processor Apple A12 Bionic - Storage 64/128/256GB - Ram 3GB ", price = "$650", company = company2)

session.add(mobilephone7)
session.commit()

mobilephone8 = MobilePhones(name = "iPhone X", Specifications = "Display 5.8inch - Camera  12MegaPixel - Processor Apple A11 Bionic - Storage 64/256GB - Ram 3GB ", price = "$700", company = company2)

session.add(mobilephone8)
session.commit()

mobilephone9 = MobilePhones(name = "iPhone 8 Plus", Specifications = "Display 5.5inch - Camera  12MegaPixel - Processor Apple A11 Bionic - Storage 64/256GB - Ram 3GB ", price = "$550", company = company2)

session.add(mobilephone9)
session.commit()

mobilephone10 = MobilePhones(name = "iPhone 7", Specifications = "Display 4.7inch - Camera  12MegaPixel - Processor Apple A10 Bionic - Storage 32/128/256GB - Ram 2GB ", price = "$300", company = company2)

session.add(mobilephone10)
session.commit()

#Huawei Mobile Phones

company3 = Company(name = "Huawei")

session.add(company3)
session.commit()

mobilephone11 = MobilePhones(name = "Mate 20 Pro", Specifications = "Display 6.39inch - Camera  40MegaPixel - Processor HiSilicon Kirin 980 - Storage 256GB - Ram 8GB ", price = "$1000", company = company3)

session.add(mobilephone11)
session.commit()

mobilephone12 = MobilePhones(name = "P20 Pro", Specifications = "Display 6.1inch - Camera  40MegaPixel - Processor HiSilicon Kirin 970 - Storage 128/256GB - Ram 6/8GB ", price = "$650", company = company3)

session.add(mobilephone12)
session.commit()

mobilephone13 = MobilePhones(name = "Mate 10 Pro", Specifications = "Display 6.0inch - Camera  20MegaPixel - Processor HiSilicon Kirin 970 - Storage 64/128GB - Ram 4/6GB ", price = "$450", company = company3)

session.add(mobilephone13)
session.commit()

mobilephone14 = MobilePhones(name = "Nova 3", Specifications = "Display 6.3inch - Camera  24MegaPixel - Processor HiSilicon Kirin 970 - Storage 128GB - Ram 4/6GB ", price = "$400", company = company3)

session.add(mobilephone14)
session.commit()

mobilephone15 = MobilePhones(name = "Honor 8X", Specifications = "Display 6.5inch - Camera  20MegaPixel - Processor HiSilicon Kirin 910 - Storage 64/128GB - Ram 4/6GB ", price = "$300", company = company3)

session.add(mobilephone15)
session.commit()

#Nokia Mobile Phones

company4 = Company(name = "Nokia")

session.add(company4)
session.commit()

mobilephone16 = MobilePhones(name = "Nokia 8.1", Specifications = "Display 6.18inch - Camera  13MegaPixel - Processor Qualcomm SDM710 Snapdragon 710 - Storage 64/128GB - Ram 4/6GB ", price = "$550", company = company4)

session.add(mobilephone16)
session.commit()

mobilephone17 = MobilePhones(name = "Nokia X6", Specifications = "Display 5.8inch - Camera  16MegaPixel - Processor Qualcomm SDM636 Snapdragon 636 - Storage 32/64GB - Ram 4/6GB ", price = "$300", company = company4)

session.add(mobilephone17)
session.commit()

mobilephone18 = MobilePhones(name = "Nokia X7", Specifications = "Display 6.18inch - Camera  13MegaPixel - Processor Qualcomm SDM710 Snapdragon 710 - Storage 64/128GB - Ram 4/6GB ", price = "$400", company = company4)

session.add(mobilephone18)
session.commit()

mobilephone19 = MobilePhones(name = "Nokia 6", Specifications = "Display 5.5inch - Camera  16MegaPixel - Processor Qualcomm MSM8937 Snapdragon 430 - Storage 32/64GB - Ram 3/4GB ", price = "$250", company = company4)

session.add(mobilephone19)
session.commit()

mobilephone20 = MobilePhones(name = "Nokia 3.1 Plus", Specifications = "Display 6.0inch - Camera  13MegaPixel - Processor Mediatek MT6762 Helio P22 - Storage 16/32GB - Ram 2/3GB ", price = "$150", company = company4)

session.add(mobilephone20)
session.commit()

#HTC Mobile Phones

company5 = Company(name = "HTC")

session.add(company5)
session.commit()

mobilephone21 = MobilePhones(name = "Exodus 1", Specifications = "Display 6.0inch - Camera  16MegaPixel - Processor Qualcomm SDM845 Snapdragon 845 - Storage 128GB - Ram 6GB ", price = "$750", company = company5)

session.add(mobilephone21)
session.commit()

mobilephone22 = MobilePhones(name = "U12 Plus", Specifications = "Display 6.0inch - Camera  12MegaPixel - Processor Qualcomm SDM845 Snapdragon 845 - Storage 64/128GB - Ram 6GB ", price = "$550", company = company5)

session.add(mobilephone22)
session.commit()

mobilephone23 = MobilePhones(name = "U11", Specifications = "Display 5.5inch - Camera  12MegaPixel - Processor Qualcomm MSM8998 Snapdragon 835 - Storage 64/128GB - Ram 4/6GB ", price = "$350", company = company5)

session.add(mobilephone23)
session.commit()

mobilephone24 = MobilePhones(name = "U Ultra", Specifications = "Display 5.7inch - Camera  12MegaPixel - Processor Qualcomm MSM8996 Snapdragon 821 - Storage 64/128GB - Ram 4GB ", price = "$300", company = company5)

session.add(mobilephone24)
session.commit()

mobilephone25 = MobilePhones(name = "Desire 12 Plus", Specifications = "Display 6.0inch - Camera  13MegaPixel - Processor Qualcomm SDM450 Snapdragon 450 - Storage 32GB - Ram 3GB ", price = "$150", company = company5)

session.add(mobilephone25)
session.commit()

#Google Mobile Phones

company6 = Company(name = "Google")

session.add(company6)
session.commit()

mobilephone26 = MobilePhones(name = "Pixel 3 XL", Specifications = "Display 6.3inch - Camera  12MegaPixel - Processor Qualcomm SDM845 Snapdragon 845 - Storage 64/128GB - Ram 4GB ", price = "$900", company = company6)

session.add(mobilephone26)
session.commit()

mobilephone27 = MobilePhones(name = "Pixel 3", Specifications = "Display 5.5inch - Camera  12MegaPixel - Processor Qualcomm SDM845 Snapdragon 845 - Storage 64/128GB - Ram 4GB ", price = "$800", company = company6)

session.add(mobilephone27)
session.commit()

mobilephone28 = MobilePhones(name = "Pixel 2 XL", Specifications = "Display 6.0inch - Camera  12MegaPixel - Processor Qualcomm MSM8998 Snapdragon 835 - Storage 64/128GB - Ram 4GB ", price = "$600", company = company6)

session.add(mobilephone28)
session.commit()

mobilephone29 = MobilePhones(name = "Pixel 2", Specifications = "Display 5.0inch - Camera  12MegaPixel - Processor Qualcomm MSM8998 Snapdragon 835 - Storage 64/128GB - Ram 4GB ", price = "$490", company = company6)

session.add(mobilephone29)
session.commit()

mobilephone30 = MobilePhones(name = "Pixel", Specifications = "Display 5.0inch - Camera  12MegaPixel - Processor Qualcomm MSM8996 Snapdragon 821 - Storage 32/128GB - Ram 4GB ", price = "$350", company = company6)

session.add(mobilephone30)
session.commit()

#Xiaomi Mobile Phones

company7 = Company(name = "Xiaomi")

session.add(company7)
session.commit()

mobilephone31 = MobilePhones(name = "Mi Mix 3", Specifications = "Display 6.39inch - Camera  12MegaPixel - Processor Qualcomm SDM845 Snapdragon 845 - Storage 128/256GB - Ram 10GB ", price = "$800", company = company7)

session.add(mobilephone31)
session.commit()

mobilephone32 = MobilePhones(name = "Redmi Note 6 Pro", Specifications = "Display 6.26inch - Camera  12MegaPixel - Processor Qualcomm SDM636 Snapdragon 636 - Storage 32/64GB - Ram 4/6GB ", price = "$550", company = company7)

session.add(mobilephone32)
session.commit()

mobilephone33 = MobilePhones(name = "Mi 8 Pro", Specifications = "Display 6.21inch - Camera  12MegaPixel - Processor Qualcomm SDM845 Snapdragon 845 - Storage 128GB - Ram 6/8GB ", price = "$650", company = company7)

session.add(mobilephone33)
session.commit()

mobilephone34 = MobilePhones(name = "Pocophone F1", Specifications = "Display 6.18inch - Camera  12MegaPixel - Processor Qualcomm SDM845 Snapdragon 845 - Storage 64/128/256GB - Ram 6/8GB ", price = "$700", company = company7)

session.add(mobilephone34)
session.commit()

mobilephone35 = MobilePhones(name = "Mi 8", Specifications = "Display 6.21inch - Camera  12MegaPixel - Processor Qualcomm SDM845 Snapdragon 845 - Storage 64/128/256GB - Ram 6/8GB ", price = "$600", company = company7)

session.add(mobilephone35)
session.commit()

print "added Mobile Phones!"