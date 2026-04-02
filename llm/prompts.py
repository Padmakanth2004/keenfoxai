def competitor_prompt(data):
    return f"""
You are a competitive intelligence system.

Extract ONLY the following fields:

1. Feature launches and product updates
2. Messaging shifts
3. Customer sentiment:
   - what users love
   - what users complain about
4. Pricing changes or packaging
5. Gaps or weaknesses

Return STRICT JSON format:

{{
  "feature_launches": [],
  "messaging_shifts": [],
  "customer_sentiment": {{
    "loves": [],
    "complaints": []
  }},
  "pricing_changes": [],
  "gaps": []
}}

DATA:
{data}
"""
def campaign_prompt(intel):
    return f"""
You are a senior GTM strategist for KeenFox.

Using the competitive intelligence data below, generate actionable campaign recommendations.

---

### 1. Messaging & Positioning
- Identify where KeenFox is weak compared to competitors
- Highlight underexploited angles
- Generate improved copy for ONE channel (choose one):
  - Homepage headline OR
  - Cold email OR
  - LinkedIn ad

---

### 2. Channel & Targeting Strategy
- Identify where competitors are most active
- Recommend:
  - Channels KeenFox should DOUBLE DOWN on
  - Channels KeenFox should REDUCE focus on

---

### 3. Full GTM Strategy Refinements
- Provide 3 to 5 prioritized strategies
- Each MUST include:
  - Strategy
  - Clear reasoning based on competitor insights

---

### OUTPUT FORMAT (STRICT):

## Messaging & Positioning
...

## Channel & Targeting Strategy
...

## GTM Strategy
1. Strategy:
   Reason:
2. Strategy:
   Reason:

---

DATA:
{intel}
"""