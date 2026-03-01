from hydrogram import Client

# ────────────────────────────────
# Խաղի ընդհանուր կարգավորումներ
# ────────────────────────────────

games = {}
player_game = {}

timeout = 120                     # ռեգիստրացիայի ժամանակը վայրկյաններով
minimum_players = 2               # նվազագույն խաղացողներ սկսելու համար

sudoers = [123456789]             # քո user ID-ն (այստեղ դիր քո Telegram ID-ն)

# ────────────────────────────────
# Telegram API կոնֆիգ
# ────────────────────────────────

API_ID = 1234567                  # ← այստեղ դիր քո api_id-ն (my.telegram.org-ից)
API_HASH = "abcdef1234567890abcdef1234567890"   # ← այստեղ դիր api_hash-ը

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
