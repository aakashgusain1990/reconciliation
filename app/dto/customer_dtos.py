from dataclasses import dataclass, asdict
from typing import Optional

@dataclass
class CustomerDto:
    email: Optional[str] = None
    phone_number: Optional[str] = None

    def dict(self):
        return {k: str(v) for k, v in asdict(self).items()}
