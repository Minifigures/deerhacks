# TODO — Nodes 2, 3, 5: Scout, Vibe Matcher, Cost Analyst

## 🔒 Pre-Flight: Security
- [x] Verify `.env` is not tracked by git
- [x] Confirm all API keys are set (Google Cloud, Yelp, Firecrawl, Snowflake)

---

## Node 2: The SCOUT (Discovery)
- [x] **2.1** Create `services/google_places.py`
- [x] **2.2** Create `services/yelp.py`
- [x] **2.3** Implement `scout_node()` in `scout.py`
- [x] **2.4** Add `pydantic-settings` + `SNOWFLAKE_ROLE` to config

## Node 3: The VIBE MATCHER
- [x] **3.1** Create `services/gemini.py`
- [x] **3.2** Implement `vibe_matcher_node()` in `vibe_matcher.py`

## Node 5: The COST ANALYST
- [x] **5.1** Implement `_firecrawl_map()` in `cost_analyst.py`
- [x] **5.2** Implement `_firecrawl_scrape()` in `cost_analyst.py`
- [x] **5.3** Implement `cost_analyst_node()` full pipeline
- [x] **5.4** Gemini-based pricing extraction (replaces manual parsing)

## Final Checks
- [x] Syntax check all modified files (7/7 passed)
- [x] No secrets in committed code (verified: zero hits)
- [x] `.env` not tracked by git (confirmed)

---

## Review

### Files Created (5 new)
| File | Purpose |
|------|---------|
| `services/google_places.py` | Google Places Text Search wrapper |
| `services/yelp.py` | Yelp Fusion Business Search wrapper |
| `services/gemini.py` | Gemini API wrapper (text + multimodal) |
| `agents/scout.py` | Node 2 — full implementation |
| `agents/vibe_matcher.py` | Node 3 — full implementation |

### Files Modified (3)
| File | Change |
|------|--------|
| `agents/cost_analyst.py` | Node 5 — full implementation |
| `core/config.py` | Added `SNOWFLAKE_ROLE` field |
| `requirements.txt` | Added `pydantic-settings` |

### Security Audit Results
- ✅ No API keys found in any `.py`, `.js`, or `.jsx` file
- ✅ `.env` not tracked by git
- ✅ All secrets loaded via `pydantic-settings` from environment only
