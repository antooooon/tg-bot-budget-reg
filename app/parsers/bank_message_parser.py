import re
from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal


@dataclass
class ParserBankMessage:
    operation_type: str
    category: str
    amount: Decimal
    payment_date: datetime


def parse_bank_message(text:str) -> ParserBankMessage:

    lines = text.splitlines()

    # operation_type, amount = lines[0].split(": ")
    operation_type = "Payment"
    amount = parse_amount(lines)
    # amount = Decimal(amount.replace(" GEL", ""))

    # place = lines[2].split(">")[0]
    place = parse_place(lines)
    category = parse_category(place)
    payment_date = datetime.strptime(parse_payment_date(lines),"%d/%m/%Y %H:%M:%S")

    # payment_date = datetime.strptime(lines[4],"%d/%m/%Y %H:%M:%S")

    return ParserBankMessage(
        operation_type=operation_type,
        category=category,
        amount=amount,
        payment_date=payment_date
    )


def parse_amount(lines:list) -> Decimal:
    first_line = lines[0].strip()
    operation_type, separator, amount = first_line.partition(":")

    if amount == "":
        amount = lines[1]

    return Decimal(amount.replace(" GEL", ""))


def parse_place(lines:list) -> str:
    third_line = lines[2]
    place, separator, _  = third_line.partition(">")
    return place.strip()


def parse_category(place:str) -> str:
    BANK_CATEGORIES = {
        "Продукты": ["WOLT", "MAGNITI", "AGROHUB", "LLC GREEN MARKET 1",
                     "CARREFOUR", "ORI NABIJI", "PETMALL LLC"],
        "Ежемес.платежи": ["SERVICE", "SOCAR-GAZ", "EP Georgia Supply", "Silknet", "Tskali"],
        "McD": ["MCDONALD'S"]
    }

    place = place.upper()

    for category, keywords in BANK_CATEGORIES.items():
        for keyword in keywords:
            if keyword in place:
                print(category)
                return category

    return "Досуг/Другое"


def parse_payment_date(lines:list) -> str:
    payment_date = ""
    for line in lines:
        if "Creation date" in line:
            _, payment_date = line.split(":")
        if re.fullmatch(r"\d{2}[./]\d{2}[./]\d{4}(?: \d{2}:\d{2}:\d{2})?", line):
            payment_date = line

    return payment_date
