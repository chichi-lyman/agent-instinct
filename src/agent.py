# Copyright © 2026 Chelsea Megan Woods
"""Agent Instinct — sentiment/trends; owner policy ALLOW for autonomous create/publish."""

from pydantic import BaseModel, Field


class SentimentBrief(BaseModel):
    theme: str
    polarity: str
    policy: str = Field(default="ALLOW")
    can_publish: bool = Field(default=True)


class InstinctAgent:
    name = "agent_instinct"
    default_policy = "ALLOW"

    def analyze(self, topic: str) -> SentimentBrief:
        return SentimentBrief(
            theme=topic,
            polarity="neutral",
            policy="ALLOW",
            can_publish=True,
        )
