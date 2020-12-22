from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime, date


class OpenDirectorySettings(BaseModel):
    # Settings - General
    role: int = 1

    # Settings - Protocols
    configure: int = 1
    search_base: str
    database: str
    max_search_results: int = 500
    search_time_out: int = 1
    search_time_out_unit: int = 1
    enable_ldap_ssl: bool = False
    certificate: Optional[int]

    auth_disable_on_date: Optional[date]
    auth_disable_after_date: Optional[int]
    auth_disable_inactive_days: Optional[int]
    auth_disable_failed_attempts: Optional[int]

    pass_differ_account_name: bool = False
    pass_contain_one_letter: bool = False
    pass_contain_one_number: bool = False
    pass_reset_first_login: bool = False
    pass_contain_characters: bool = False
    pass_contain_num_characters: Optional[int]
    pass_differ_from_last: bool = False
    pass_differ_from_last_number_used: Optional[int]
    pass_be_reset: Optional[int]
    pass_be_reset_unit: int = 1

    enable_directory_binding: bool = False
    require_clients_to_bind: bool = False
    disable_clear_text_passwords: bool = False
    digitally_sign_all_packets: bool = False
    encrypt_all_packets: bool = False
    block_mitm_attacks: bool = False

    hash_method_ntlmv1_ntlmv2: bool = False
    hash_method_lan_manager: bool = False
    hash_method_mschapv2: bool = False
    recover_webdav_digest: bool = False
    recover_apop: bool = False


class OpenDirectoryService(BaseModel):
    running: bool = False
    start_time: Optional[datetime]
