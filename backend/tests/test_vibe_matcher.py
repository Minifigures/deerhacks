"""
Test Node 3 — The VIBE MATCHER (standalone)
Tests vibe scoring with mock candidate data so it doesn't depend on Scout.

Run:  python -m pytest tests/test_vibe_matcher.py -v -s
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import pytest
from app.agents.vibe_matcher import vibe_matcher_node


# ── Mock venue data (no Scout dependency) ──────────────────

MOCK_CANDIDATES = [
    {
        "venue_id": "gp_test001",
        "name": "The Cozy Bean Café",
        "address": "123 Queen St W, Toronto",
        "lat": 43.6510,
        "lng": -79.3935,
        "rating": 4.5,
        "review_count": 200,
        "photos": [],  # No photos — tests the no-image path
        "category": "cafe",
        "source": "google_places",
    },
    {
        "venue_id": "yelp_test002",
        "name": "Neon Arcade Bar",
        "address": "456 King St W, Toronto",
        "lat": 43.6445,
        "lng": -79.3951,
        "rating": 4.2,
        "review_count": 150,
        "photos": [],
        "category": "bar",
        "source": "yelp",
    },
]


class TestVibeMatcher:
    """Test the vibe_matcher_node with mock candidates."""

    def test_vibe_scores_returned_for_all_candidates(self):
        """Every candidate should get a vibe score entry."""
        state = {
            "parsed_intent": {"vibe": "cozy"},
            "candidate_venues": MOCK_CANDIDATES,
            "vibe_scores": {},
        }

        result = vibe_matcher_node(state)

        scores = result.get("vibe_scores", {})
        assert isinstance(scores, dict), "vibe_scores should be a dict"
        assert len(scores) == len(MOCK_CANDIDATES), (
            f"Expected {len(MOCK_CANDIDATES)} scores, got {len(scores)}"
        )

        for venue in MOCK_CANDIDATES:
            vid = venue["venue_id"]
            assert vid in scores, f"Missing score for {vid}"
            entry = scores[vid]
            assert "score" in entry, f"Missing 'score' key for {vid}"
            assert "style" in entry, f"Missing 'style' key for {vid}"
            assert "descriptors" in entry, f"Missing 'descriptors' key for {vid}"
            assert "confidence" in entry, f"Missing 'confidence' key for {vid}"

        print("\n✅ Vibe Matcher scored all candidates:")
        for vid, s in scores.items():
            print(f"   {vid}: score={s['score']}, style={s['style']}, "
                  f"confidence={s['confidence']}")

    def test_vibe_no_preference(self):
        """Without a vibe preference, it should still score using a neutral prompt."""
        state = {
            "parsed_intent": {},  # no vibe key
            "candidate_venues": MOCK_CANDIDATES[:1],  # just one to save API calls
            "vibe_scores": {},
        }

        result = vibe_matcher_node(state)
        scores = result.get("vibe_scores", {})
        assert len(scores) == 1

    def test_vibe_empty_candidates(self):
        """No candidates → empty scores, no crash."""
        state = {
            "parsed_intent": {"vibe": "cyberpunk"},
            "candidate_venues": [],
            "vibe_scores": {},
        }

        result = vibe_matcher_node(state)
        assert result["vibe_scores"] == {}
