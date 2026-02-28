# System Architecture Documentation

## Project: PATHFINDER

**Goal:** Intelligent, vibe-aware group activity and venue planning with predictive risk analysis and spatial visualization.

---

## 🏗️ Architecture Overview

PATHFINDER is an agentic, graph-orchestrated decision system designed to recommend where groups should go—not just based on availability, but on vibe, accessibility, cost realism, and failure risk.

The system is built around a multi-agent LangGraph workflow, coordinated by a central Orchestrator (the Commander), with Snowflake acting as long-term memory and predictive intelligence.

### Core Design Philosophy

> Move from "What places exist?" → "What will actually work for this group, at this time?"

---

## 🧭 PATHFINDER: Integrated Agentic Workflow

### Node 1: The COMMANDER (Orchestrator Node)

**Role:** Central brain and LangGraph Supervisor.
**Model:** Gemini 1.5 Flash
**Never calls external APIs directly.**

**Responsibilities:**

- **Intent Parsing:** Converts prompts like
  `"Basketball for 10 people, budget-friendly, west end"`
  into a structured execution state.

- **Complexity Tiering:** Determines whether the request needs:
  - Quick lookup
  - Full multi-agent evaluation
  - Adversarial re-checks

- **Dynamic Weighting:**
  Adjusts agent influence in real time:
  - "Cheap" → Cost Analyst ↑
  - "Aesthetic / vibe" → Vibe Matcher ↑
  - "Outdoor" → Critic ↑

- **Snowflake Pre-Check:**
  Queries Snowflake Cortex for historical risk patterns (e.g., weather failures, noise complaints) and preemptively boosts the Critic's priority if needed.

**Output:**
A fully weighted execution plan passed into LangGraph.

---

### Node 2: The SCOUT (Discovery Node)

**Role:** The system's "eyes."
**Tools:** Google Places API, Yelp Fusion

**Responsibilities:**

- Discovers 5–10 candidate venues based on the Commander's intent.

- Collects:
  - Coordinates
  - Ratings & reviews
  - Photos
  - Category metadata

- **Snowflake Enrichment:**
  Immediately enriches candidates with internal intelligence:
  - Past noise complaints
  - Seasonal closures
  - Known operational issues not visible on Maps/Yelp

**Output:**
A shortlist of enriched candidate venues.

---

### Node 3: The VIBE MATCHER (Qualitative Node)

**Role:** Aesthetic and subjective reasoning engine.
**Model:** Gemini 1.5 Pro (Multimodal)

**Responsibilities:**

- Analyzes:
  - Venue photos
  - Review sentiment
  - Visual composition

- Matches venues against subjective styles such as:
  - Minimalist
  - Cyberpunk
  - Cozy
  - Dark Academia

- Computes a **Vibe Score** based on:
  - Color palettes
  - Lighting
  - Symmetry
  - Architectural mood

**Output:**
A normalized Vibe Score per venue + qualitative descriptors.

---

### Node 4: The ACCESS ANALYST (Logistics Node)

**Role:** Spatial reality check.
**Tools:**
- Mapbox Isochrone API
- Google Distance Matrix

**Responsibilities:**

- Computes travel-time feasibility for the entire group.

- Penalizes venues that are:
  - Close geographically
  - Far chronologically (traffic, transit gaps)

- Generates GeoJSON isochrones representing reachable areas.

- **Frontend Integration:**
  GeoJSON blobs are passed directly to the Mapbox SDK.
  Rendered as interactive travel-time overlays on the user's map.

**Output:**
Accessibility scores + map-ready spatial data.

---

### Node 5: The COST ANALYST (Financial Node)

**Role:** "No-surprises" auditor.
**Tools:** Firecrawl, Jina Reader

**Responsibilities:**

- Scrapes venue websites to compute **Total Cost of Attendance (TCA)**:
  - Hidden fees
  - Equipment rentals
  - Minimum spends

- **Snowflake Cortex Comparison:**
  Compares live prices against historical trends to detect:
  - Seasonal price spikes
  - Misleading "discounts"

**Output:**
Transparent, normalized cost profiles per venue.

---

### Node 6: The CRITIC (Adversarial Node)

**Role:** Actively tries to break the plan.
**Model:** Gemini (Adversarial Reasoning)
**Tools:** OpenWeather API, PredictHQ

**Responsibilities:**

- Cross-references top venues with real-world risks:
  - Weather conditions
  - City events
  - Road closures

- Identifies dealbreakers:
  - Rain-prone parks
  - Marathon routes
  - Event congestion

- **The Veto Mechanism:**
  If a critical issue is found:
  - Triggers a LangGraph retry
  - Forces the Commander to re-rank candidates

**Output:**
Risk flags, veto signals, and explicit warnings.

---

### Node 7: SNOWFLAKE (Memory & Intelligence Layer)

**Role:** Long-term memory and predictive intelligence.

**Functions:**

- **Risk Storage:** Logs historical failures
  (e.g., "Park floods after 5mm rain")

- **RAG Engine:** Snowflake Cortex Search powers:
  - Scout enrichment
  - Critic forecasting

- **Trend Analysis:** Seasonal pricing surges, congestion patterns

**Value Proposition:**
Transforms PATHFINDER from reactive to predictive.

---

## 🎨 Final Synthesis & Output

The Commander collects all node outputs, applies final dynamic weights, and emits a clean JSON response to the frontend.

### The User Receives:

1. **Ranked Top 3 Venues**
   - Displayed as interactive pins on a Mapbox canvas

2. **"Why" & "Watch Out" Cards**
   - Human-readable reasoning
   - Explicit warnings surfaced from the Critic

3. **Spatial Visualization**
   - Travel-time isochrones
   - Feasibility overlays for the entire group

---

## ⚙️ Frontend Integration

### Tech Stack:
- React + Next.js
- Tailwind CSS
- Mapbox SDK

### Map Experience:
- Interactive Mapbox canvas (Google Maps–like UX)
- Pins for ranked venues
- Isochrone overlays for reachability
- Hover & click interactions tied to agent explanations

---

## 🚀 Optional Enhancements

- **Redis:**
  Cache Google/Yelp results for popular queries to reduce cost and latency.

- **FAISS:**
  Local similarity scoring for fast pre-ranking before Snowflake persistence.

- **Auth0 Favorites:**
  Save "High Vibe" locations and feed them back into Commander weight personalization.

---

## 🛠️ Troubleshooting

### 1. "No Results / Empty Map"

**Symptoms:**
- No venue pins appear on the Mapbox canvas.
- Scout returns an empty candidate list.

**Checks:**
- Verify `GOOGLE_PLACES_API_KEY` and `YELP_API_KEY` are set in backend environment variables.
- Confirm the Commander did not over-constrain filters (e.g., strict budget + niche vibe).
- Inspect LangGraph logs to ensure the Scout node executed (not short-circuited by intent classification).

---

### 2. "Map Loads but No Isochrone Overlays"

**Symptoms:**
- Mapbox renders, but no travel-time blobs appear.

**Checks:**
- Ensure `MAPBOX_ACCESS_TOKEN` is valid and scoped for Isochrone API usage.
- Confirm the Access Analyst returned valid GeoJSON.
- Verify the frontend Mapbox layer is added after the map `onLoad` event.
- Check that coordinates are in `[longitude, latitude]` order (Mapbox requirement).

---

### 3. "Results Look Good but Fail in Reality"

**Symptoms:**
- A recommended venue is closed, flooded, or inaccessible.

**Checks:**
- Confirm Snowflake Cortex is reachable and returning RAG context.
- Inspect Critic node execution — ensure veto conditions are not disabled.
- Check PredictHQ quota and response validity for event congestion data.

---

### 4. "High Latency or Timeouts"

**Symptoms:**
- Requests exceed acceptable response times.

**Checks:**
- Ensure Scout and Cost Analyst API calls are parallelized.
- Enable Redis caching for Google Places and Yelp queries.
- Reduce candidate pool size (default: 5–10).
- Confirm LangGraph retry limits are not too permissive.

---

### 5. "Pricing Seems Wrong or Incomplete"

**Symptoms:**
- Users report unexpected fees.

**Checks:**
- Verify Firecrawl/Jina Reader selectors are still valid.
- Confirm Cost Analyst is computing Total Cost of Attendance, not just entry price.
- Check Snowflake historical pricing baseline is populated.

---

## 🧠 Model Summary

| Node | Model / Tooling | Purpose |
|------|----------------|---------|
| Commander | Gemini 1.5 Flash | Intent parsing, complexity tiering, dynamic agent weighting |
| Scout | Google Places API, Yelp Fusion | Venue discovery and raw metadata collection |
| Vibe Matcher | Gemini 1.5 Pro (Multimodal) | Aesthetic, photo-based, and sentiment-driven vibe analysis |
| Access Analyst | Mapbox Isochrone API, Google Distance Matrix | Travel-time feasibility and spatial scoring |
| Cost Analyst | Firecrawl, Jina Reader + Snowflake Cortex | True cost extraction and pricing anomaly detection |
| Critic | Gemini (Adversarial Reasoning) + OpenWeather, PredictHQ | Failure detection, risk forecasting, veto logic |
| Memory & RAG | Snowflake + Snowflake Cortex Search | Historical risk storage and predictive intelligence |
| Orchestration | LangGraph | Execution order, shared state, conditional retries |
| Frontend Mapping | Mapbox SDK | Interactive maps, pins, isochrone overlays |

---

## Design Rationale

- **Gemini 1.5 Flash** is used where speed and classification matter.
- **Gemini 1.5 Pro** is reserved for high-value multimodal reasoning (vibe).
- **Snowflake Cortex** ensures the system improves over time instead of repeating failures.
- **LangGraph** enables controlled retries without infinite loops or silent failures.
