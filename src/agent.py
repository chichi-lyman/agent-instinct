# Copyright © 2026 Chelsea Megan Woods
"""Agent Instinct — sentiment + empowerment content; ALLOW publish."""

from pydantic import BaseModel, Field


class SentimentBrief(BaseModel):
    theme: str
    polarity: str
    policy: str = Field(default="ALLOW")
    can_publish: bool = Field(default=True)


class ContentBrief(BaseModel):
    pillar: str
    topic: str
    avoid: list[str] = Field(
        default_factory=lambda: [
            "rage bait",
            "jealousy clickbait",
            "shame hooks",
            "fake followers",
        ]
    )
    schedulers: list[str] = Field(default_factory=lambda: ["feedhive", "publer"])
    policy: str = Field(default="ALLOW")


class InstinctAgent:
    name = "agent_instinct"
    default_policy = "ALLOW"

    def analyze(self, topic: str) -> SentimentBrief:
        return SentimentBrief(
            theme=topic,
            polarity="supportive",
            policy="ALLOW",
            can_publish=True,
        )

    def content_brief(self, pillar: str, topic: str) -> ContentBrief:
        return ContentBrief(pillar=pillar, topic=topic, policy="ALLOW")
