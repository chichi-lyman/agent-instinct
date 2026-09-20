# Copyright © 2026 Chelsea Megan Woods
from pydantic import BaseModel, Field

class SentimentBrief(BaseModel):
    theme: str
    polarity: str
    policy: str = Field(default="REQUIRE_APPROVAL")
    can_publish: bool = Field(default=False)

class InstinctAgent:
    name = "agent_instinct"
    def analyze(self, topic: str) -> SentimentBrief:
        return SentimentBrief(theme=topic, polarity="neutral", policy="REQUIRE_APPROVAL", can_publish=False)
