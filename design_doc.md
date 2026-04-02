# KeenFox AI-Powered Competitive Intelligence & Campaign Feedback System

---

## 1. System Overview

This system is designed to automate the end-to-end process of gathering, analyzing, and leveraging competitive intelligence to improve marketing effectiveness and go-to-market (GTM) strategies.

It consists of two major components:

### 1. Competitive Intelligence Engine
- Collects competitor signals from multiple sources
- Extracts structured insights using an LLM (Gemini)
- Produces a queryable intelligence dataset

### 2. Campaign Feedback Loop Integrator
- Uses extracted intelligence to generate actionable campaign strategies
- Continuously updates recommendations based on new data
- Enables iterative improvement of GTM decisions

The system bridges the gap between **raw competitor data → actionable strategy**, making it highly valuable for marketing and product teams.

---

## 2. System Architecture & Data Flow

## System Architecture & Data Flow Diagram

![System Architecture](./image-diagram.png)

> Figure 1: End-to-end architecture of the Competitive Intelligence & Campaign Feedback System

---

### Detailed Explanation

The system follows a modular pipeline architecture:

### 1. Data Sources Layer
The system ingests data from multiple sources:
- Competitor websites (pricing, features, messaging)
- Reddit discussions (community sentiment)
- Review platforms like G2/Capterra (user feedback)

This ensures diversity in signals and reduces bias.

---

### 2. Data Ingestion Layer
Each source is processed independently:
- Web Scraper → extracts structured text from websites
- Reddit Fetcher → retrieves community discussions
- Review Loader → loads user feedback data

These are combined into a unified dataset for each competitor.

---

### 3. Data Aggregation Layer
All raw inputs are merged into a single text corpus per competitor:
- Removes duplication
- Combines multiple signal sources
- Prepares data for LLM processing

---

### 4. LLM Signal Extraction Layer (Gemini)

Gemini is used as the reasoning engine to transform unstructured text into structured intelligence.

It extracts:
- Feature launches
- Messaging shifts
- Customer sentiment (loves & complaints)
- Pricing changes
- Product gaps / weaknesses

Output is strictly structured in JSON format.

---

### 5. Structured Intelligence Layer

The extracted insights are stored in a structured format:

```json
{
  "feature_launches": [],
  "messaging_shifts": [],
  "customer_sentiment": {
    "loves": [],
    "complaints": []
  },
  "pricing_changes": [],
  "gaps": []
}