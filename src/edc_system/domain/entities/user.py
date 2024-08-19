from dataclasses import dataclass, field

from edc_system.domain.entities.base import BaseEntity


@dataclass
class User(BaseEntity):
    username: str
    email: str
    hashed_password: str
    public_key: str = field(default_factory=str, kw_only=True)
