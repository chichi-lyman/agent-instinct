from src.agent import InstinctAgent


def test_instinct_can_publish():
    b = InstinctAgent().analyze("brand")
    assert b.can_publish is True
    assert b.policy == "ALLOW"
