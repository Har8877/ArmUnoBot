from hydrogram import Client

# ────────────────────────────────
# Խաղի ընդհանուր կարգավորումներ
# ────────────────────────────────

games = {}
player_game = {}

timeout = 120                     # ռեգիստրացիայի ժամանակը վայրկյաններով
minimum_players = 2               # նվազագույն խաղացողներ սկսելու համար

sudoers = [7189950846]             # քո user ID-ն (այստեղ դիր քո Telegram ID-ն)

# ────────────────────────────────
# Telegram API կոնֆիգ
# ────────────────────────────────

API_ID = 21558552              # ← այստեղ դիր քո api_id-ն (my.telegram.org-ից)
API_HASH = "04eea889fbbcf51b143ecbe0523cb19c"   # ← այստեղ դիր api_hash-ը

BOT_TOKEN = "8664179912:AAGxa-CEY7jEBkABFI-2hFZ28odmHQaaM2g"   # քո բոտի token-ը

# ────────────────────────────────
# Բոտի ստեղծումը
# ────────────────────────────────

bot = Client(
    name="bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins={"root": "unu.plugins"}   # plugins պապկեն, որտեղ կան բոտի հրամանները
)
