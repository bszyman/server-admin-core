from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class MailStores(BaseModel):
    id: str = ""
    partition_name: str = ""
    partition_location: str = ""


class MailingListMember(BaseModel):
    email_address: str
    subscribe: bool = True
    post: bool = True
    admin: bool = False


class MailingList(BaseModel):
    list_name: str = ""
    admin_user: str = ""
    users_may_self_subscribe: bool = False
    default_language: str = "1"
    lang_support_en: bool = True
    lang_support_fr: bool = False
    lang_support_de: bool = False
    lang_support_jp: bool = False
    lang_support_kr: bool = False
    lang_support_ru: bool = False
    lang_support_es: bool = False
    max_body_length_kb: int = 40
    members: Optional[List[MailingListMember]] = []


class MailSettings(BaseModel):
    # Settings - General
    enable_pop: bool = True
    enable_imap: bool = True
    imax_max_connections: int = 0
    var_mail_when_pop_imap_disabled: bool = False
    enable_smtp: bool = True
    allow_incoming_mail: bool = True
    smtp_domain_name: str = "localhost"
    smtp_hostname: str = "localhost"
    hold_outgoing_mail: bool = False
    relay_outgoing_mail: bool = False
    relay_outgoing_mail_host: str
    copy_undeliverable_mail: bool = False
    copy_undeliverable_mail_host: str
    copy_all_mail: bool = False
    copy_all_mail_host: str

    # Settings - Relay
    accept_smtp_relays: bool = True
    smtp_relays: Optional[List[str]] = []
    refuse_messages: bool = True
    refuse_messages_networks: Optional[List[str]] = []
    use_junkmail_rejection_servers: bool = True
    junkmail_rejection_servers: Optional[List[str]] = []

    # Settings - Filters
    scan_email_for_junk_mail: bool = False
    junk_mail_score: int = 5
    accepted_languages: Optional[List[int]] = []
    accepted_locales: Optional[List[str]] = []
    junk_mail_message_action: int = 1
    attach_subject_tag: bool = False
    subject_tag: str = "*** JUNK MAIL ***"
    encapsulate_junk_mail_as_mime: bool = False
    scan_email_for_viruses: bool = False
    infected_message_action: int = 1
    send_notifications: bool = False
    sent_notifications_to: str = "virus-admin@example.com"
    virus_notify_recipients: bool = False
    update_junk_and_virus_database: bool = False
    update_junk_and_virus_database_frequency: int = 1

    # Settings - Quotas
    refuse_incoming_messages: bool = True
    refuse_incoming_messages_size: int = 10
    disable_user_if_over_quota: bool = False
    over_quota_error_message: str = "[Error] Email server usage has exceeded quota"
    enable_quota_warnings: bool = False
    quota_warning_message: str = "[Warning] Email server usages is approaching quota"
    send_quota_warnings_percent: int = 90
    send_quota_warning_frequency_days: int = 1

    # Settings - Mailing Lists
    enable_mailing_lists: bool = False
    mailing_lists: Optional[List[MailingList]] = []

    # Settings - Logging
    smtp_log_detail_level: int = 1
    imap_pop_log_detail_level: int = 1
    junk_virus_log_detail_level: int = 1
    archive_logs: bool = False
    archive_logs_frequency_days: int = 1

    # Settings - Advanced
    smtp_kerberos: bool = False
    smtp_crammd5: bool = False
    smtp_login: bool = False
    smtp_plain: bool = False
    imap_kerberos: bool = False
    imap_crammd5: bool = False
    imap_login: bool = False
    imap_plain: bool = False
    imap_clear: bool = True
    pop_kerberos: bool = False
    pop_apop: bool = False
    pop_clear: bool = True
    smtp_ssl_mode: int = 1
    smtp_ssl_configuration: int = 1
    imap_pop_ssl_mode: int = 1
    imap_pip_ssl_configuration: int = 1

    localhost_aliases: Optional[List[str]] = []
    enable_virtual_hosting: bool = False
    locally_hosted_virtual_domains: Optional[List[str]] = []

    database_location: str = ""
    mail_store_location: str = ""
    additional_mail_stores: Optional[List[MailStores]] = []


class MailConnection(BaseModel):
    username: str
    address: str
    type: int
    sessions: int
    connection_length: int


class MailService(BaseModel):
    running: bool = False
    start_time: Optional[datetime]
