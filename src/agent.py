# Copyright © 2026 Chelsea Megan Woods
"""Agent Instinct — ALLOW publish; raw/rage/jealousy themes allowed."""

from pydantic import BaseModel, Field


class SentimentBrief(BaseModel):
    theme: str
    polarity: str
    policy: str = Field(default="ALLOW")
    can_publish: bool = Field(default=True)


class ContentBrief(BaseModel):
    pillar: str
    topic: str
    intensity: str = Field(default="raw")  # calm | raw | rage
    allow_rage_jealousy_hooks: bool = Field(default=True)
    transform_to_agency: bool = Field(
        default=True,
        description="Prefer ending on boundary/clarity/power when it fits",
    )
    schedulers: list[str] = Field(default_factory=lambda: ["feedhive", "publer"])
    policy: str = Field(default="ALLOW")


class InstinctAgent:
    name = "agent_instinct"
    default_policy = "ALLOW"

    def analyze(self, topic: str) -> SentimentBrief:
        return SentimentBrief(
            theme=topic,
            polarity="raw_or_supportive",
            policy="ALLOW",
            can_publish=True,
        )

    def content_brief(
        self, pillar: str, topic: str, intensity: str = "raw"
    ) -> ContentBrief:
        return ContentBrief(
            pillar=pillar,
            topic=topic,
            intensity=intensity,
            allow_rage_jealousy_hooks=True,
            policy="ALLOW",
        )
