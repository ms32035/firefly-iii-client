import typing_extensions

from firefly_iii_client.paths import PathValues
from firefly_iii_client.apis.paths.v1_about import V1About
from firefly_iii_client.apis.paths.v1_about_user import V1AboutUser
from firefly_iii_client.apis.paths.v1_accounts import V1Accounts
from firefly_iii_client.apis.paths.v1_accounts_id import V1AccountsId
from firefly_iii_client.apis.paths.v1_accounts_id_attachments import V1AccountsIdAttachments
from firefly_iii_client.apis.paths.v1_accounts_id_piggy_banks import V1AccountsIdPiggyBanks
from firefly_iii_client.apis.paths.v1_accounts_id_transactions import V1AccountsIdTransactions
from firefly_iii_client.apis.paths.v1_attachments import V1Attachments
from firefly_iii_client.apis.paths.v1_attachments_id import V1AttachmentsId
from firefly_iii_client.apis.paths.v1_attachments_id_download import V1AttachmentsIdDownload
from firefly_iii_client.apis.paths.v1_attachments_id_upload import V1AttachmentsIdUpload
from firefly_iii_client.apis.paths.v1_autocomplete_accounts import V1AutocompleteAccounts
from firefly_iii_client.apis.paths.v1_autocomplete_bills import V1AutocompleteBills
from firefly_iii_client.apis.paths.v1_autocomplete_budgets import V1AutocompleteBudgets
from firefly_iii_client.apis.paths.v1_autocomplete_categories import V1AutocompleteCategories
from firefly_iii_client.apis.paths.v1_autocomplete_currencies import V1AutocompleteCurrencies
from firefly_iii_client.apis.paths.v1_autocomplete_currencies_with_code import V1AutocompleteCurrenciesWithCode
from firefly_iii_client.apis.paths.v1_autocomplete_object_groups import V1AutocompleteObjectGroups
from firefly_iii_client.apis.paths.v1_autocomplete_piggy_banks import V1AutocompletePiggyBanks
from firefly_iii_client.apis.paths.v1_autocomplete_piggy_banks_with_balance import V1AutocompletePiggyBanksWithBalance
from firefly_iii_client.apis.paths.v1_autocomplete_recurring import V1AutocompleteRecurring
from firefly_iii_client.apis.paths.v1_autocomplete_rule_groups import V1AutocompleteRuleGroups
from firefly_iii_client.apis.paths.v1_autocomplete_rules import V1AutocompleteRules
from firefly_iii_client.apis.paths.v1_autocomplete_tags import V1AutocompleteTags
from firefly_iii_client.apis.paths.v1_autocomplete_transaction_types import V1AutocompleteTransactionTypes
from firefly_iii_client.apis.paths.v1_autocomplete_transactions import V1AutocompleteTransactions
from firefly_iii_client.apis.paths.v1_autocomplete_transactions_with_id import V1AutocompleteTransactionsWithId
from firefly_iii_client.apis.paths.v1_available_budgets import V1AvailableBudgets
from firefly_iii_client.apis.paths.v1_available_budgets_id import V1AvailableBudgetsId
from firefly_iii_client.apis.paths.v1_bills import V1Bills
from firefly_iii_client.apis.paths.v1_bills_id import V1BillsId
from firefly_iii_client.apis.paths.v1_bills_id_attachments import V1BillsIdAttachments
from firefly_iii_client.apis.paths.v1_bills_id_rules import V1BillsIdRules
from firefly_iii_client.apis.paths.v1_bills_id_transactions import V1BillsIdTransactions
from firefly_iii_client.apis.paths.v1_budget_limits import V1BudgetLimits
from firefly_iii_client.apis.paths.v1_budgets import V1Budgets
from firefly_iii_client.apis.paths.v1_budgets_id import V1BudgetsId
from firefly_iii_client.apis.paths.v1_budgets_id_attachments import V1BudgetsIdAttachments
from firefly_iii_client.apis.paths.v1_budgets_id_limits import V1BudgetsIdLimits
from firefly_iii_client.apis.paths.v1_budgets_id_limits_limit_id import V1BudgetsIdLimitsLimitId
from firefly_iii_client.apis.paths.v1_budgets_id_limits_limit_id_transactions import V1BudgetsIdLimitsLimitIdTransactions
from firefly_iii_client.apis.paths.v1_budgets_id_transactions import V1BudgetsIdTransactions
from firefly_iii_client.apis.paths.v1_categories import V1Categories
from firefly_iii_client.apis.paths.v1_categories_id import V1CategoriesId
from firefly_iii_client.apis.paths.v1_categories_id_attachments import V1CategoriesIdAttachments
from firefly_iii_client.apis.paths.v1_categories_id_transactions import V1CategoriesIdTransactions
from firefly_iii_client.apis.paths.v1_chart_account_overview import V1ChartAccountOverview
from firefly_iii_client.apis.paths.v1_configuration import V1Configuration
from firefly_iii_client.apis.paths.v1_configuration_name import V1ConfigurationName
from firefly_iii_client.apis.paths.v1_cron_cli_token import V1CronCliToken
from firefly_iii_client.apis.paths.v1_currencies import V1Currencies
from firefly_iii_client.apis.paths.v1_currencies_default import V1CurrenciesDefault
from firefly_iii_client.apis.paths.v1_currencies_code import V1CurrenciesCode
from firefly_iii_client.apis.paths.v1_currencies_code_accounts import V1CurrenciesCodeAccounts
from firefly_iii_client.apis.paths.v1_currencies_code_available_budgets import V1CurrenciesCodeAvailableBudgets
from firefly_iii_client.apis.paths.v1_currencies_code_bills import V1CurrenciesCodeBills
from firefly_iii_client.apis.paths.v1_currencies_code_budget_limits import V1CurrenciesCodeBudgetLimits
from firefly_iii_client.apis.paths.v1_currencies_code_default import V1CurrenciesCodeDefault
from firefly_iii_client.apis.paths.v1_currencies_code_disable import V1CurrenciesCodeDisable
from firefly_iii_client.apis.paths.v1_currencies_code_enable import V1CurrenciesCodeEnable
from firefly_iii_client.apis.paths.v1_currencies_code_recurrences import V1CurrenciesCodeRecurrences
from firefly_iii_client.apis.paths.v1_currencies_code_rules import V1CurrenciesCodeRules
from firefly_iii_client.apis.paths.v1_currencies_code_transactions import V1CurrenciesCodeTransactions
from firefly_iii_client.apis.paths.v1_data_bulk_transactions import V1DataBulkTransactions
from firefly_iii_client.apis.paths.v1_data_destroy import V1DataDestroy
from firefly_iii_client.apis.paths.v1_data_export_accounts import V1DataExportAccounts
from firefly_iii_client.apis.paths.v1_data_export_bills import V1DataExportBills
from firefly_iii_client.apis.paths.v1_data_export_budgets import V1DataExportBudgets
from firefly_iii_client.apis.paths.v1_data_export_categories import V1DataExportCategories
from firefly_iii_client.apis.paths.v1_data_export_piggy_banks import V1DataExportPiggyBanks
from firefly_iii_client.apis.paths.v1_data_export_recurring import V1DataExportRecurring
from firefly_iii_client.apis.paths.v1_data_export_rules import V1DataExportRules
from firefly_iii_client.apis.paths.v1_data_export_tags import V1DataExportTags
from firefly_iii_client.apis.paths.v1_data_export_transactions import V1DataExportTransactions
from firefly_iii_client.apis.paths.v1_data_purge import V1DataPurge
from firefly_iii_client.apis.paths.v1_insight_expense_asset import V1InsightExpenseAsset
from firefly_iii_client.apis.paths.v1_insight_expense_bill import V1InsightExpenseBill
from firefly_iii_client.apis.paths.v1_insight_expense_budget import V1InsightExpenseBudget
from firefly_iii_client.apis.paths.v1_insight_expense_category import V1InsightExpenseCategory
from firefly_iii_client.apis.paths.v1_insight_expense_expense import V1InsightExpenseExpense
from firefly_iii_client.apis.paths.v1_insight_expense_no_bill import V1InsightExpenseNoBill
from firefly_iii_client.apis.paths.v1_insight_expense_no_budget import V1InsightExpenseNoBudget
from firefly_iii_client.apis.paths.v1_insight_expense_no_category import V1InsightExpenseNoCategory
from firefly_iii_client.apis.paths.v1_insight_expense_no_tag import V1InsightExpenseNoTag
from firefly_iii_client.apis.paths.v1_insight_expense_tag import V1InsightExpenseTag
from firefly_iii_client.apis.paths.v1_insight_expense_total import V1InsightExpenseTotal
from firefly_iii_client.apis.paths.v1_insight_income_asset import V1InsightIncomeAsset
from firefly_iii_client.apis.paths.v1_insight_income_category import V1InsightIncomeCategory
from firefly_iii_client.apis.paths.v1_insight_income_no_category import V1InsightIncomeNoCategory
from firefly_iii_client.apis.paths.v1_insight_income_no_tag import V1InsightIncomeNoTag
from firefly_iii_client.apis.paths.v1_insight_income_revenue import V1InsightIncomeRevenue
from firefly_iii_client.apis.paths.v1_insight_income_tag import V1InsightIncomeTag
from firefly_iii_client.apis.paths.v1_insight_income_total import V1InsightIncomeTotal
from firefly_iii_client.apis.paths.v1_insight_transfer_asset import V1InsightTransferAsset
from firefly_iii_client.apis.paths.v1_insight_transfer_category import V1InsightTransferCategory
from firefly_iii_client.apis.paths.v1_insight_transfer_no_category import V1InsightTransferNoCategory
from firefly_iii_client.apis.paths.v1_insight_transfer_no_tag import V1InsightTransferNoTag
from firefly_iii_client.apis.paths.v1_insight_transfer_tag import V1InsightTransferTag
from firefly_iii_client.apis.paths.v1_insight_transfer_total import V1InsightTransferTotal
from firefly_iii_client.apis.paths.v1_link_types import V1LinkTypes
from firefly_iii_client.apis.paths.v1_link_types_id import V1LinkTypesId
from firefly_iii_client.apis.paths.v1_link_types_id_transactions import V1LinkTypesIdTransactions
from firefly_iii_client.apis.paths.v1_object_groups import V1ObjectGroups
from firefly_iii_client.apis.paths.v1_object_groups_id import V1ObjectGroupsId
from firefly_iii_client.apis.paths.v1_object_groups_id_bills import V1ObjectGroupsIdBills
from firefly_iii_client.apis.paths.v1_object_groups_id_piggy_banks import V1ObjectGroupsIdPiggyBanks
from firefly_iii_client.apis.paths.v1_piggy_banks import V1PiggyBanks
from firefly_iii_client.apis.paths.v1_piggy_banks_id import V1PiggyBanksId
from firefly_iii_client.apis.paths.v1_piggy_banks_id_attachments import V1PiggyBanksIdAttachments
from firefly_iii_client.apis.paths.v1_piggy_banks_id_events import V1PiggyBanksIdEvents
from firefly_iii_client.apis.paths.v1_preferences import V1Preferences
from firefly_iii_client.apis.paths.v1_preferences_name import V1PreferencesName
from firefly_iii_client.apis.paths.v1_recurrences import V1Recurrences
from firefly_iii_client.apis.paths.v1_recurrences_id import V1RecurrencesId
from firefly_iii_client.apis.paths.v1_recurrences_id_transactions import V1RecurrencesIdTransactions
from firefly_iii_client.apis.paths.v1_rule_groups import V1RuleGroups
from firefly_iii_client.apis.paths.v1_rule_groups_id import V1RuleGroupsId
from firefly_iii_client.apis.paths.v1_rule_groups_id_rules import V1RuleGroupsIdRules
from firefly_iii_client.apis.paths.v1_rule_groups_id_test import V1RuleGroupsIdTest
from firefly_iii_client.apis.paths.v1_rule_groups_id_trigger import V1RuleGroupsIdTrigger
from firefly_iii_client.apis.paths.v1_rules import V1Rules
from firefly_iii_client.apis.paths.v1_rules_id import V1RulesId
from firefly_iii_client.apis.paths.v1_rules_id_test import V1RulesIdTest
from firefly_iii_client.apis.paths.v1_rules_id_trigger import V1RulesIdTrigger
from firefly_iii_client.apis.paths.v1_search_accounts import V1SearchAccounts
from firefly_iii_client.apis.paths.v1_search_transactions import V1SearchTransactions
from firefly_iii_client.apis.paths.v1_summary_basic import V1SummaryBasic
from firefly_iii_client.apis.paths.v1_tags import V1Tags
from firefly_iii_client.apis.paths.v1_tags_tag import V1TagsTag
from firefly_iii_client.apis.paths.v1_tags_tag_attachments import V1TagsTagAttachments
from firefly_iii_client.apis.paths.v1_tags_tag_transactions import V1TagsTagTransactions
from firefly_iii_client.apis.paths.v1_transaction_journals_id import V1TransactionJournalsId
from firefly_iii_client.apis.paths.v1_transaction_journals_id_links import V1TransactionJournalsIdLinks
from firefly_iii_client.apis.paths.v1_transaction_links import V1TransactionLinks
from firefly_iii_client.apis.paths.v1_transaction_links_id import V1TransactionLinksId
from firefly_iii_client.apis.paths.v1_transactions import V1Transactions
from firefly_iii_client.apis.paths.v1_transactions_id import V1TransactionsId
from firefly_iii_client.apis.paths.v1_transactions_id_attachments import V1TransactionsIdAttachments
from firefly_iii_client.apis.paths.v1_transactions_id_piggy_bank_events import V1TransactionsIdPiggyBankEvents
from firefly_iii_client.apis.paths.v1_users import V1Users
from firefly_iii_client.apis.paths.v1_users_id import V1UsersId
from firefly_iii_client.apis.paths.v1_webhooks import V1Webhooks
from firefly_iii_client.apis.paths.v1_webhooks_id import V1WebhooksId
from firefly_iii_client.apis.paths.v1_webhooks_id_messages import V1WebhooksIdMessages
from firefly_iii_client.apis.paths.v1_webhooks_id_messages_message_id import V1WebhooksIdMessagesMessageId
from firefly_iii_client.apis.paths.v1_webhooks_id_messages_message_id_attempts import V1WebhooksIdMessagesMessageIdAttempts
from firefly_iii_client.apis.paths.v1_webhooks_id_messages_message_id_attempts_attempt_id import V1WebhooksIdMessagesMessageIdAttemptsAttemptId
from firefly_iii_client.apis.paths.v1_webhooks_id_submit import V1WebhooksIdSubmit

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V1_ABOUT: V1About,
        PathValues.V1_ABOUT_USER: V1AboutUser,
        PathValues.V1_ACCOUNTS: V1Accounts,
        PathValues.V1_ACCOUNTS_ID: V1AccountsId,
        PathValues.V1_ACCOUNTS_ID_ATTACHMENTS: V1AccountsIdAttachments,
        PathValues.V1_ACCOUNTS_ID_PIGGYBANKS: V1AccountsIdPiggyBanks,
        PathValues.V1_ACCOUNTS_ID_TRANSACTIONS: V1AccountsIdTransactions,
        PathValues.V1_ATTACHMENTS: V1Attachments,
        PathValues.V1_ATTACHMENTS_ID: V1AttachmentsId,
        PathValues.V1_ATTACHMENTS_ID_DOWNLOAD: V1AttachmentsIdDownload,
        PathValues.V1_ATTACHMENTS_ID_UPLOAD: V1AttachmentsIdUpload,
        PathValues.V1_AUTOCOMPLETE_ACCOUNTS: V1AutocompleteAccounts,
        PathValues.V1_AUTOCOMPLETE_BILLS: V1AutocompleteBills,
        PathValues.V1_AUTOCOMPLETE_BUDGETS: V1AutocompleteBudgets,
        PathValues.V1_AUTOCOMPLETE_CATEGORIES: V1AutocompleteCategories,
        PathValues.V1_AUTOCOMPLETE_CURRENCIES: V1AutocompleteCurrencies,
        PathValues.V1_AUTOCOMPLETE_CURRENCIESWITHCODE: V1AutocompleteCurrenciesWithCode,
        PathValues.V1_AUTOCOMPLETE_OBJECTGROUPS: V1AutocompleteObjectGroups,
        PathValues.V1_AUTOCOMPLETE_PIGGYBANKS: V1AutocompletePiggyBanks,
        PathValues.V1_AUTOCOMPLETE_PIGGYBANKSWITHBALANCE: V1AutocompletePiggyBanksWithBalance,
        PathValues.V1_AUTOCOMPLETE_RECURRING: V1AutocompleteRecurring,
        PathValues.V1_AUTOCOMPLETE_RULEGROUPS: V1AutocompleteRuleGroups,
        PathValues.V1_AUTOCOMPLETE_RULES: V1AutocompleteRules,
        PathValues.V1_AUTOCOMPLETE_TAGS: V1AutocompleteTags,
        PathValues.V1_AUTOCOMPLETE_TRANSACTIONTYPES: V1AutocompleteTransactionTypes,
        PathValues.V1_AUTOCOMPLETE_TRANSACTIONS: V1AutocompleteTransactions,
        PathValues.V1_AUTOCOMPLETE_TRANSACTIONSWITHID: V1AutocompleteTransactionsWithId,
        PathValues.V1_AVAILABLEBUDGETS: V1AvailableBudgets,
        PathValues.V1_AVAILABLEBUDGETS_ID: V1AvailableBudgetsId,
        PathValues.V1_BILLS: V1Bills,
        PathValues.V1_BILLS_ID: V1BillsId,
        PathValues.V1_BILLS_ID_ATTACHMENTS: V1BillsIdAttachments,
        PathValues.V1_BILLS_ID_RULES: V1BillsIdRules,
        PathValues.V1_BILLS_ID_TRANSACTIONS: V1BillsIdTransactions,
        PathValues.V1_BUDGETLIMITS: V1BudgetLimits,
        PathValues.V1_BUDGETS: V1Budgets,
        PathValues.V1_BUDGETS_ID: V1BudgetsId,
        PathValues.V1_BUDGETS_ID_ATTACHMENTS: V1BudgetsIdAttachments,
        PathValues.V1_BUDGETS_ID_LIMITS: V1BudgetsIdLimits,
        PathValues.V1_BUDGETS_ID_LIMITS_LIMIT_ID: V1BudgetsIdLimitsLimitId,
        PathValues.V1_BUDGETS_ID_LIMITS_LIMIT_ID_TRANSACTIONS: V1BudgetsIdLimitsLimitIdTransactions,
        PathValues.V1_BUDGETS_ID_TRANSACTIONS: V1BudgetsIdTransactions,
        PathValues.V1_CATEGORIES: V1Categories,
        PathValues.V1_CATEGORIES_ID: V1CategoriesId,
        PathValues.V1_CATEGORIES_ID_ATTACHMENTS: V1CategoriesIdAttachments,
        PathValues.V1_CATEGORIES_ID_TRANSACTIONS: V1CategoriesIdTransactions,
        PathValues.V1_CHART_ACCOUNT_OVERVIEW: V1ChartAccountOverview,
        PathValues.V1_CONFIGURATION: V1Configuration,
        PathValues.V1_CONFIGURATION_NAME: V1ConfigurationName,
        PathValues.V1_CRON_CLI_TOKEN: V1CronCliToken,
        PathValues.V1_CURRENCIES: V1Currencies,
        PathValues.V1_CURRENCIES_DEFAULT: V1CurrenciesDefault,
        PathValues.V1_CURRENCIES_CODE: V1CurrenciesCode,
        PathValues.V1_CURRENCIES_CODE_ACCOUNTS: V1CurrenciesCodeAccounts,
        PathValues.V1_CURRENCIES_CODE_AVAILABLEBUDGETS: V1CurrenciesCodeAvailableBudgets,
        PathValues.V1_CURRENCIES_CODE_BILLS: V1CurrenciesCodeBills,
        PathValues.V1_CURRENCIES_CODE_BUDGET_LIMITS: V1CurrenciesCodeBudgetLimits,
        PathValues.V1_CURRENCIES_CODE_DEFAULT: V1CurrenciesCodeDefault,
        PathValues.V1_CURRENCIES_CODE_DISABLE: V1CurrenciesCodeDisable,
        PathValues.V1_CURRENCIES_CODE_ENABLE: V1CurrenciesCodeEnable,
        PathValues.V1_CURRENCIES_CODE_RECURRENCES: V1CurrenciesCodeRecurrences,
        PathValues.V1_CURRENCIES_CODE_RULES: V1CurrenciesCodeRules,
        PathValues.V1_CURRENCIES_CODE_TRANSACTIONS: V1CurrenciesCodeTransactions,
        PathValues.V1_DATA_BULK_TRANSACTIONS: V1DataBulkTransactions,
        PathValues.V1_DATA_DESTROY: V1DataDestroy,
        PathValues.V1_DATA_EXPORT_ACCOUNTS: V1DataExportAccounts,
        PathValues.V1_DATA_EXPORT_BILLS: V1DataExportBills,
        PathValues.V1_DATA_EXPORT_BUDGETS: V1DataExportBudgets,
        PathValues.V1_DATA_EXPORT_CATEGORIES: V1DataExportCategories,
        PathValues.V1_DATA_EXPORT_PIGGYBANKS: V1DataExportPiggyBanks,
        PathValues.V1_DATA_EXPORT_RECURRING: V1DataExportRecurring,
        PathValues.V1_DATA_EXPORT_RULES: V1DataExportRules,
        PathValues.V1_DATA_EXPORT_TAGS: V1DataExportTags,
        PathValues.V1_DATA_EXPORT_TRANSACTIONS: V1DataExportTransactions,
        PathValues.V1_DATA_PURGE: V1DataPurge,
        PathValues.V1_INSIGHT_EXPENSE_ASSET: V1InsightExpenseAsset,
        PathValues.V1_INSIGHT_EXPENSE_BILL: V1InsightExpenseBill,
        PathValues.V1_INSIGHT_EXPENSE_BUDGET: V1InsightExpenseBudget,
        PathValues.V1_INSIGHT_EXPENSE_CATEGORY: V1InsightExpenseCategory,
        PathValues.V1_INSIGHT_EXPENSE_EXPENSE: V1InsightExpenseExpense,
        PathValues.V1_INSIGHT_EXPENSE_NOBILL: V1InsightExpenseNoBill,
        PathValues.V1_INSIGHT_EXPENSE_NOBUDGET: V1InsightExpenseNoBudget,
        PathValues.V1_INSIGHT_EXPENSE_NOCATEGORY: V1InsightExpenseNoCategory,
        PathValues.V1_INSIGHT_EXPENSE_NOTAG: V1InsightExpenseNoTag,
        PathValues.V1_INSIGHT_EXPENSE_TAG: V1InsightExpenseTag,
        PathValues.V1_INSIGHT_EXPENSE_TOTAL: V1InsightExpenseTotal,
        PathValues.V1_INSIGHT_INCOME_ASSET: V1InsightIncomeAsset,
        PathValues.V1_INSIGHT_INCOME_CATEGORY: V1InsightIncomeCategory,
        PathValues.V1_INSIGHT_INCOME_NOCATEGORY: V1InsightIncomeNoCategory,
        PathValues.V1_INSIGHT_INCOME_NOTAG: V1InsightIncomeNoTag,
        PathValues.V1_INSIGHT_INCOME_REVENUE: V1InsightIncomeRevenue,
        PathValues.V1_INSIGHT_INCOME_TAG: V1InsightIncomeTag,
        PathValues.V1_INSIGHT_INCOME_TOTAL: V1InsightIncomeTotal,
        PathValues.V1_INSIGHT_TRANSFER_ASSET: V1InsightTransferAsset,
        PathValues.V1_INSIGHT_TRANSFER_CATEGORY: V1InsightTransferCategory,
        PathValues.V1_INSIGHT_TRANSFER_NOCATEGORY: V1InsightTransferNoCategory,
        PathValues.V1_INSIGHT_TRANSFER_NOTAG: V1InsightTransferNoTag,
        PathValues.V1_INSIGHT_TRANSFER_TAG: V1InsightTransferTag,
        PathValues.V1_INSIGHT_TRANSFER_TOTAL: V1InsightTransferTotal,
        PathValues.V1_LINKTYPES: V1LinkTypes,
        PathValues.V1_LINKTYPES_ID: V1LinkTypesId,
        PathValues.V1_LINKTYPES_ID_TRANSACTIONS: V1LinkTypesIdTransactions,
        PathValues.V1_OBJECTGROUPS: V1ObjectGroups,
        PathValues.V1_OBJECTGROUPS_ID: V1ObjectGroupsId,
        PathValues.V1_OBJECTGROUPS_ID_BILLS: V1ObjectGroupsIdBills,
        PathValues.V1_OBJECTGROUPS_ID_PIGGYBANKS: V1ObjectGroupsIdPiggyBanks,
        PathValues.V1_PIGGYBANKS: V1PiggyBanks,
        PathValues.V1_PIGGYBANKS_ID: V1PiggyBanksId,
        PathValues.V1_PIGGYBANKS_ID_ATTACHMENTS: V1PiggyBanksIdAttachments,
        PathValues.V1_PIGGYBANKS_ID_EVENTS: V1PiggyBanksIdEvents,
        PathValues.V1_PREFERENCES: V1Preferences,
        PathValues.V1_PREFERENCES_NAME: V1PreferencesName,
        PathValues.V1_RECURRENCES: V1Recurrences,
        PathValues.V1_RECURRENCES_ID: V1RecurrencesId,
        PathValues.V1_RECURRENCES_ID_TRANSACTIONS: V1RecurrencesIdTransactions,
        PathValues.V1_RULEGROUPS: V1RuleGroups,
        PathValues.V1_RULEGROUPS_ID: V1RuleGroupsId,
        PathValues.V1_RULEGROUPS_ID_RULES: V1RuleGroupsIdRules,
        PathValues.V1_RULEGROUPS_ID_TEST: V1RuleGroupsIdTest,
        PathValues.V1_RULEGROUPS_ID_TRIGGER: V1RuleGroupsIdTrigger,
        PathValues.V1_RULES: V1Rules,
        PathValues.V1_RULES_ID: V1RulesId,
        PathValues.V1_RULES_ID_TEST: V1RulesIdTest,
        PathValues.V1_RULES_ID_TRIGGER: V1RulesIdTrigger,
        PathValues.V1_SEARCH_ACCOUNTS: V1SearchAccounts,
        PathValues.V1_SEARCH_TRANSACTIONS: V1SearchTransactions,
        PathValues.V1_SUMMARY_BASIC: V1SummaryBasic,
        PathValues.V1_TAGS: V1Tags,
        PathValues.V1_TAGS_TAG: V1TagsTag,
        PathValues.V1_TAGS_TAG_ATTACHMENTS: V1TagsTagAttachments,
        PathValues.V1_TAGS_TAG_TRANSACTIONS: V1TagsTagTransactions,
        PathValues.V1_TRANSACTIONJOURNALS_ID: V1TransactionJournalsId,
        PathValues.V1_TRANSACTIONJOURNALS_ID_LINKS: V1TransactionJournalsIdLinks,
        PathValues.V1_TRANSACTIONLINKS: V1TransactionLinks,
        PathValues.V1_TRANSACTIONLINKS_ID: V1TransactionLinksId,
        PathValues.V1_TRANSACTIONS: V1Transactions,
        PathValues.V1_TRANSACTIONS_ID: V1TransactionsId,
        PathValues.V1_TRANSACTIONS_ID_ATTACHMENTS: V1TransactionsIdAttachments,
        PathValues.V1_TRANSACTIONS_ID_PIGGYBANKEVENTS: V1TransactionsIdPiggyBankEvents,
        PathValues.V1_USERS: V1Users,
        PathValues.V1_USERS_ID: V1UsersId,
        PathValues.V1_WEBHOOKS: V1Webhooks,
        PathValues.V1_WEBHOOKS_ID: V1WebhooksId,
        PathValues.V1_WEBHOOKS_ID_MESSAGES: V1WebhooksIdMessages,
        PathValues.V1_WEBHOOKS_ID_MESSAGES_MESSAGE_ID: V1WebhooksIdMessagesMessageId,
        PathValues.V1_WEBHOOKS_ID_MESSAGES_MESSAGE_ID_ATTEMPTS: V1WebhooksIdMessagesMessageIdAttempts,
        PathValues.V1_WEBHOOKS_ID_MESSAGES_MESSAGE_ID_ATTEMPTS_ATTEMPT_ID: V1WebhooksIdMessagesMessageIdAttemptsAttemptId,
        PathValues.V1_WEBHOOKS_ID_SUBMIT: V1WebhooksIdSubmit,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V1_ABOUT: V1About,
        PathValues.V1_ABOUT_USER: V1AboutUser,
        PathValues.V1_ACCOUNTS: V1Accounts,
        PathValues.V1_ACCOUNTS_ID: V1AccountsId,
        PathValues.V1_ACCOUNTS_ID_ATTACHMENTS: V1AccountsIdAttachments,
        PathValues.V1_ACCOUNTS_ID_PIGGYBANKS: V1AccountsIdPiggyBanks,
        PathValues.V1_ACCOUNTS_ID_TRANSACTIONS: V1AccountsIdTransactions,
        PathValues.V1_ATTACHMENTS: V1Attachments,
        PathValues.V1_ATTACHMENTS_ID: V1AttachmentsId,
        PathValues.V1_ATTACHMENTS_ID_DOWNLOAD: V1AttachmentsIdDownload,
        PathValues.V1_ATTACHMENTS_ID_UPLOAD: V1AttachmentsIdUpload,
        PathValues.V1_AUTOCOMPLETE_ACCOUNTS: V1AutocompleteAccounts,
        PathValues.V1_AUTOCOMPLETE_BILLS: V1AutocompleteBills,
        PathValues.V1_AUTOCOMPLETE_BUDGETS: V1AutocompleteBudgets,
        PathValues.V1_AUTOCOMPLETE_CATEGORIES: V1AutocompleteCategories,
        PathValues.V1_AUTOCOMPLETE_CURRENCIES: V1AutocompleteCurrencies,
        PathValues.V1_AUTOCOMPLETE_CURRENCIESWITHCODE: V1AutocompleteCurrenciesWithCode,
        PathValues.V1_AUTOCOMPLETE_OBJECTGROUPS: V1AutocompleteObjectGroups,
        PathValues.V1_AUTOCOMPLETE_PIGGYBANKS: V1AutocompletePiggyBanks,
        PathValues.V1_AUTOCOMPLETE_PIGGYBANKSWITHBALANCE: V1AutocompletePiggyBanksWithBalance,
        PathValues.V1_AUTOCOMPLETE_RECURRING: V1AutocompleteRecurring,
        PathValues.V1_AUTOCOMPLETE_RULEGROUPS: V1AutocompleteRuleGroups,
        PathValues.V1_AUTOCOMPLETE_RULES: V1AutocompleteRules,
        PathValues.V1_AUTOCOMPLETE_TAGS: V1AutocompleteTags,
        PathValues.V1_AUTOCOMPLETE_TRANSACTIONTYPES: V1AutocompleteTransactionTypes,
        PathValues.V1_AUTOCOMPLETE_TRANSACTIONS: V1AutocompleteTransactions,
        PathValues.V1_AUTOCOMPLETE_TRANSACTIONSWITHID: V1AutocompleteTransactionsWithId,
        PathValues.V1_AVAILABLEBUDGETS: V1AvailableBudgets,
        PathValues.V1_AVAILABLEBUDGETS_ID: V1AvailableBudgetsId,
        PathValues.V1_BILLS: V1Bills,
        PathValues.V1_BILLS_ID: V1BillsId,
        PathValues.V1_BILLS_ID_ATTACHMENTS: V1BillsIdAttachments,
        PathValues.V1_BILLS_ID_RULES: V1BillsIdRules,
        PathValues.V1_BILLS_ID_TRANSACTIONS: V1BillsIdTransactions,
        PathValues.V1_BUDGETLIMITS: V1BudgetLimits,
        PathValues.V1_BUDGETS: V1Budgets,
        PathValues.V1_BUDGETS_ID: V1BudgetsId,
        PathValues.V1_BUDGETS_ID_ATTACHMENTS: V1BudgetsIdAttachments,
        PathValues.V1_BUDGETS_ID_LIMITS: V1BudgetsIdLimits,
        PathValues.V1_BUDGETS_ID_LIMITS_LIMIT_ID: V1BudgetsIdLimitsLimitId,
        PathValues.V1_BUDGETS_ID_LIMITS_LIMIT_ID_TRANSACTIONS: V1BudgetsIdLimitsLimitIdTransactions,
        PathValues.V1_BUDGETS_ID_TRANSACTIONS: V1BudgetsIdTransactions,
        PathValues.V1_CATEGORIES: V1Categories,
        PathValues.V1_CATEGORIES_ID: V1CategoriesId,
        PathValues.V1_CATEGORIES_ID_ATTACHMENTS: V1CategoriesIdAttachments,
        PathValues.V1_CATEGORIES_ID_TRANSACTIONS: V1CategoriesIdTransactions,
        PathValues.V1_CHART_ACCOUNT_OVERVIEW: V1ChartAccountOverview,
        PathValues.V1_CONFIGURATION: V1Configuration,
        PathValues.V1_CONFIGURATION_NAME: V1ConfigurationName,
        PathValues.V1_CRON_CLI_TOKEN: V1CronCliToken,
        PathValues.V1_CURRENCIES: V1Currencies,
        PathValues.V1_CURRENCIES_DEFAULT: V1CurrenciesDefault,
        PathValues.V1_CURRENCIES_CODE: V1CurrenciesCode,
        PathValues.V1_CURRENCIES_CODE_ACCOUNTS: V1CurrenciesCodeAccounts,
        PathValues.V1_CURRENCIES_CODE_AVAILABLEBUDGETS: V1CurrenciesCodeAvailableBudgets,
        PathValues.V1_CURRENCIES_CODE_BILLS: V1CurrenciesCodeBills,
        PathValues.V1_CURRENCIES_CODE_BUDGET_LIMITS: V1CurrenciesCodeBudgetLimits,
        PathValues.V1_CURRENCIES_CODE_DEFAULT: V1CurrenciesCodeDefault,
        PathValues.V1_CURRENCIES_CODE_DISABLE: V1CurrenciesCodeDisable,
        PathValues.V1_CURRENCIES_CODE_ENABLE: V1CurrenciesCodeEnable,
        PathValues.V1_CURRENCIES_CODE_RECURRENCES: V1CurrenciesCodeRecurrences,
        PathValues.V1_CURRENCIES_CODE_RULES: V1CurrenciesCodeRules,
        PathValues.V1_CURRENCIES_CODE_TRANSACTIONS: V1CurrenciesCodeTransactions,
        PathValues.V1_DATA_BULK_TRANSACTIONS: V1DataBulkTransactions,
        PathValues.V1_DATA_DESTROY: V1DataDestroy,
        PathValues.V1_DATA_EXPORT_ACCOUNTS: V1DataExportAccounts,
        PathValues.V1_DATA_EXPORT_BILLS: V1DataExportBills,
        PathValues.V1_DATA_EXPORT_BUDGETS: V1DataExportBudgets,
        PathValues.V1_DATA_EXPORT_CATEGORIES: V1DataExportCategories,
        PathValues.V1_DATA_EXPORT_PIGGYBANKS: V1DataExportPiggyBanks,
        PathValues.V1_DATA_EXPORT_RECURRING: V1DataExportRecurring,
        PathValues.V1_DATA_EXPORT_RULES: V1DataExportRules,
        PathValues.V1_DATA_EXPORT_TAGS: V1DataExportTags,
        PathValues.V1_DATA_EXPORT_TRANSACTIONS: V1DataExportTransactions,
        PathValues.V1_DATA_PURGE: V1DataPurge,
        PathValues.V1_INSIGHT_EXPENSE_ASSET: V1InsightExpenseAsset,
        PathValues.V1_INSIGHT_EXPENSE_BILL: V1InsightExpenseBill,
        PathValues.V1_INSIGHT_EXPENSE_BUDGET: V1InsightExpenseBudget,
        PathValues.V1_INSIGHT_EXPENSE_CATEGORY: V1InsightExpenseCategory,
        PathValues.V1_INSIGHT_EXPENSE_EXPENSE: V1InsightExpenseExpense,
        PathValues.V1_INSIGHT_EXPENSE_NOBILL: V1InsightExpenseNoBill,
        PathValues.V1_INSIGHT_EXPENSE_NOBUDGET: V1InsightExpenseNoBudget,
        PathValues.V1_INSIGHT_EXPENSE_NOCATEGORY: V1InsightExpenseNoCategory,
        PathValues.V1_INSIGHT_EXPENSE_NOTAG: V1InsightExpenseNoTag,
        PathValues.V1_INSIGHT_EXPENSE_TAG: V1InsightExpenseTag,
        PathValues.V1_INSIGHT_EXPENSE_TOTAL: V1InsightExpenseTotal,
        PathValues.V1_INSIGHT_INCOME_ASSET: V1InsightIncomeAsset,
        PathValues.V1_INSIGHT_INCOME_CATEGORY: V1InsightIncomeCategory,
        PathValues.V1_INSIGHT_INCOME_NOCATEGORY: V1InsightIncomeNoCategory,
        PathValues.V1_INSIGHT_INCOME_NOTAG: V1InsightIncomeNoTag,
        PathValues.V1_INSIGHT_INCOME_REVENUE: V1InsightIncomeRevenue,
        PathValues.V1_INSIGHT_INCOME_TAG: V1InsightIncomeTag,
        PathValues.V1_INSIGHT_INCOME_TOTAL: V1InsightIncomeTotal,
        PathValues.V1_INSIGHT_TRANSFER_ASSET: V1InsightTransferAsset,
        PathValues.V1_INSIGHT_TRANSFER_CATEGORY: V1InsightTransferCategory,
        PathValues.V1_INSIGHT_TRANSFER_NOCATEGORY: V1InsightTransferNoCategory,
        PathValues.V1_INSIGHT_TRANSFER_NOTAG: V1InsightTransferNoTag,
        PathValues.V1_INSIGHT_TRANSFER_TAG: V1InsightTransferTag,
        PathValues.V1_INSIGHT_TRANSFER_TOTAL: V1InsightTransferTotal,
        PathValues.V1_LINKTYPES: V1LinkTypes,
        PathValues.V1_LINKTYPES_ID: V1LinkTypesId,
        PathValues.V1_LINKTYPES_ID_TRANSACTIONS: V1LinkTypesIdTransactions,
        PathValues.V1_OBJECTGROUPS: V1ObjectGroups,
        PathValues.V1_OBJECTGROUPS_ID: V1ObjectGroupsId,
        PathValues.V1_OBJECTGROUPS_ID_BILLS: V1ObjectGroupsIdBills,
        PathValues.V1_OBJECTGROUPS_ID_PIGGYBANKS: V1ObjectGroupsIdPiggyBanks,
        PathValues.V1_PIGGYBANKS: V1PiggyBanks,
        PathValues.V1_PIGGYBANKS_ID: V1PiggyBanksId,
        PathValues.V1_PIGGYBANKS_ID_ATTACHMENTS: V1PiggyBanksIdAttachments,
        PathValues.V1_PIGGYBANKS_ID_EVENTS: V1PiggyBanksIdEvents,
        PathValues.V1_PREFERENCES: V1Preferences,
        PathValues.V1_PREFERENCES_NAME: V1PreferencesName,
        PathValues.V1_RECURRENCES: V1Recurrences,
        PathValues.V1_RECURRENCES_ID: V1RecurrencesId,
        PathValues.V1_RECURRENCES_ID_TRANSACTIONS: V1RecurrencesIdTransactions,
        PathValues.V1_RULEGROUPS: V1RuleGroups,
        PathValues.V1_RULEGROUPS_ID: V1RuleGroupsId,
        PathValues.V1_RULEGROUPS_ID_RULES: V1RuleGroupsIdRules,
        PathValues.V1_RULEGROUPS_ID_TEST: V1RuleGroupsIdTest,
        PathValues.V1_RULEGROUPS_ID_TRIGGER: V1RuleGroupsIdTrigger,
        PathValues.V1_RULES: V1Rules,
        PathValues.V1_RULES_ID: V1RulesId,
        PathValues.V1_RULES_ID_TEST: V1RulesIdTest,
        PathValues.V1_RULES_ID_TRIGGER: V1RulesIdTrigger,
        PathValues.V1_SEARCH_ACCOUNTS: V1SearchAccounts,
        PathValues.V1_SEARCH_TRANSACTIONS: V1SearchTransactions,
        PathValues.V1_SUMMARY_BASIC: V1SummaryBasic,
        PathValues.V1_TAGS: V1Tags,
        PathValues.V1_TAGS_TAG: V1TagsTag,
        PathValues.V1_TAGS_TAG_ATTACHMENTS: V1TagsTagAttachments,
        PathValues.V1_TAGS_TAG_TRANSACTIONS: V1TagsTagTransactions,
        PathValues.V1_TRANSACTIONJOURNALS_ID: V1TransactionJournalsId,
        PathValues.V1_TRANSACTIONJOURNALS_ID_LINKS: V1TransactionJournalsIdLinks,
        PathValues.V1_TRANSACTIONLINKS: V1TransactionLinks,
        PathValues.V1_TRANSACTIONLINKS_ID: V1TransactionLinksId,
        PathValues.V1_TRANSACTIONS: V1Transactions,
        PathValues.V1_TRANSACTIONS_ID: V1TransactionsId,
        PathValues.V1_TRANSACTIONS_ID_ATTACHMENTS: V1TransactionsIdAttachments,
        PathValues.V1_TRANSACTIONS_ID_PIGGYBANKEVENTS: V1TransactionsIdPiggyBankEvents,
        PathValues.V1_USERS: V1Users,
        PathValues.V1_USERS_ID: V1UsersId,
        PathValues.V1_WEBHOOKS: V1Webhooks,
        PathValues.V1_WEBHOOKS_ID: V1WebhooksId,
        PathValues.V1_WEBHOOKS_ID_MESSAGES: V1WebhooksIdMessages,
        PathValues.V1_WEBHOOKS_ID_MESSAGES_MESSAGE_ID: V1WebhooksIdMessagesMessageId,
        PathValues.V1_WEBHOOKS_ID_MESSAGES_MESSAGE_ID_ATTEMPTS: V1WebhooksIdMessagesMessageIdAttempts,
        PathValues.V1_WEBHOOKS_ID_MESSAGES_MESSAGE_ID_ATTEMPTS_ATTEMPT_ID: V1WebhooksIdMessagesMessageIdAttemptsAttemptId,
        PathValues.V1_WEBHOOKS_ID_SUBMIT: V1WebhooksIdSubmit,
    }
)
