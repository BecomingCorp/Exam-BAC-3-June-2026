#!/usr/bin/env python3
"""Generate EBE study materials: 4 CLAUDE.md files + 4 PDFs."""

import os
import re
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak, KeepTogether
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY

BASE = "/home/user/real-estate-dashboard/Session June 2026/European Business and Economics"

def md_bold(text):
    """Convert **word** markdown bold to <b>word</b> HTML bold for reportlab."""
    return re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)

# ─────────────────────────────────────────────────────────────
# CONTENT DEFINITIONS
# ─────────────────────────────────────────────────────────────

CHAPTERS = [
    {
        "num": 1,
        "title": "Chapter 1 — Context: EU Institutions & Law",
        "subtitle": "What is the EU, how is it built, and how does it make decisions?",
        "pdf_name": "Chapter_1_Context.pdf",
        "claude_path": "Introduction and History/CLAUDE.md",
        "synthesis": """
## KEY CONCEPT 1 — The EU Idea & History

The EU was born from the ashes of WWII with one goal: make war between European nations **materially impossible** by linking their economies. Robert Schuman's 1950 declaration led to the ECSC (coal & steel), the first brick of European integration.

**7 milestones you must know:**

| Date | Event | What it changed |
|------|-------|----------------|
| 1951 | ECSC (Schuman Treaty) | France + Germany pool coal & steel |
| 1957 | Treaties of Rome | EEC + Euratom → common market created |
| 1968 | Customs Union completed | No more customs duties between members |
| 1985/86 | Schengen + Single Market Act | Free movement of people + 4 freedoms |
| 1992 | Maastricht Treaty | Official EU created + euro planned |
| 2007 | Lisbon Treaty | 295 amendments, streamlined institutions |
| 1999/2002 | Euro (rates fixed / coins) | Single monetary policy under ECB |

**The 3 circles — never confuse them:**
- **EU** = 27 Member States
- **Schengen** = 29 states (free movement, includes non-EU: Norway, Switzerland...)
- **Eurozone** = 20 states (single currency, the euro)

---

## KEY CONCEPT 2 — The Institutional Triangle

The EU is governed by a triangle of 3 main institutions that share legislative power:

| Institution | Role | Head | Location |
|-------------|------|------|----------|
| **European Commission** | Executive + proposes laws + guardian of treaties | Ursula von der Leyen (27 commissioners) | Brussels (Berlaymont) |
| **European Parliament** | Co-legislator, represents **citizens** | Roberta Metsola (705 MEPs) | Strasbourg + Brussels |
| **Council of the EU** | Co-legislator, represents **governments** | Rotating presidency (6 months) | Brussels (Justus Lipsius) |

**Concrete example:** The Commission proposes a law on CO2 emissions. The Parliament (elected citizens) and the Council (environment ministers of 27 states) both vote on it. If they disagree, they negotiate — this is the OLP.

**3 more institutions to know:**
- **European Council** = heads of state (Macron, Scholz, etc.) — sets political direction, NOT a legislator
- **ECB** = manages the euro, sets interest rates (Christine Lagarde)
- **CJEU** = ensures EU law is respected (Luxembourg)
- **Council of Europe** ≠ EU — completely separate, 46 countries, human rights only

---

## KEY CONCEPT 3 — EU Law: Primary vs Secondary

**Primary Law** = the EU's constitution. It's the founding treaties:
- **TEU** (Treaty on European Union): objectives, institutional structure
- **TFEU** (Treaty on Functioning of EU): detailed competences and policies

**Secondary Law** = laws made *under* the treaties. 5 types:

| Type | Binding? | Direct? | Example |
|------|----------|---------|---------|
| **Regulation** | Yes | Yes (applies immediately) | GDPR data protection |
| **Directive** | Yes | No (states must transpose) | USB-C standardization directive |
| **Decision** | Yes | Yes (specific targets) | Fine on Microsoft |
| **Recommendation** | No | No | Advice on pension reform |
| **Opinion** | No | No | View on trade policy |

**3 principles governing EU competences:**
1. **Conferral**: EU only has powers granted by treaties — nothing more
2. **Subsidiarity**: EU acts only if states can't do it effectively alone
3. **Proportionality**: EU action must not exceed what's needed

---

## KEY CONCEPT 4 — The OLP (Ordinary Legislative Procedure)

How a law gets made: Commission proposes → Parliament + Council co-decide (max 3 readings). If no agreement after 3 readings → Conciliation Committee → if still no deal → law dies.

**Qualified majority in Council** = 55% of states + 65% of EU population.

---

## KEY CONCEPT 5 — The Single Market & Balassa's Integration Levels

The Single Market = the EU's greatest achievement. 450 million consumers, free movement of:
1. **Goods** (no customs duties internally)
2. **Services** (a Belgian lawyer can work in Spain)
3. **Capital** (invest freely across borders)
4. **People** (live, work, study anywhere in the EU)

**Balassa's 6 levels of integration (learn in order):**
1. Free Trade Area → removes customs duties between members
2. Customs Union → + common external tariff with non-members
3. Common Market → + free movement of production factors
4. Economic Union → + harmonized economic policies
5. **EMU** → + single currency + common monetary policy ← WHERE THE EU IS
6. Political Union → + full sovereignty transfer (not achieved yet)

---

## KEY CONCEPT 6 — EU Trade Policy

The EU is the world's largest single market and speaks with **one voice** in trade negotiations.
- **TTIP** (USA) — under negotiation, aims to reduce tariff + regulatory barriers
- **CETA** (Canada, 2017) — removes 99% of trade barriers, "new generation" treaty
- **MERCOSUR** (Latin America) — Argentina, Brazil, Paraguay, Uruguay
- **CCT (Common Customs Tariff)** — same tariff applied to ALL imports from outside EU
- Trade policy = **exclusive EU competence** (not national governments)
""",
        "qa": [
            ("What was the founding idea behind the EU?", "To make war between European nations materially impossible by linking their economies. The Schuman Declaration (1950) proposed pooling French and German coal and steel production, leading to the ECSC in 1951."),
            ("What are the 3 circles of European membership? How many states in each?", "EU = 27 states. Schengen = 29 states (free movement of people, includes non-EU countries). Eurozone = 20 states (single currency, the euro)."),
            ("What are the 3 institutions of the Institutional Triangle and their roles?", "Commission (executive, proposes laws, guardian of treaties — von der Leyen, 27 commissioners). Parliament (co-legislator, represents citizens — Metsola, 705 MEPs). Council of the EU (co-legislator, represents governments — rotating 6-month presidency)."),
            ("European Council ≠ Council of the EU ≠ Council of Europe — explain each.", "European Council = heads of state (Macron, Scholz…), sets political direction, NOT a legislator. Council of the EU = ministers of 27 states, co-legislates. Council of Europe = completely separate from EU, 46 countries, defends human rights."),
            ("What is Primary Law? Give examples.", "Primary Law is the supreme source of EU law — the founding treaties. TEU (Treaty on European Union): objectives and institutional structure. TFEU (Treaty on Functioning of EU): detailed competences and policies. Both were created at Maastricht and updated at Lisbon."),
            ("Regulation vs Directive — what's the key difference?", "A Regulation is directly applicable in all member states the moment it enters into force (e.g. GDPR). A Directive sets an objective but member states must transpose it into national law within a deadline (e.g. USB-C directive)."),
            ("What are the 3 principles governing EU competences?", "1. Conferral: EU only has powers explicitly granted by treaties. 2. Subsidiarity: EU acts only if states cannot act effectively alone. 3. Proportionality: EU action must not exceed what is needed to achieve the objective."),
            ("What is the OLP (Ordinary Legislative Procedure)?", "The default lawmaking process: Commission proposes → Parliament + Council co-decide on equal footing, max 3 readings. If no agreement, a Conciliation Committee is convened. If it still fails, the law is not adopted."),
            ("What is the qualified majority in the Council of the EU?", "55% of Member States + 65% of the EU population. This double threshold means large AND small countries must both be represented."),
            ("What are the 4 freedoms of the Single Market?", "Free movement of: 1. Goods (no internal customs). 2. Services (provide services in any member state). 3. Capital (invest freely). 4. People (live, work, study anywhere in the EU)."),
            ("List Balassa's 6 levels of regional integration in order.", "1. Free Trade Area. 2. Customs Union (+ common external tariff). 3. Common Market (+ free movement of factors). 4. Economic Union (+ harmonized policies). 5. EMU (+ single currency + monetary policy). 6. Political Union (+ full sovereignty transfer). The EU is at level 5."),
            ("What is the CETA and why is it called a 'new generation' treaty?", "CETA is the free trade agreement between the EU and Canada (signed 2016, partially in force 2017). It removes 99% of import barriers. It's 'new generation' because it goes beyond customs duties to cover services, investments, intellectual property and public procurement."),
            ("What is the Common Customs Tariff (CCT)?", "A uniform tariff applied by all EU member states to goods imported from outside the EU. Rates vary depending on the product type and its economic sensitivity. Managing external trade is an exclusive EU competence."),
            ("What Treaty created the EU as we know it today?", "The Maastricht Treaty (1992), which officially created the European Union from the existing European Community, introduced the three-pillar structure, and laid the groundwork for the euro and EMU."),
            ("What did the Lisbon Treaty change?", "Signed in 2007, it introduced 295 amendments to existing treaties. It created the permanent President of the European Council, gave the Parliament equal power with the Council in most areas, and made the Charter of Fundamental Rights legally binding. It did NOT transfer new exclusive powers to the EU."),
        ]
    },
    {
        "num": 2,
        "title": "Chapter 2 — Functioning: EU Economic Governance",
        "subtitle": "How does the EU manage 27 economies with one currency?",
        "pdf_name": "Chapter_2_Governance.pdf",
        "claude_path": "Economical & Monetary Union (EMU)/CLAUDE.md",
        "synthesis": """
## KEY CONCEPT 1 — Mundell's Policy Trilemma (THE most important concept)

A national economy **cannot simultaneously achieve** all three of these objectives:
1. **Fixed exchange rate** (stable currency for trade)
2. **Independent monetary policy** (set your own interest rates)
3. **Free movement of capital** (investors move money freely)

You can only ever have **2 out of 3**.

**What the Eurozone chose:** Fixed rates (1) + Free capital (3) → surrendered monetary autonomy. Result: interest rates are set by the ECB for all 20 eurozone members, regardless of individual national needs.

**Concrete example:** When Greece was in crisis (2010), it couldn't devalue its currency or cut interest rates independently — the ECB decides for everyone. That's the structural tension of the Eurozone.

---

## KEY CONCEPT 2 — The 3 Phases of the Eurozone (Delors Report)

| Phase | Date | What happened |
|-------|------|---------------|
| **Phase 1** | July 1990 | Legal preparations, abolition of capital movement restrictions |
| **Phase 2** | Jan 1994 | IME (European Monetary Institute) created, ECB preparation, Maastricht criteria applied |
| **Phase 3** | Jan 1999 | Exchange rates irrevocably fixed, ECB takes over monetary policy. Coins/notes: 2002 |

**Maastricht Convergence Criteria** (to join the euro, a country must meet):
- Inflation: no more than 1.5% above the 3 best-performing EU states
- Government deficit: below **3% of GDP**
- Government debt: below **60% of GDP**
- Exchange rate: stable for 2 years in ERM
- Long-term interest rates: no more than 2% above the 3 best performers

---

## KEY CONCEPT 3 — Macroeconomic Policy: Two Levels

**At national level:**
- Short-term: **fiscal policy** (taxes + spending) + monetary policy (only for non-euro countries)
- Long-term: structural policies (agriculture, labour market reforms, education)

**At EU/supranational level:**
- Short-term: **monetary policy** (ECB manages the euro)
- Coordination: **European Semester** + Stability and Growth Pact

**The key tension:** Monetary policy is EU-level (ECB). Fiscal policy remains national. This creates coordination challenges — if Germany saves and Greece spends, the ECB must find a middle ground.

---

## KEY CONCEPT 4 — The ECB and Monetary Policy

The ECB's **single mandate**: maintain price stability = keep inflation at **2% over the medium term**.
(Unlike the US Federal Reserve / FED which also targets full employment)

**3 interest rates the ECB controls:**
| Rate | Who it affects | Purpose |
|------|----------------|---------|
| Main refinancing rate | Banks borrowing from ECB | Controls cost of money in the economy |
| Marginal lending facility | Overnight bank loans | Emergency liquidity for banks |
| Deposit facility | Banks parking money at ECB | Discourages hoarding, encourages lending |

**Concrete example:** When inflation hit 10% post-COVID, the ECB raised all 3 rates aggressively (to 4.5%/4.75%/4%) to cool down spending and bring inflation back to 2%.

---

## KEY CONCEPT 5 — Fiscal Discipline: SGP + European Semester

**Stability and Growth Pact (SGP):**
- Deficit < **3% of GDP**
- Debt < **60% of GDP**
- Sanctions theoretically exist but have **never been applied** (political reality)

**European Semester** (created 2011 post-2008 crisis):
Annual 6-month cycle:
1. Commission publishes economic overview
2. Member states submit budget plans
3. Commission issues country-specific recommendations
4. States implement (or not)

Topics covered: public finances, pensions, taxation, education, unemployment.

---

## KEY CONCEPT 6 — Macro-Prudential Policy

Macro-prudential policy = preventing the **entire financial system** from collapsing (not just individual banks).
- Managed by the ECB through the **SSM** (Single Supervisory Mechanism)
- Monitors systemic risks: excessive credit growth, leverage, contagion effects
- Example: After 2008, the ECB gained supervisory powers over major European banks to prevent another systemic crisis

**Micro vs Macro prudential:**
- Micro = supervising individual banks
- Macro = watching the whole system for domino effects

---

## KEY CONCEPT 7 — Key Macroeconomic Indicators

| Indicator | What it measures | Why it matters for the EU |
|-----------|-----------------|--------------------------|
| **GDP** | Total economic output | Measures economic size and growth |
| **Inflation** | Price level increase | ECB targets 2% — too high = crisis, too low = stagnation |
| **Unemployment** | % of workforce without jobs | Structural vs cyclical; EU Semester tracks this |
| **Public deficit** | Government spending - revenues | SGP: must stay below 3% GDP |
| **Public debt** | Total accumulated government debt | SGP: must stay below 60% GDP |
| **Balance of payments** | All financial flows with rest of world | Always balanced (double-entry accounting) |

---

## KEY CONCEPT 8 — Exchange Rates: Depreciation vs Devaluation

- **Depreciation**: spontaneous fall in currency value driven by the **market** (e.g. investor panic)
- **Devaluation**: deliberate decision by **authorities** to lower currency value (to boost exports)

In the Eurozone, individual countries **cannot devalue** — the ECB manages the euro's value for all 20 members. This was Greece's problem in 2010.

---

## KEY CONCEPT 9 — The Theory of Comparative Advantage

Countries should specialize in what they produce **relatively best**, even if another country is better at everything in absolute terms. This maximizes total output for all trading partners.

**Example:** Germany is better than Portugal at both cars and wine. But Germany is *relatively* much better at cars, and Portugal is *relatively* better at wine. So Germany makes cars, Portugal makes wine — both gain from trade.

This is the fundamental economic argument for free trade and the EU Single Market.
""",
        "qa": [
            ("What is Mundell's Policy Trilemma?", "A country cannot simultaneously have: (1) fixed exchange rate, (2) independent monetary policy, (3) free movement of capital. You must sacrifice one. The Eurozone chose 1 + 3, giving up national monetary autonomy to the ECB."),
            ("What did the Eurozone sacrifice by adopting the euro?", "Member states surrendered their independent monetary policy. Interest rates are now set by the ECB for all 20 eurozone members, regardless of each country's individual economic situation."),
            ("What are the Maastricht convergence criteria to join the euro?", "Inflation ≤ 1.5% above the 3 best EU performers. Deficit < 3% of GDP. Debt < 60% of GDP. Exchange rate stable in ERM for 2 years. Long-term interest rates ≤ 2% above the 3 best performers."),
            ("What are the 3 phases of the Eurozone creation?", "Phase 1 (1990): legal preparations, free capital movement. Phase 2 (1994): IME created, Maastricht criteria applied. Phase 3 (1999): exchange rates irrevocably fixed, ECB takes over. Coins and notes launched in 2002."),
            ("What is the ECB's mandate? How does it differ from the FED?", "The ECB has a single mandate: price stability = inflation at 2% over the medium term. The US Federal Reserve (FED) has a dual mandate: price stability AND full employment. The ECB focuses solely on inflation."),
            ("What are the 3 interest rates the ECB controls?", "1. Main refinancing rate (cost for banks to borrow from ECB — affects all lending). 2. Marginal lending facility (overnight emergency loans for banks). 3. Deposit facility (rate on banks parking money at ECB — discourages hoarding)."),
            ("What is the Stability and Growth Pact (SGP)?", "An EU framework ensuring fiscal discipline. Rules: government deficit must stay below 3% of GDP, government debt below 60% of GDP. Sanctions exist but have never been applied in practice."),
            ("What is the European Semester and why was it created?", "An annual 6-month cycle to coordinate economic, fiscal, social and labour policies across EU member states. Created in 2011 after the 2008 crisis revealed that one country's fiscal problems (Greece) could destabilize all others."),
            ("Depreciation vs Devaluation — what's the difference?", "Depreciation = spontaneous market-driven fall in currency value (e.g. investors sell euros). Devaluation = deliberate government/central bank decision to lower the currency's value (to make exports cheaper). Eurozone members cannot devalue individually."),
            ("What is macro-prudential policy? Who manages it?", "Policy aimed at preserving the stability of the ENTIRE financial system (not just individual banks). Managed by the ECB through the Single Supervisory Mechanism (SSM). It monitors systemic risks like excessive credit growth and contagion effects between banks."),
            ("What is the theory of comparative advantage? Give an example.", "Countries should specialize in what they produce relatively most efficiently. Example: Germany is better at both cars and wine than Portugal, but relatively much better at cars. Germany makes cars, Portugal makes wine — trade makes both better off."),
            ("What is the balance of payments?", "A statistical document recording ALL financial flows between a country's residents and the rest of the world (goods, services, capital, transfers). By accounting definition it always balances. When people say it's 'in deficit' they usually mean the current account (trade) is negative."),
            ("What tension exists at the heart of EMU governance?", "Monetary policy is centralized at the ECB (supranational), but fiscal policy remains national. This means the ECB sets one interest rate for 20 countries with very different economic needs — what's good for Germany may hurt Italy or Greece."),
            ("What are the main macroeconomic indicators tracked in the EU?", "GDP (economic output), Inflation (ECB target: 2%), Unemployment rate, Public deficit (SGP: <3% GDP), Public debt (SGP: <60% GDP), Balance of payments, Exchange rates."),
            ("What is the MIP (Macroeconomic Imbalance Procedure)?", "A monitoring mechanism that detects and corrects macroeconomic imbalances within the EU — e.g. countries running large current account surpluses or deficits, housing bubbles, or rapidly growing private debt. It's part of the European Semester framework."),
        ]
    },
    {
        "num": 3,
        "title": "Chapter 3 — EU Policies: Agriculture, Competition & Industry",
        "subtitle": "What does the EU actually do? Its concrete policies explained.",
        "pdf_name": "Chapter_3_Policies.pdf",
        "claude_path": "EU  From competition to industrial policy/CLAUDE.md",
        "synthesis": """
## KEY CONCEPT 1 — The Common Agricultural Policy (CAP)

The CAP is the EU's agricultural policy — and its **biggest budget item** (~1/3 of the entire EU budget).

**Purpose:** Ensure food security, fair income for farmers, reasonable prices for consumers.

**2 pillars:**
1. **Direct payments** to farmers (based on land area or number of livestock)
2. **Rural development** (modernization, environmental projects)

**Managed by:** DG AGRI (Directorate-General for Agriculture)

**Current controversies:** In 2024, Belgian and European farmers blocked roads across Europe to protest against EU environmental regulations they see as killing profitability. The tension: Green Deal vs farmer viability.

**New CAP 2028:** Stronger emphasis on environmental conditions for receiving subsidies.

---

## KEY CONCEPT 2 — EU Competition Policy

Competition policy = preventing any company from dominating and abusing the market, ensuring a level playing field for all European businesses.

**Managed by:** DG COMP (Directorate-General for Competition)
**Key figure:** Margrethe Vestager (Danish, EU Competition Commissioner)

**Two core legal rules (TFEU):**
- **Article 101**: Prohibits **anti-competitive agreements** between companies (cartels, price-fixing, market sharing)
  - Example: Truck manufacturers secretly agreed on prices → €3.8 billion fine (2016)
- **Article 102**: Prohibits **abuse of dominant position**
  - Example: Google fined €4.3 billion for forcing Android makers to pre-install its apps
  - Example: Apple fined for App Store monopoly (only app store allowed)
  - Example: Microsoft fined for bundling Internet Explorer with Windows

**4 areas of DG COMP:**
1. Antitrust (cartels + dominant position)
2. Mergers & Acquisitions (blocking anti-competitive mergers)
3. Liberalization (opening monopoly sectors to competition)
4. State Aid (preventing governments from unfairly subsidying their own companies)

**Liberalization examples:**
- Telecom: national monopolies broken up in the 1990s → mobile competition
- Aviation: liberalization → Ryanair (low-cost) became possible

---

## KEY CONCEPT 3 — Industrial Policy

**Purpose:** Strengthen European industry's competitiveness, especially vs USA and China.
**Managed by:** DG GROW (Internal Market, Industry, Entrepreneurship, SMEs)

**Lisbon Strategy (2000–2010):**
Goal: Make the EU "the most competitive and dynamic knowledge-based economy in the world by 2010."
Result: Partially achieved — lagged behind on digital/tech vs USA.

**New Industrial Strategy (2020):**
- Finance "alliances" in strategic sectors: clean hydrogen, batteries, semiconductors, satellites
- More flexibility for state aid in these sectors
- Protect European intellectual property globally

**EU vs USA vs China — the competitiveness gap:**
| Sector | EU strength | EU weakness |
|--------|-------------|-------------|
| Automotive | Volkswagen, BMW, Stellantis | Losing to Chinese EVs |
| Aerospace | Airbus | — |
| Chemicals/Pharma | BASF, Bayer | — |
| Digital/Tech | — | No EU equivalent of Google, Apple, Meta |

---

## KEY CONCEPT 4 — The Green Deal

The EU's most ambitious long-term policy. Goal: make Europe the **first climate-neutral continent by 2050**.

**Key targets:**
- **-55% greenhouse gas emissions by 2030** (vs 1990 levels)
- **Net zero emissions by 2050**
- Financed by **NextGenerationEU** (€1,800 billion recovery plan, 1/3 dedicated to green transition)

**Circular Economy:**
- Goal: decouple economic growth from resource consumption
- Double the rate of circular material use before 2035
- Reduce plastic waste, promote repair/reuse over disposal

**Practical examples of Green Deal:**
- EU ban on new petrol/diesel cars from 2035
- USB-C universal charger (reduces e-waste)
- ESG reporting mandatory for large listed companies

---

## KEY CONCEPT 5 — ESG (Environmental, Social, Governance)

A framework to evaluate a company's non-financial impact. Increasingly mandatory for listed EU companies.

| Pillar | What it covers | Example metrics |
|--------|---------------|-----------------|
| **Environmental** | Climate impact, resource use | CO2 emissions, waste management, energy use |
| **Social** | People and communities | Gender pay gap, worker safety, training |
| **Governance** | How the company is run | Board diversity, anti-corruption, executive pay transparency |

**Why it matters for business:** Investors, banks and regulators increasingly refuse to fund companies with poor ESG scores. Being green is no longer optional for EU businesses.

---

## KEY CONCEPT 6 — VUCA World

The concept that explains why business strategy is so complex today:
- **V**olatility: rapid, unpredictable changes (COVID, Ukraine war)
- **U**ncertainty: incomplete information, hard to predict outcomes
- **C**omplexity: multiple interdependent actors (supply chains, regulations, geopolitics)
- **A**mbiguity: situations open to multiple interpretations

**Why the EU matters in a VUCA world:** The EU Single Market gives companies a stable regulatory environment, a large home market, and negotiating power — reducing some VUCA effects for European businesses.

---

## KEY CONCEPT 7 — Schengen & Structural Policies

**Schengen Area:**
- 29 states, free movement of people without systematic border controls
- Includes non-EU members (Norway, Switzerland, Iceland, Liechtenstein)
- NOT the same as the EU (27 countries)

**Structural Policies:**
Long-term policies that permanently alter the supply side of the economy:
- Labour market reforms (flexibility, training)
- Financial market reforms (access to capital)
- Innovation policy (R&D investment)
- Social cohesion (reducing inequalities between regions)
""",
        "qa": [
            ("What is the CAP and how much of the EU budget does it represent?", "The Common Agricultural Policy is the EU's agricultural policy, representing approximately 1/3 of the entire EU budget. It has 2 pillars: direct payments to farmers (based on land/livestock) and rural development funding."),
            ("Why were European farmers protesting in Brussels in 2024?", "Farmers protested against EU environmental regulations (Green Deal requirements) they argued were making farming unprofitable — strict limits on pesticides, fertilizers, and land use. They felt the EU was prioritizing climate goals over agricultural viability."),
            ("What does Article 101 TFEU prohibit? Give a concrete example.", "Article 101 prohibits anti-competitive agreements between companies — cartels, price-fixing, market-sharing. Example: European truck manufacturers secretly coordinated prices for 14 years → €3.8 billion fine by the Commission in 2016."),
            ("What does Article 102 TFEU prohibit? Give a concrete example.", "Article 102 prohibits abuse of a dominant market position. Example: Google was fined €4.3 billion in 2018 for forcing Android smartphone makers to pre-install Google Search and Chrome, blocking competitors from the mobile market."),
            ("Who is Margrethe Vestager and what is her role?", "Margrethe Vestager is a Danish politician who served as EU Commissioner for Competition. She became famous for taking on Silicon Valley giants (Google, Apple, Amazon, Facebook), issuing record fines and pushing for fairer competition in the digital market."),
            ("What is the Lisbon Strategy? Was it successful?", "The Lisbon Strategy (2000-2010) aimed to make the EU 'the most competitive and dynamic knowledge-based economy in the world by 2010.' It was only partially achieved — the EU improved in some areas but fell significantly behind the USA on digital technology and innovation."),
            ("What are the key targets of the European Green Deal?", "Reduce greenhouse gas emissions by 55% by 2030 (vs 1990 levels). Achieve climate neutrality (net zero) by 2050. Financed partly by NextGenerationEU (€1,800 billion recovery plan, with 1/3 allocated to the green transition)."),
            ("What is the circular economy? What is the EU's target?", "An economic model that keeps materials in use as long as possible — repairing, reusing, recycling instead of disposing. EU target: double the circular use rate of materials before 2035. Reduces dependency on raw material imports and cuts waste."),
            ("What are the 3 ESG pillars? Give one metric per pillar.", "Environmental (E): CO2 emissions, energy consumption, waste management. Social (S): gender pay gap, worker safety rates, staff training hours. Governance (G): board diversity, anti-corruption policies, transparency of executive compensation."),
            ("What does VUCA stand for and why is it relevant to the EU?", "Volatility, Uncertainty, Complexity, Ambiguity. It describes today's business environment. The EU is relevant because its Single Market and regulatory framework give companies a stable home base of 450M consumers, reducing VUCA effects compared to operating in fragmented national markets."),
            ("What is DG COMP and what are its 4 areas of competence?", "DG COMP is the European Commission's Directorate-General for Competition. Its 4 areas: 1. Antitrust (cartels + abuse of dominance). 2. Mergers & Acquisitions (blocking anti-competitive deals). 3. Liberalization (opening monopoly sectors). 4. State Aid control (preventing unfair subsidies)."),
            ("How did liberalization change European aviation? Give an example.", "Before liberalization (pre-1990s), each country had a national airline monopoly with high prices. After liberalization opened the market to competition, low-cost carriers like Ryanair emerged, drastically cutting prices and making air travel accessible to millions of Europeans."),
            ("What is the Schengen Area? How is it different from the EU?", "Schengen is a zone of 29 countries with no systematic border controls for people. It's different from the EU (27 countries): some EU members are not in Schengen (Ireland), and some non-EU countries are in Schengen (Norway, Switzerland, Iceland, Liechtenstein)."),
            ("What is the New Industrial Strategy 2020 and why was it launched?", "Proposed by the Commission in March 2020, it aims to boost EU competitiveness in strategic sectors (clean hydrogen, batteries, semiconductors, satellites) by funding sectoral 'alliances,' increasing state aid flexibility, and protecting European intellectual property against unfair foreign competition."),
            ("What is State Aid? Why does the EU control it?", "State aid is financial support given by a government to specific companies (subsidies, tax breaks, loans). The EU controls it to prevent member states from giving their own companies an unfair advantage over competitors from other EU countries, which would distort the Single Market."),
        ]
    },
    {
        "num": 4,
        "title": "Chapter 4 — Businesses & Consumers: EMU in Practice",
        "subtitle": "What does European integration concretely mean for companies and people?",
        "pdf_name": "Chapter_4_Businesses.pdf",
        "claude_path": "EU single market/CLAUDE.md",
        "synthesis": """
## KEY CONCEPT 1 — EMU Benefits for Companies

The euro and the Single Market transformed the business environment for European companies. 5 concrete advantages:

| Advantage | What it means | Concrete example |
|-----------|--------------|-----------------|
| **No exchange rate costs** | No conversion fees between eurozone countries | A Belgian company pays a German supplier in euros — no forex needed |
| **Exchange rate stability** | No currency risk within eurozone | No fear that your Italian customer's currency will depreciate before payment |
| **Vast home market** | 450 million consumers, single set of rules | An Estonian startup can sell to France, Spain, Germany without adapting to 3 different regulatory frameworks |
| **Easier financing** | Unified capital markets, lower borrowing costs | A Portuguese SME can borrow from a Dutch bank as easily as a local one |
| **Price transparency** | Consumers can directly compare prices across countries | Amazon comparison shopping across EU countries |

**Concrete example of the scale:** The EU internal market is the **largest in the world**. Exporting within the EU is like selling domestically — no tariffs, same rules. This is why companies like Airbus or LVMH are globally competitive: they have a massive home base.

---

## KEY CONCEPT 2 — EU Value Chains: Strengths and Weaknesses

The EU is a global leader in **modular production networks** — products are assembled across multiple countries.

**Example:** A German BMW is designed in Munich, has a French-made gearbox, an Italian-made leather interior, assembled in Germany, sold across 100 countries.

**EU competitive strengths:**
- **Automotive**: Volkswagen Group, BMW, Stellantis, Mercedes — global leaders BUT challenged by Chinese EVs
- **Aerospace & Defence**: Airbus competes directly with Boeing
- **Chemicals & Pharmaceuticals**: BASF, Bayer, Sanofi, AstraZeneca
- **Luxury goods**: LVMH, Hermès, Richemont — EU dominates globally

**EU competitive weaknesses:**
- **Electronics**: No EU equivalent of Apple, Samsung, Sony
- **Digital/Tech**: No EU equivalent of Google, Amazon, Meta, Netflix
- **Semiconductors**: Heavy dependence on TSMC (Taiwan), Samsung (Korea)

**EU's strategic response:** EU Chips Act (2023) — invest €43 billion to produce 20% of global chips in Europe by 2030.

---

## KEY CONCEPT 3 — The EU and the Global Economy

**EU's global weight:**
- ~500 million people (now closer to 450M post-Brexit)
- Represents ~14-15% of global GDP
- ~30% of global trade in goods and services
- World's largest aid donor

**The geopolitical challenge:** The EU faces three major trading powers:
- **USA**: Services, digital, defence — TTIP negotiations (stalled)
- **China**: Manufacturing, electronics, infrastructure — Belt & Road concerns, Chinese EV subsidies
- **Emerging blocs**: RCEP (Asia-Pacific), AfCFTA (Africa), USMCA (Americas)

**EU's response:** "Strategic autonomy" — reducing dependence on single suppliers for critical goods (energy, chips, medicines, rare earths).

---

## KEY CONCEPT 4 — EMU for Consumers

The euro and EU membership changed everyday life for 450 million Europeans:

**Freedom to:**
- **Live** in any EU member state (just register, no visa)
- **Work** in any EU member state (qualifications mutually recognized)
- **Be protected** by EU consumer law wherever you are in the EU
- **Study** in any EU university (Erasmus programme, ECTS credits transferable)

**Practical EU impacts on daily life:**
- **No roaming charges** in the EU (abolished 2017) — your phone plan works across all 27 countries
- **USB-C standard** (2024) — EU forced Apple and all manufacturers to use universal charger
- **GDPR** — you can ask any company to delete your data
- **Price comparison** across borders enabled by the euro
- **30-day return policy** minimum across all EU online purchases

---

## KEY CONCEPT 5 — The EU Business Model and ESG Integration

Modern EU companies are increasingly judged not just on profit but on their **ESG performance**:

**Why ESG is now mandatory for many EU companies:**
- CSRD (Corporate Sustainability Reporting Directive, 2024): large listed companies MUST report on ESG metrics
- Banks increasingly use ESG scores in lending decisions
- Large institutional investors (pension funds) apply ESG filters

**The VUCA challenge for businesses:**
In today's volatile world, EU companies face:
- Supply chain disruptions (COVID, Suez Canal blockage)
- Geopolitical risks (Ukraine war, US-China tensions)
- Regulatory changes (Green Deal, digital regulation)
- Demographic shifts (ageing EU population)

**The EU's answer:** Resilient value chains + strategic autonomy + green transition = more stable long-term business environment.

---

## KEY CONCEPT 6 — Wintelism and Modular Production Networks

A key concept from Module 6 (Mme Nouveau's course):

**Fordism** (old model): One company controls the entire production chain (Ford makes every car part).

**Wintelism** (new model, named after Windows + Intel): Value comes from controlling the **standard** (the platform), not the physical production.
- Apple doesn't make iPhones — it designs them and controls the iOS ecosystem
- Airbus designs planes but outsources manufacturing globally
- Value = created by **design, brand, and standard**, not by owning factories

**Why this matters for the EU:** EU companies excel at the middle of value chains (manufacturing, components) but often lack the platform/standard dominance that US tech companies have.

---

## KEY CONCEPT 7 — Making the Link Between All 4 Chapters

**The professor's key question: "Connect the 4 chapters."**

The perfect answer structure:
1. **Chapter 1 (What is the EU?)**: We learn the language — institutions, law, the Single Market. Like learning the alphabet of European integration.
2. **Chapter 2 (How does it work?)**: We understand the grammar — how 27 economies coordinate monetary and fiscal policy with the Mundell trilemma at the core.
3. **Chapter 3 (What does it do?)**: We see the sentences — concrete policies: CAP for agriculture, competition law for fairness, Green Deal for the future.
4. **Chapter 4 (So what?)**: We can now speak the language fluently as a businessperson — understanding how the euro, the Single Market, and EU regulation directly impact your company and your life as a consumer.

**The progression:** Context → Governance → Policies → Business Impact. Each chapter adds a layer of depth to the same reality: a political and economic union trying to be stronger together than apart.
""",
        "qa": [
            ("What are the 5 concrete advantages of EMU for European companies?", "1. No exchange rate conversion costs within the eurozone. 2. Exchange rate stability (no currency risk). 3. Access to a vast home market of 450 million consumers under one regulatory framework. 4. Easier access to financing through unified capital markets. 5. Full price transparency allowing direct cross-border price comparison."),
            ("What are the EU's main competitive strengths and weaknesses in global value chains?", "Strengths: Automotive (BMW, VW), Aerospace (Airbus), Chemicals/Pharma (BASF, Bayer), Luxury (LVMH). Weaknesses: No major consumer electronics brand, no EU equivalent of Google/Apple/Amazon, heavy semiconductor dependence on Asian suppliers."),
            ("What is Wintelism? How does it differ from Fordism?", "Fordism: one company controls the entire production chain (Ford makes every part of the car). Wintelism (Windows + Intel): value comes from owning the platform/standard, not the physical production. Apple designs the iPhone and controls iOS but outsources manufacturing to Foxconn in China."),
            ("What are the 4 freedoms EU citizens enjoy as consumers?", "1. Live in any EU member state (just register). 2. Work in any EU member state (qualifications recognized). 3. Be protected by EU consumer law across all 27 countries. 4. Study in any EU university (Erasmus, ECTS credits transferable)."),
            ("Give 3 concrete examples of how the EU affects daily consumer life.", "1. No roaming charges across EU since 2017 (your phone plan works in all 27 countries). 2. USB-C universal charger mandated by the EU for all devices from 2024. 3. GDPR: you can request any company to delete your personal data, even US companies operating in Europe."),
            ("What is the EU's strategic response to its weakness in semiconductors?", "The EU Chips Act (2023) allocates €43 billion to boost domestic semiconductor production, with the goal of producing 20% of global chips in Europe by 2030, reducing dangerous dependence on Taiwan (TSMC) and South Korea (Samsung)."),
            ("What is the CSRD and why does it matter?", "The Corporate Sustainability Reporting Directive (2024) makes it mandatory for large listed EU companies to report on their ESG (Environmental, Social, Governance) performance in detail. It forces companies to measure and disclose their climate impact, labor practices, and governance quality."),
            ("How would you connect all 4 chapters of the EBE course in one answer?", "Ch1 = the alphabet (what is the EU, its institutions and rules). Ch2 = the grammar (how monetary and fiscal policy coordination works, Mundell trilemma). Ch3 = the sentences (concrete policies: CAP, competition, Green Deal). Ch4 = speaking the language as a businessperson (how it all impacts companies and consumers in practice)."),
            ("What is the EU's global economic weight?", "~450-500 million citizens, ~14-15% of global GDP, approximately 30% of global trade. The world's largest single market. Also the world's largest development aid donor. Despite being a major force, it faces challenges from the USA (services/digital) and China (manufacturing)."),
            ("What is 'strategic autonomy' and why is the EU pursuing it?", "Strategic autonomy means reducing the EU's dependence on foreign suppliers for critical goods and technologies. Triggered by COVID (medicine shortages), the Ukraine war (energy dependence on Russia), and US-China tensions (chip supply chain risks). The EU wants to produce more critical goods domestically or with trusted partners."),
            ("What is the Erasmus programme and what EU principle does it embody?", "Erasmus is the EU student exchange programme, allowing students to study at any EU university with credits recognized across all member states (ECTS system). It embodies the free movement of people and the idea of a shared European identity and education space."),
            ("Why is price transparency an advantage of the euro for businesses?", "With the euro, a French company can directly compare prices from German, Italian and Spanish suppliers without currency conversion. This forces suppliers to compete on quality and efficiency, not just exchange rate advantages, ultimately benefiting consumers through lower prices."),
            ("What is a 'free rider' in the EU context?", "A free rider is a Member State (or actor) that benefits from EU integration and its collective goods (Single Market access, security, standards) without contributing proportionally to the costs. Example: a small country enjoying the full benefits of the Single Market while lobbying for minimal budget contributions."),
            ("What is 'critical mass' in an EU context?", "Critical mass is the minimum level of support or participation needed to have significant influence within the EU system. A single small country has little leverage; but a coalition representing enough population and economic weight can shift EU policy. Example: France + Germany + Italy forming a bloc to influence Commission decisions."),
            ("What are the key VUCA challenges facing EU businesses today?", "Volatility: rapid market changes (COVID disruptions, war in Ukraine). Uncertainty: unpredictable geopolitical outcomes, energy prices. Complexity: global supply chains with many interdependent actors. Ambiguity: unclear regulatory future (Green Deal rules still evolving, AI regulation uncertain). The EU Single Market helps buffer some VUCA effects by providing regulatory stability."),
        ]
    },
]

# ─────────────────────────────────────────────────────────────
# GENERATE CLAUDE.md FILES
# ─────────────────────────────────────────────────────────────

def build_claude_md(ch):
    lines = []
    lines.append(f"# {ch['title']}")
    lines.append(f"> {ch['subtitle']}\n")
    lines.append("---\n")
    lines.append("## PART 1 — COMPLETE SYNTHESIS\n")
    lines.append(ch['synthesis'].strip())
    lines.append("\n\n---\n")
    lines.append("## PART 2 — Q&A EXAM FORMAT\n")
    lines.append("> Format: Q → A. Cover definitions, distinctions, mechanisms, examples.\n")
    for i, (q, a) in enumerate(ch['qa'], 1):
        lines.append(f"**Q{i}: {q}**")
        lines.append(f"> A: {a}\n")
    return "\n".join(lines)


def write_claude_md(ch):
    path = os.path.join(BASE, ch['claude_path'])
    os.makedirs(os.path.dirname(path), exist_ok=True)
    content = build_claude_md(ch)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  Written: {ch['claude_path']}")


# ─────────────────────────────────────────────────────────────
# PDF GENERATION
# ─────────────────────────────────────────────────────────────

EU_BLUE = colors.HexColor('#003399')
EU_YELLOW = colors.HexColor('#FFCC00')
LIGHT_BLUE = colors.HexColor('#E8EEF7')
LIGHT_GREY = colors.HexColor('#F5F5F5')
DARK_GREY = colors.HexColor('#333333')
MID_GREY = colors.HexColor('#666666')
QA_Q_BG = colors.HexColor('#EEF3FB')
QA_A_BG = colors.HexColor('#FAFAFA')


def build_styles():
    base = getSampleStyleSheet()
    s = {}

    s['cover_title'] = ParagraphStyle('cover_title',
        fontName='Helvetica-Bold', fontSize=26, textColor=colors.white,
        alignment=TA_CENTER, spaceAfter=8, leading=32)
    s['cover_sub'] = ParagraphStyle('cover_sub',
        fontName='Helvetica', fontSize=13, textColor=EU_YELLOW,
        alignment=TA_CENTER, spaceAfter=6, leading=18)
    s['cover_meta'] = ParagraphStyle('cover_meta',
        fontName='Helvetica', fontSize=10, textColor=colors.HexColor('#CCDDFF'),
        alignment=TA_CENTER, spaceAfter=4)

    s['part_header'] = ParagraphStyle('part_header',
        fontName='Helvetica-Bold', fontSize=15, textColor=colors.white,
        alignment=TA_CENTER, spaceAfter=4, spaceBefore=8,
        backColor=EU_BLUE, borderPad=8, leading=20)

    s['h2'] = ParagraphStyle('h2',
        fontName='Helvetica-Bold', fontSize=13, textColor=EU_BLUE,
        spaceBefore=14, spaceAfter=4, leading=17,
        borderPad=4)
    s['h3'] = ParagraphStyle('h3',
        fontName='Helvetica-Bold', fontSize=11, textColor=DARK_GREY,
        spaceBefore=8, spaceAfter=3, leading=15)

    s['body'] = ParagraphStyle('body',
        fontName='Helvetica', fontSize=10, textColor=DARK_GREY,
        spaceBefore=3, spaceAfter=3, leading=15, alignment=TA_JUSTIFY)
    s['bullet'] = ParagraphStyle('bullet',
        fontName='Helvetica', fontSize=10, textColor=DARK_GREY,
        spaceBefore=2, spaceAfter=2, leading=14,
        leftIndent=16, bulletIndent=6)

    s['qa_q'] = ParagraphStyle('qa_q',
        fontName='Helvetica-Bold', fontSize=10, textColor=EU_BLUE,
        spaceBefore=8, spaceAfter=2, leading=14,
        backColor=QA_Q_BG, borderPad=6, leftIndent=4)
    s['qa_a'] = ParagraphStyle('qa_a',
        fontName='Helvetica', fontSize=10, textColor=DARK_GREY,
        spaceBefore=2, spaceAfter=6, leading=14,
        leftIndent=12, backColor=QA_A_BG, borderPad=4)
    s['qa_num'] = ParagraphStyle('qa_num',
        fontName='Helvetica-Bold', fontSize=9, textColor=MID_GREY,
        spaceBefore=0, spaceAfter=0)

    s['table_header'] = ParagraphStyle('table_header',
        fontName='Helvetica-Bold', fontSize=9, textColor=colors.white,
        alignment=TA_CENTER, leading=12)
    s['table_cell'] = ParagraphStyle('table_cell',
        fontName='Helvetica', fontSize=9, textColor=DARK_GREY,
        leading=12, alignment=TA_LEFT)

    return s


def make_table(headers, rows, styles_map, col_widths=None):
    s = styles_map
    header_row = [Paragraph(h, s['table_header']) for h in headers]
    data = [header_row]
    for row in rows:
        data.append([Paragraph(str(c), s['table_cell']) for c in row])

    page_w = A4[0] - 4*cm
    if col_widths is None:
        n = len(headers)
        col_widths = [page_w / n] * n

    t = Table(data, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), EU_BLUE),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 9),
        ('ALIGN', (0,0), (-1,0), 'CENTER'),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [LIGHT_GREY, colors.white]),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CCCCCC')),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    return t


def add_header_footer(canvas, doc):
    canvas.saveState()
    w, h = A4
    # Header bar
    canvas.setFillColor(EU_BLUE)
    canvas.rect(0, h - 1.2*cm, w, 1.2*cm, fill=1, stroke=0)
    canvas.setFillColor(EU_YELLOW)
    canvas.setFont('Helvetica-Bold', 8)
    canvas.drawString(1.5*cm, h - 0.8*cm, "EBE — European Business & Economics | EPHEC | Prof. Ducobu")
    canvas.setFillColor(colors.white)
    canvas.drawRightString(w - 1.5*cm, h - 0.8*cm, f"Page {doc.page}")
    # Footer
    canvas.setFillColor(EU_BLUE)
    canvas.rect(0, 0, w, 0.8*cm, fill=1, stroke=0)
    canvas.setFillColor(EU_YELLOW)
    canvas.setFont('Helvetica', 7)
    canvas.drawCentredString(w/2, 0.25*cm, "Study material — Exam preparation June 2026")
    canvas.restoreState()


def generate_pdf(ch, s):
    pdf_path = os.path.join(BASE, ch['pdf_name'])
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=A4,
        leftMargin=2*cm, rightMargin=2*cm,
        topMargin=2*cm, bottomMargin=1.5*cm,
        title=ch['title'],
        author="EBE Study Guide"
    )

    story = []
    page_w = A4[0] - 4*cm

    # ── COVER PAGE ───────────────────────────────────────────
    cover_data = [[
        Paragraph(f"Chapter {ch['num']}", ParagraphStyle('cn',
            fontName='Helvetica', fontSize=14, textColor=EU_YELLOW,
            alignment=TA_CENTER, spaceAfter=4)),
        Paragraph(ch['title'].replace(f"Chapter {ch['num']} — ", ""), s['cover_title']),
        Paragraph(ch['subtitle'], s['cover_sub']),
        Paragraph("European Business & Economics  •  EPHEC  •  Prof. Y.-D. Ducobu  •  Exam: 28 May 2026", s['cover_meta']),
    ]]
    cover_table = Table([[item] for item in cover_data[0]],
                        colWidths=[page_w + 2*cm])
    cover_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), EU_BLUE),
        ('TOPPADDING', (0,0), (-1,-1), 12),
        ('BOTTOMPADDING', (0,0), (-1,-1), 12),
        ('LEFTPADDING', (0,0), (-1,-1), 20),
        ('RIGHTPADDING', (0,0), (-1,-1), 20),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(Spacer(1, 2*cm))
    story.append(cover_table)
    story.append(Spacer(1, 0.5*cm))

    # TOC hint
    toc_items = [f"Part 1: Complete Synthesis — all key concepts with examples",
                 f"Part 2: Q&A Exam Format — {len(ch['qa'])} questions & answers"]
    for item in toc_items:
        story.append(Paragraph(f"• {item}", s['bullet']))
    story.append(PageBreak())

    # ── PART 1: SYNTHESIS ────────────────────────────────────
    part1_header = Table([[Paragraph("PART 1 — COMPLETE SYNTHESIS", s['part_header'])]],
                         colWidths=[page_w])
    part1_header.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), EU_BLUE),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(part1_header)
    story.append(Spacer(1, 0.3*cm))

    # Parse synthesis text
    for line in ch['synthesis'].strip().split('\n'):
        line = line.rstrip()
        if line.startswith('## '):
            story.append(Spacer(1, 0.2*cm))
            story.append(HRFlowable(width=page_w, thickness=1.5, color=EU_BLUE))
            story.append(Paragraph(line[3:], s['h2']))
        elif line.startswith('### '):
            story.append(Paragraph(line[4:], s['h3']))
        elif line.startswith('| ') and '|' in line[2:]:
            # Table row — collect all consecutive table lines
            pass  # handled below via block parsing
        elif line.startswith('- **') or line.startswith('- '):
            txt = md_bold(line[2:])
            story.append(Paragraph(f"• {txt}", s['bullet']))
        elif line.startswith('1. ') or line.startswith('2. ') or line.startswith('3. '):
            txt = md_bold(line[3:])
            num = line[0]
            story.append(Paragraph(f"{num}. {txt}", s['bullet']))
        elif line == '' or line == '---':
            story.append(Spacer(1, 0.15*cm))
        else:
            story.append(Paragraph(md_bold(line), s['body']))

    # Re-parse synthesis for tables properly
    story2 = []
    lines_syn = ch['synthesis'].strip().split('\n')
    i = 0
    while i < len(lines_syn):
        line = lines_syn[i].rstrip()
        if line.startswith('## '):
            story2.append(Spacer(1, 0.2*cm))
            story2.append(HRFlowable(width=page_w, thickness=1.5, color=EU_BLUE))
            story2.append(Paragraph(line[3:], s['h2']))
            i += 1
        elif line.startswith('### '):
            story2.append(Paragraph(line[4:], s['h3']))
            i += 1
        elif line.startswith('| '):
            # Collect table block
            table_lines = []
            while i < len(lines_syn) and lines_syn[i].startswith('|'):
                table_lines.append(lines_syn[i])
                i += 1
            # Parse
            rows = []
            for tl in table_lines:
                if set(tl.replace('|', '').replace('-', '').replace(' ', '')) == set():
                    continue  # separator row
                cells = [c.strip() for c in tl.strip('|').split('|')]
                rows.append(cells)
            if len(rows) >= 2:
                headers = rows[0]
                data_rows = rows[1:]
                n = len(headers)
                cw = [page_w / n] * n
                story2.append(make_table(headers, data_rows, s, cw))
                story2.append(Spacer(1, 0.2*cm))
        elif line.startswith('- '):
            txt = line[2:]
            # Handle bold
            out = ''
            parts = txt.split('**')
            for idx, part in enumerate(parts):
                if idx % 2 == 1:
                    out += f'<b>{part}</b>'
                else:
                    out += part
            story2.append(Paragraph(f"• {out}", s['bullet']))
            i += 1
        elif line and line[0].isdigit() and len(line) > 2 and line[1] == '.':
            txt = line[3:]
            out = ''
            parts = txt.split('**')
            for idx, part in enumerate(parts):
                if idx % 2 == 1:
                    out += f'<b>{part}</b>'
                else:
                    out += part
            story2.append(Paragraph(f"{line[0]}. {out}", s['bullet']))
            i += 1
        elif line == '' or line == '---':
            story2.append(Spacer(1, 0.12*cm))
            i += 1
        else:
            out = ''
            parts = line.split('**')
            for idx, part in enumerate(parts):
                if idx % 2 == 1:
                    out += f'<b>{part}</b>'
                else:
                    out += part
            story2.append(Paragraph(out, s['body']))
            i += 1

    # Replace story content after part1 header with story2
    # Find the index after part1_header in story
    story_final = story[:2]  # cover table + spacer
    for item in toc_items:
        story_final.append(Paragraph(f"• {item}", s['bullet']))
    story_final.append(PageBreak())
    story_final.append(part1_header)
    story_final.append(Spacer(1, 0.3*cm))
    story_final.extend(story2)

    # ── PART 2: Q&A ──────────────────────────────────────────
    story_final.append(PageBreak())
    part2_header = Table([[Paragraph(f"PART 2 — Q&A EXAM FORMAT ({len(ch['qa'])} Questions)", s['part_header'])]],
                         colWidths=[page_w])
    part2_header.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), EU_BLUE),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
    ]))
    story_final.append(part2_header)
    story_final.append(Spacer(1, 0.4*cm))

    for idx, (q, a) in enumerate(ch['qa'], 1):
        qa_block = [
            Paragraph(f"Q{idx} &nbsp; {q}", s['qa_q']),
            Paragraph(a, s['qa_a']),
        ]
        story_final.append(KeepTogether(qa_block))

    doc.build(story_final,
              onFirstPage=add_header_footer,
              onLaterPages=add_header_footer)
    print(f"  PDF generated: {ch['pdf_name']}")


# ─────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────

def main():
    s = build_styles()
    print("\n=== Generating CLAUDE.md files ===")
    for ch in CHAPTERS:
        write_claude_md(ch)

    print("\n=== Generating PDFs ===")
    for ch in CHAPTERS:
        generate_pdf(ch, s)

    print("\n✓ All files generated successfully.")
    print(f"  Location: {BASE}")


if __name__ == '__main__':
    main()
