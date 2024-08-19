from edc_system.domain.entities.base import BaseEntity


class FileMetadata(BaseEntity):
    author: str
    hash_sum: str
    signed_hash_sum: str
