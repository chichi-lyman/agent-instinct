from src.agent import InstinctAgent
def test_instinct_cannot_publish():
    b = InstinctAgent().analyze("brand")
    assert b.can_publish is False
    assert b.policy == "REQUIRE_APPROVAL"
