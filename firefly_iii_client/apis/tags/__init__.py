# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from firefly_iii_client.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    ABOUT = "about"
    ACCOUNTS = "accounts"
    ATTACHMENTS = "attachments"
    AUTOCOMPLETE = "autocomplete"
    AVAILABLE_BUDGETS = "available_budgets"
    BILLS = "bills"
    BUDGETS = "budgets"
    CATEGORIES = "categories"
    CHARTS = "charts"
    CONFIGURATION = "configuration"
    CURRENCIES = "currencies"
    DATA = "data"
    INSIGHT = "insight"
    LINKS = "links"
    OBJECT_GROUPS = "object_groups"
    PIGGY_BANKS = "piggy_banks"
    PREFERENCES = "preferences"
    RECURRENCES = "recurrences"
    RULE_GROUPS = "rule_groups"
    RULES = "rules"
    SEARCH = "search"
    SUMMARY = "summary"
    TAGS = "tags"
    TRANSACTIONS = "transactions"
    USERS = "users"
    WEBHOOKS = "webhooks"
