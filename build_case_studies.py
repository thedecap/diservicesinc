#!/usr/bin/env python3
"""Generate the six polished case-study pages from a single template.

The header, footer, and styling are mirrored from cloud-providers.html so the
case studies feel like a first-class part of the site. Each page gets unique
content, a unique banner image, and a "More case studies" cross-link section.
"""

from pathlib import Path

ROOT = Path(__file__).parent

# ---------------------------------------------------------------------------
# Case study content
# ---------------------------------------------------------------------------

CASES = [
    {
        "slug": "supply-chain",
        "filename": "case-study-supply-chain.html",
        "image": "web/images/casestudy_images/65b94bd409c60_cloud-mis-01.png",
        "hero_image": "web/images/data-analytic_hq.jpg",
        "page_title": "Supply Chain Optimization Case Study | DIS Services Inc",
        "meta_description": "How DIS reduced supply chain inefficiencies by 20% for a global retail chain with a Unified Data Platform on Microsoft Azure.",
        "hero_main": "Supply Chain",
        "hero_accent": "Optimization",
        "industry": "Global Retail",
        "headline": "Cutting Supply Chain Inefficiencies by 20% for a Global Retail Chain",
        "summary": "A unified data platform on Microsoft Azure replaced data silos with real-time, network-wide visibility — enabling faster decisions and a leaner supply chain.",
        "challenge_short": "Geographically dispersed retail operations were trapped behind data silos, blocking real-time decisions and cross-region collaboration.",
        "benefits": [
            "Enhanced data quality and consistency across the organization.",
            "Real-time, unified business intelligence dashboards for timely insights.",
            "20% reduction in supply chain inefficiencies through better data flow.",
        ],
        "challenge_body": (
            "A leading global retail chain came to Data Integrity Services with a familiar but stubborn problem: "
            "valuable information was scattered across regional systems that couldn't talk to each other. Sales, "
            "inventory, supplier, and logistics data each lived in its own silo, making it impossible to see the "
            "full picture of the supply chain at any given moment. Branch managers were forced to make decisions "
            "from outdated reports, while head office struggled to spot trends until they had already caused "
            "stock-outs or excess inventory. The dispersed nature of operations magnified every gap — what should "
            "have been a routine reorder turned into a multi-day reconciliation exercise. The retailer needed more "
            "than another report; it needed a single source of truth that every region, function, and decision-maker "
            "could rely on in real time."
        ),
        "approach_lead": (
            "DIS designed and rolled out a Unified Data Platform on Microsoft Azure, integrating every relevant "
            "system into one governed, real-time fabric — and layering modern analytics and machine learning on top."
        ),
        "approach_steps": [
            "Conducted a comprehensive assessment of existing data systems and pinpointed key pain points.",
            "Built a customized Unified Data Platform tailored to the retailer's network and objectives.",
            "Integrated sales, inventory, customer behavior, and supply chain data into one centralized platform.",
            "Deployed advanced analytics for real-time insight, predictive modeling, and trend analysis.",
        ],
        "solution_lead": (
            "The new platform did more than fix the immediate visibility problem — it gave the retailer a "
            "scalable foundation for the next decade of growth. Decision-making accelerated, planning got tighter, "
            "and the leadership team finally had numbers everyone could trust."
        ),
        "solution_results": [
            "Streamlined data access and analysis, dramatically reducing decision-making time.",
            "Stronger cross-functional collaboration across global teams and regions.",
            "Predictive analytics now optimize inventory and marketing, lifting revenue.",
            "Architecture proven scalable as data volumes continue to grow.",
        ],
        "quote": (
            "DIS sets the gold standard in partnering with Microsoft Azure, where precision meets security. "
            "With an unwavering commitment to safeguarding information and ensuring its accuracy, DIS is the "
            "beacon of trust in data management."
        ),
    },
    {
        "slug": "cloud-migration",
        "filename": "case-study-cloud-migration.html",
        "image": "web/images/casestudy_images/65b95d5c54bb0_cloud-mis-02.png",
        "hero_image": "web/images/cloud-pro-img02_hq.jpg",
        "page_title": "Secure Cloud Migration Case Study | DIS Services Inc",
        "meta_description": "How DIS led a financial institution through a secure, compliant migration to Microsoft Azure with zero data loss.",
        "hero_main": "Secure Cloud",
        "hero_accent": "Migration",
        "industry": "Financial Services",
        "headline": "Protected Cloud Migration for a Large Financial Institution",
        "summary": "An end-to-end migration to Microsoft Azure that put compliance, encryption, and uptime first — with zero data loss and no disruption to customer-facing services.",
        "challenge_short": "A regulated financial institution needed to move to the cloud without exposing sensitive data, missing a regulation, or interrupting service.",
        "benefits": [
            "Smooth cloud transition with zero data loss and no security incidents.",
            "Improved scalability and performance in the new cloud environment.",
            "Full compliance with industry regulations, deepening customer trust.",
        ],
        "challenge_body": (
            "For Data Integrity Services, the challenge was guiding a financial institution through one of the most "
            "high-stakes moves any regulated business can make: shifting core systems to the public cloud while "
            "protecting deeply sensitive customer data. Security concerns, regulatory compliance, and the absolute "
            "requirement of uninterrupted service were non-negotiable. Every workload had to be assessed, every "
            "control mapped to a specific regulation, and every cutover staged so customers never saw a hiccup. "
            "The team had to balance the efficiency gains of Azure against the institution's obligation to keep "
            "financial data confidential, accurate, and continuously available — a balance that left no margin "
            "for error."
        ),
        "approach_lead": (
            "DIS built a phased migration strategy anchored in end-to-end encryption, multi-layered identity, "
            "and compliance-driven controls — designed so security and uptime travelled with the workload."
        ),
        "approach_steps": [
            "Ran a thorough discovery sweep of existing systems to surface vulnerabilities before they moved.",
            "Tailored security controls to the unique requirements of financial data and regulatory standards.",
            "Implemented advanced encryption for data in transit and at rest throughout the migration.",
            "Stood up real-time monitoring for immediate threat detection and incident response.",
        ],
        "solution_lead": (
            "DIS delivered a textbook secure migration: not just a lift-and-shift, but a measurable upgrade in the "
            "institution's overall security posture. The result is a cloud footprint the institution can confidently "
            "audit, scale, and build the next generation of services on."
        ),
        "solution_results": [
            "Preserved the integrity and confidentiality of financial data through every phase.",
            "Cleared complex regulatory requirements without a single non-conformance.",
            "Executed cutovers with minimal disruption to day-to-day operations.",
            "Strengthened security posture with proactive controls and continuous monitoring.",
        ],
        "quote": (
            "DIS excels in collaboration with Microsoft Azure, blending precision with security. Their dedication "
            "to keeping information safe and accurate makes them a trusted figure in data management."
        ),
    },
    {
        "slug": "data-warehouse",
        "filename": "case-study-data-warehouse.html",
        "image": "web/images/casestudy_images/65b954ad233ae_cloud-mis-05.png",
        "hero_image": "web/images/data-visualization_hq.jpg",
        "page_title": "Azure Synapse Data Warehouse Case Study | DIS Services Inc",
        "meta_description": "How DIS modernized a legacy data warehouse with Azure Synapse Analytics, halving processing time and unlocking real-time analytics.",
        "hero_main": "Data Warehouse",
        "hero_accent": "Modernization",
        "industry": "Enterprise Analytics",
        "headline": "Revolutionising the Data Warehouse with Azure Synapse Analytics",
        "summary": "A legacy warehouse that had hit its ceiling was replaced with Azure Synapse Analytics — cutting processing time in half and enabling real-time, business-wide insight.",
        "challenge_short": "Traditional data warehousing was slowing the business down — query times were creeping up, scale was painful, and analysts were waiting on yesterday's numbers.",
        "benefits": [
            "50% reduction in data processing time across critical pipelines.",
            "Effortless scalability as data volumes continue to grow.",
            "Augmented analytics that make data-driven decisions the default.",
        ],
        "challenge_body": (
            "A large enterprise approached DIS with a problem hiding in plain sight: their data warehouse was "
            "still running, but it was no longer the asset it used to be. Queries that once took minutes were "
            "taking hours. New data sources were piling up faster than the team could onboard them. Executives "
            "asking for a quick view of the business were being told to wait until the overnight job ran. The "
            "limitations of traditional data warehousing methods were no longer just a technical inconvenience — "
            "they were holding the entire organization back from making informed, timely decisions. DIS recognized "
            "that the fix wasn't more hardware on the existing platform; it was a fundamentally different architecture "
            "built for the volume, variety, and velocity of modern data."
        ),
        "approach_lead": (
            "DIS modernized the warehouse with Azure Synapse Analytics — combining enterprise data warehousing "
            "and big data analytics into a single platform that scales elastically and queries in real time."
        ),
        "approach_steps": [
            "Audited the existing data infrastructure end-to-end and clarified business requirements.",
            "Architected and deployed Azure Synapse Analytics as the new warehousing core.",
            "Migrated historical data from the legacy warehouse with no loss of fidelity.",
            "Trained analyst teams on the new analytics, modeling, and reporting capabilities.",
        ],
        "solution_lead": (
            "Synapse didn't just replace the legacy stack — it changed the way the business thought about data. "
            "The team can now answer questions in seconds that used to take days, and the platform scales as "
            "fast as the company does."
        ),
        "solution_results": [
            "Elastic scale to match changing data volumes and workloads.",
            "Real-time insights replace overnight batch reporting.",
            "Diverse data sources unified into a single, holistic view.",
            "Operational efficiency lifted across every analytics-driven team.",
        ],
        "quote": (
            "DIS leads the way in teaming up with Microsoft Azure, bringing together precision and security "
            "seamlessly. Choose DIS to enhance your data integrity — where every insight is backed by trust."
        ),
    },
    {
        "slug": "ai-maintenance",
        "filename": "case-study-ai-maintenance.html",
        "image": "web/images/casestudy_images/65b95d223a602_cloud-mis-04.png",
        "hero_image": "web/images/joinus-img02_hq.jpg",
        "page_title": "AI-Driven Predictive Maintenance Case Study | DIS Services Inc",
        "meta_description": "How DIS slashed equipment downtime by 30% at a manufacturing plant using AI-driven predictive maintenance on Microsoft Azure.",
        "hero_main": "AI Predictive",
        "hero_accent": "Maintenance",
        "industry": "Manufacturing",
        "headline": "From Equipment Breakdowns to Significant Cost Savings with AI-Driven Maintenance",
        "summary": "An AI predictive-maintenance platform on Microsoft Azure replaced costly reactive servicing with proactive insight — cutting downtime by 30% and lifting overall equipment effectiveness.",
        "challenge_short": "Reactive maintenance was eating into productivity. The plant needed a way to see failures coming, not clean up after them.",
        "benefits": [
            "30% reduction in equipment downtime through proactive maintenance.",
            "Substantial cost savings from optimized maintenance schedules.",
            "Improved overall equipment effectiveness and production efficiency.",
        ],
        "challenge_body": (
            "A struggling manufacturing plant approached DIS with an urgent request: stop the bleeding from "
            "unplanned downtime. Their existing maintenance strategy was reactive by design — wait for something "
            "to break, then race to fix it. That approach was expensive in two ways. First, the obvious one: "
            "emergency repairs cost more than scheduled ones. Second, and more damaging: every breakdown stopped "
            "a production line that the rest of the business depended on. Traditional methods couldn't see "
            "failures coming; they could only respond to them. To turn that around, the plant needed continuous, "
            "data-driven visibility into equipment health, plus the ability to act on that visibility before "
            "failures occurred."
        ),
        "approach_lead": (
            "DIS proposed an AI-driven predictive maintenance solution built on Microsoft Azure — combining "
            "advanced analytics, machine learning, and live telemetry from the plant floor."
        ),
        "approach_steps": [
            "Assessed existing machinery, historical maintenance data, and operational patterns in detail.",
            "Trained tailored AI models to predict failures from real-time data and historical trends.",
            "Integrated the predictive system with existing plant infrastructure for continuous monitoring.",
            "Trained plant personnel to act on the AI-driven maintenance insights effectively.",
        ],
        "solution_lead": (
            "The plant moved from firefighting to forecasting. Maintenance now happens on the AI's schedule — "
            "before a breakdown, not after — and the savings show up in both the maintenance budget and the "
            "production numbers."
        ),
        "solution_results": [
            "Significant drop in unplanned downtime through proactive scheduling.",
            "Maintenance costs reduced by focusing resources where they matter.",
            "Improved overall plant efficiency and equipment performance.",
            "Plant management now has predictive insight to drive decisions.",
        ],
        "quote": (
            "DIS establishes a pinnacle of excellence in collaboration with Microsoft Azure, merging precision "
            "and security seamlessly. Through cutting-edge technology, DIS epitomizes reliability."
        ),
    },
    {
        "slug": "data-security",
        "filename": "case-study-data-security.html",
        "image": "web/images/casestudy_images/65b95d926050e_cloud-mis-03.png",
        "hero_image": "web/images/joinus-img01_hq.jpg",
        "page_title": "Banking Data Security Case Study | DIS Services Inc",
        "meta_description": "How DIS rebuilt the security posture of a large financial institution with a zero-trust, Azure-native architecture.",
        "hero_main": "Banking Data",
        "hero_accent": "Security",
        "industry": "Financial Services",
        "headline": "Saving a Large Financial Institution by Securing Their Data Through the Cloud",
        "summary": "A zero-trust, Azure-native security overhaul that closed the gaps left by aging on-prem infrastructure — and gave a regulated financial institution a defensible posture for the next decade.",
        "challenge_short": "Legacy infrastructure was leaving sensitive customer data exposed at exactly the moment cyber threats and regulators were tightening the screws.",
        "benefits": [
            "Zero-trust architecture established across the entire estate.",
            "Customer data encrypted at rest and in transit, end to end.",
            "Compliance audits passed first time, with documented controls.",
        ],
        "challenge_body": (
            "When a large financial institution came to Data Integrity Services, the situation was urgent. Their "
            "on-premises infrastructure had served them well for years, but it was no longer keeping pace with "
            "the threat landscape. Attack surfaces were expanding, sensitive customer data was sitting in systems "
            "that predated modern security practices, and regulators were beginning to ask harder questions. A "
            "single breach would mean reputational damage, regulatory penalties, and a loss of customer trust "
            "that no marketing budget could fix. The institution needed more than perimeter patching — it needed "
            "a fundamentally different security model, designed for a world where every request must be verified "
            "and every byte must be protected."
        ),
        "approach_lead": (
            "DIS led a cloud-anchored security overhaul: a zero-trust architecture on Microsoft Azure with "
            "identity-driven access, continuous threat detection, and encryption woven into every layer."
        ),
        "approach_steps": [
            "Mapped sensitive data, classified it, and built encryption controls around the highest-risk stores.",
            "Adopted a zero-trust model with identity-driven access using Microsoft Entra ID.",
            "Deployed Microsoft Defender for Cloud for continuous threat detection across the estate.",
            "Codified compliance controls so every audit can be evidenced from a single source of truth.",
        ],
        "solution_lead": (
            "The institution now operates from a defensible, modern security baseline. Threats are detected in "
            "real time, sensitive data is unreadable to anyone outside the trust boundary, and audits no longer "
            "require a months-long scramble for evidence."
        ),
        "solution_results": [
            "Continuous monitoring and automated response to suspicious activity.",
            "Granular, identity-aware access control for every system and dataset.",
            "Customer financial data fully encrypted at rest and in transit.",
            "Audit-ready evidence available on demand, not gathered after the fact.",
        ],
        "quote": (
            "Data security isn't a project — it's an architecture. DIS gave us one we can defend, audit, and "
            "build on for the next decade of regulatory change."
        ),
    },
    {
        "slug": "hr-automation",
        "filename": "case-study-hr-automation.html",
        "image": "web/images/wecare-img02.jpg",
        "hero_image": "web/images/wecare-img02_hq.jpg",
        "page_title": "HR Onboarding Automation Case Study | DIS Services Inc",
        "meta_description": "How DIS cut onboarding time by 30% for a large HR team using Microsoft Power Automate and Azure AI services.",
        "hero_main": "HR Onboarding",
        "hero_accent": "Automation",
        "industry": "Human Resources",
        "headline": "Cutting Onboarding Time and Paperwork by 30% with Power Automate and Azure AI",
        "summary": "An end-to-end onboarding flow built on Microsoft Power Automate and Azure AI — replacing weeks of manual paperwork with same-day, error-free processing.",
        "challenge_short": "A large HR team was buried under manual onboarding paperwork. New hires were waiting weeks to start, and the team was waiting days to process each one.",
        "benefits": [
            "30% reduction in total onboarding time, from offer to first day.",
            "Paper forms eliminated — every step happens digitally.",
            "Faster time-to-productivity for every new hire.",
        ],
        "challenge_body": (
            "A large HR organization came to Data Integrity Services with a problem any growing company will "
            "recognise. Onboarding had become the team's biggest bottleneck. Every new hire generated a stack of "
            "forms that had to be collected, transcribed into multiple systems, validated for accuracy, and "
            "filed for compliance — all by hand. As headcount grew, the HR team couldn't grow fast enough to "
            "keep up. New hires were waiting days for accounts, equipment, and access. Recruiters were spending "
            "their time chasing paperwork instead of finding talent. And the manual transcription created exactly "
            "the kind of small errors that lead to large problems later. The HR team needed to automate the boring, "
            "error-prone parts of onboarding without losing the human touch that made their welcome experience work."
        ),
        "approach_lead": (
            "DIS designed an end-to-end automated onboarding workflow using Microsoft Power Automate, Azure AI "
            "Document Intelligence, and SharePoint — keeping HR in control while letting the platform handle the heavy lifting."
        ),
        "approach_steps": [
            "Mapped the existing onboarding journey end-to-end and identified every manual handoff.",
            "Built Power Automate flows to orchestrate offers, forms, approvals, and provisioning.",
            "Used Azure AI Document Intelligence to extract data from uploaded ID and tax documents automatically.",
            "Connected the workflow to SharePoint and the HRIS so every record updates in lockstep.",
        ],
        "solution_lead": (
            "Onboarding is now something that happens to a new hire, not something the HR team has to do for "
            "them. New employees are productive on day one, and the HR team is finally free to spend their "
            "time on the work only humans can do."
        ),
        "solution_results": [
            "Onboarding cycle time cut by 30%, from offer letter to first day.",
            "Manual data entry replaced with AI-driven document parsing.",
            "Approvals routed automatically, with full audit trail.",
            "HR team freed from paperwork to focus on people, not forms.",
        ],
        "quote": (
            "Power Automate and Azure AI gave our HR team their week back. New hires feel taken care of, and "
            "we have an audit trail for every step — without anyone touching a paper form."
        ),
    },
]

# ---------------------------------------------------------------------------
# Shared template fragments (mirrored from cloud-providers.html)
# ---------------------------------------------------------------------------

HEAD_AND_STYLE = r"""<!doctype html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>__PAGE_TITLE__</title>

    <meta name="description" content="__META_DESCRIPTION__">
    <meta name="robots" content="index, follow">
    <meta name="author" content="DIS Services Inc">
    <meta name="theme-color" content="#3482ad">
    <link rel="canonical" href="__FILENAME__">

    <meta property="og:title" content="__PAGE_TITLE__">
    <meta property="og:description" content="__META_DESCRIPTION__">
    <meta property="og:image" content="/__IMAGE__">
    <meta property="og:url" content="__FILENAME__">
    <meta property="og:type" content="article">
    <meta property="og:site_name" content="DIS Services Inc">
    <meta property="og:locale" content="en_US">

    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="__PAGE_TITLE__">
    <meta name="twitter:description" content="__META_DESCRIPTION__">
    <meta name="twitter:image" content="/__IMAGE__">

    <link rel="shortcut icon" href="web/images/favicon.ico" type="image/x-icon">
    <link rel="icon" href="web/images/favicon.ico" type="image/x-icon">

    <link rel="stylesheet" type="text/css" href="web/css/stylenew.css">
    <link href="https://fonts.googleapis.com/css2?family=Play:wght@400;700&display=swap" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link
        href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600&family=Inter:wght@100;200;300;400;500;600&family=Play:wght@400;700&family=Plus+Jakarta+Sans:wght@200;300;400;500;600;700&display=swap"
        rel="stylesheet">

    <style>
        html { scroll-behavior: smooth }
        * { -webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale }
        body { background: #fff !important; overflow-x: hidden }

        /* ---------- Header ---------- */
        body main div.headercls {
            position: fixed !important; top: 0 !important; left: 0 !important; right: 0 !important;
            z-index: 9000 !important; background: rgba(255,255,255,.88) !important;
            backdrop-filter: blur(20px) saturate(180%) !important;
            -webkit-backdrop-filter: blur(20px) saturate(180%) !important;
            border-bottom: none !important; box-shadow: 0 0 0 1px rgba(0,0,0,.04) !important;
            transition: all .35s ease !important; padding: 0 !important
        }
        body main div.headercls.scrolled { background: rgba(255,255,255,.96) !important; box-shadow: 0 0 0 1px rgba(0,0,0,.04), 0 2px 12px rgba(0,0,0,.04) !important }
        body > main { padding-top: 72px !important }
        body main .headercls .navbar { padding: 8px 0 !important; min-height: 56px !important }
        body main .headercls .navbar .container-fluid { max-width: 1200px !important; margin: 0 auto !important }
        body main .headercls #mainlogo { gap: 8px !important }
        body main .headercls #mainlogo img.logo1 { height: 30px !important; transition: opacity .2s !important }
        body main .headercls #mainlogo img.logo2 { height: 24px !important; transition: opacity .2s !important }
        body main .headercls #mainlogo span { height: 32px !important; background: rgba(52,130,173,.25) !important }
        body main .homenav .nav { gap: 2px !important }
        body main .homenav .nav .nav-item .nav-link {
            font-family: 'Plus Jakarta Sans', sans-serif !important; font-weight: 500 !important;
            font-size: 13px !important; color: #424245 !important; padding: 6px 12px !important;
            border-radius: 6px !important; transition: color .15s, background .15s !important; white-space: nowrap !important
        }
        body main .homenav .nav .nav-item .nav-link:hover { color: #1d1d1f !important; background: rgba(0,0,0,.04) !important }
        body main .headercls .navbar-toggler { border: none !important; padding: 4px 8px !important; box-shadow: none !important }
        body main .headercls .navbar-toggler:focus { box-shadow: none !important }

        /* ---------- Hero banner ---------- */
        .bannerslider.oneuspage { position: relative !important; margin-bottom: 0 !important; overflow: hidden !important; min-height: 56vh !important }
        .bannerslider.oneuspage > img { position: absolute !important; inset: 0 !important; width: 100% !important; height: 100% !important; object-fit: cover !important; filter: brightness(.42) !important; z-index: 0 !important }
        .bannerslider.oneuspage::after { content: '' !important; position: absolute !important; inset: 0 !important; background: linear-gradient(to bottom, rgba(0,0,0,.15) 0%, rgba(0,0,0,.65) 100%) !important; pointer-events: none !important; z-index: 1 !important }
        .bannerslider .captionheader.shadownone.lefttextcap.nohome { position: absolute !important; top: 0 !important; left: 0 !important; right: 0 !important; bottom: 0 !important; display: flex !important; align-items: center !important; justify-content: center !important; z-index: 2 !important; height: 100% !important; padding: 0 !important; margin: 0 !important }
        .bannerslider .captionheader.shadownone .container { display: flex !important; flex-direction: column !important; align-items: center !important; justify-content: center !important; height: auto !important; text-align: center !important }
        .bannerslider .captionheader .eyebrow {
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            font-size: .72rem !important; font-weight: 600 !important;
            letter-spacing: .18em !important; text-transform: uppercase !important;
            color: #7ec8f0 !important; margin-bottom: 18px !important;
            display: inline-block !important;
            padding: 6px 14px !important;
            border: 1px solid rgba(126,200,240,.4) !important;
            border-radius: 980px !important;
            background: rgba(126,200,240,.08) !important;
        }
        .bannerslider .captionheader h1 {
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            font-size: clamp(2.2rem, 5vw, 4rem) !important;
            font-weight: 700 !important; line-height: 1.08 !important;
            letter-spacing: -.03em !important; color: #fff !important;
            max-width: 920px !important; margin: 0 auto !important;
        }
        .bannerslider .captionheader h1 span { color: #7ec8f0 !important; -webkit-text-fill-color: #7ec8f0 !important; background: none !important; display: inline !important }
        .bannerslider .captionheader .herolede {
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            font-size: 1.05rem !important; line-height: 1.6 !important;
            color: rgba(255,255,255,.78) !important;
            max-width: 720px !important; margin: 24px auto 0 !important;
            font-weight: 400 !important;
        }

        /* ---------- AT A GLANCE / sections ---------- */
        .glancepart { padding: 100px 0 80px !important; background: #fff !important }
        .glancepart .container { max-width: 1080px !important }
        .glancegrid { display: grid !important; grid-template-columns: 1fr 1fr !important; gap: 56px !important; align-items: start !important }
        .glanceblock h2 {
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            font-size: clamp(1.5rem, 2.6vw, 1.9rem) !important;
            font-weight: 700 !important; letter-spacing: -.03em !important;
            color: #1d1d1f !important; line-height: 1.25 !important; margin-bottom: 14px !important;
        }
        .glanceblock h2 .eyebrow {
            display: block !important;
            font-size: .72rem !important; font-weight: 600 !important;
            letter-spacing: .12em !important; text-transform: uppercase !important;
            color: #0071e3 !important; margin-bottom: 12px !important;
        }
        .glanceblock p { font-family: 'Plus Jakarta Sans', sans-serif !important; color: #6e6e73 !important; font-size: .98rem !important; line-height: 1.7 !important }
        .glanceblock .label {
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            font-size: .72rem !important; font-weight: 600 !important;
            letter-spacing: .12em !important; text-transform: uppercase !important;
            color: #0071e3 !important; display: block !important;
            margin: 22px 0 8px !important;
        }
        .benefitlist { list-style: none !important; padding: 0 !important; margin: 8px 0 0 !important }
        .benefitlist li {
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            color: #1d1d1f !important; font-size: .94rem !important; line-height: 1.55 !important;
            padding: 14px 0 14px 32px !important; position: relative !important;
            border-bottom: 1px solid #f0f0f0 !important;
        }
        .benefitlist li:last-child { border-bottom: none !important }
        .benefitlist li::before {
            content: '' !important; position: absolute !important;
            left: 4px !important; top: 20px !important;
            width: 14px !important; height: 14px !important; border-radius: 50% !important;
            background: rgba(0,113,227,.12) !important;
        }
        .benefitlist li::after {
            content: '' !important; position: absolute !important;
            left: 8px !important; top: 25px !important;
            width: 6px !important; height: 6px !important; border-radius: 50% !important;
            background: #0071e3 !important;
        }

        /* ---------- Long-form content blocks ---------- */
        .blockpart { padding: 80px 0 !important; background: #f5f5f7 !important }
        .blockpart.alt { background: #fff !important }
        .blockpart .container { max-width: 1080px !important }
        .blockpart .blockrow { display: grid !important; grid-template-columns: 280px 1fr !important; gap: 56px !important; align-items: start !important }
        .blockpart h3 {
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            font-size: clamp(1.4rem, 2.4vw, 1.8rem) !important;
            font-weight: 700 !important; letter-spacing: -.02em !important;
            color: #1d1d1f !important; margin-bottom: 14px !important; line-height: 1.2 !important;
        }
        .blockpart h3 .eyebrow {
            display: block !important;
            font-size: .68rem !important; font-weight: 600 !important;
            letter-spacing: .14em !important; text-transform: uppercase !important;
            color: #0071e3 !important; margin-bottom: 14px !important;
        }
        .blockpart p {
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            color: #6e6e73 !important; font-size: 1rem !important; line-height: 1.75 !important;
            margin-bottom: 16px !important;
        }
        .blockpart ul.steplist {
            list-style: none !important; padding: 0 !important; margin: 16px 0 0 !important;
            display: grid !important; grid-template-columns: 1fr 1fr !important; gap: 14px !important;
        }
        .blockpart ul.steplist li {
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            color: #1d1d1f !important; font-size: .92rem !important; line-height: 1.55 !important;
            padding: 18px 20px !important; background: #fff !important;
            border: 1px solid #e8e8ed !important; border-radius: 12px !important;
            position: relative !important;
        }
        .blockpart.alt ul.steplist li { background: #f5f5f7 !important; border-color: #ececf1 !important }

        /* ---------- Pull quote ---------- */
        .quotepart { padding: 100px 0 !important; background: #fff !important }
        .quotepart .container { max-width: 880px !important; text-align: center !important }
        .quotepart blockquote {
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            font-size: clamp(1.25rem, 2.4vw, 1.7rem) !important;
            font-weight: 500 !important; line-height: 1.45 !important;
            letter-spacing: -.01em !important; color: #1d1d1f !important;
            margin: 0 !important; padding: 0 !important; border: none !important;
        }
        .quotepart blockquote::before { content: '\201C' !important; font-size: 4rem !important; line-height: 0 !important; vertical-align: -.4em !important; color: #0071e3 !important; margin-right: 6px !important }
        .quotepart blockquote::after { content: '\201D' !important; font-size: 4rem !important; line-height: 0 !important; vertical-align: -.4em !important; color: #0071e3 !important; margin-left: 6px !important }
        .quotepart .qauthor {
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            font-size: .82rem !important; font-weight: 600 !important;
            letter-spacing: .12em !important; text-transform: uppercase !important;
            color: #86868b !important; margin-top: 28px !important;
        }

        /* ---------- More case studies grid ---------- */
        .morecases { padding: 100px 0 80px !important; background: #f5f5f7 !important }
        .morecases .container { max-width: 1080px !important }
        .morecases .wemake {
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            font-size: clamp(1.8rem, 3.2vw, 2.5rem) !important;
            font-weight: 700 !important; letter-spacing: -.03em !important;
            color: #1d1d1f !important; margin-bottom: 8px !important;
        }
        .morecases p.lede { font-family: 'Plus Jakarta Sans', sans-serif !important; color: #86868b !important; font-size: 1rem !important; margin-bottom: 48px !important }
        .maincontainer { display: grid !important; grid-template-columns: repeat(3, 1fr) !important; gap: 20px !important }
        .maincontainer figure {
            margin: 0 !important; border-radius: 14px !important; overflow: hidden !important;
            background: #fff !important; border: 1px solid #e8e8ed !important; box-shadow: none !important;
            transition: border-color .25s, box-shadow .35s ease, transform .35s ease !important;
            display: flex !important; flex-direction: column !important; cursor: pointer !important;
        }
        .maincontainer figure:hover { transform: translateY(-3px) !important; border-color: #d2d2d7 !important; box-shadow: 0 4px 12px rgba(0,0,0,.04), 0 12px 32px rgba(0,0,0,.05) !important }
        .maincontainer .imgseccont { height: 200px !important; overflow: hidden !important }
        .maincontainer .imgseccont img { width: 100% !important; height: 100% !important; object-fit: cover !important; transition: transform .6s cubic-bezier(.25,.1,.25,1) !important }
        .maincontainer figure:hover .imgseccont img { transform: scale(1.03) !important }
        .maincontainer figcaption { padding: 22px 24px 24px !important; flex: 1 !important; display: flex !important; flex-direction: column !important }
        .maincontainer figcaption a.cases {
            text-decoration: none !important;
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            font-weight: 500 !important; color: #0071e3 !important;
            font-size: .82rem !important; display: flex !important;
            flex-direction: column !important; flex: 1 !important;
        }
        .maincontainer figcaption a.cases:hover { color: #0077ed !important }
        .maincontainer figcaption .eyebrow {
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            font-size: .68rem !important; font-weight: 600 !important;
            letter-spacing: .12em !important; text-transform: uppercase !important;
            color: #86868b !important; margin-bottom: 8px !important;
        }
        .maincontainer figcaption .cases p {
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            color: #1d1d1f !important; font-size: .9rem !important; line-height: 1.5 !important;
            margin-bottom: 14px !important; flex: 1 !important; font-weight: 500 !important;
        }

        /* ---------- Contact ---------- */
        .contactpart { padding: 100px 0 !important; background: #fff !important }
        .contactpart .container { max-width: 1080px !important }
        .contactbond {
            background: #fff !important; border-radius: 20px !important;
            border: 1px solid #e8e8ed !important; padding: 48px !important;
            box-shadow: 0 2px 8px rgba(0,0,0,.04), 0 12px 48px rgba(0,0,0,.06) !important;
        }
        .cloudcontactheading {
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            font-size: clamp(1.8rem, 3.2vw, 2.5rem) !important;
            font-weight: 700 !important; letter-spacing: -.03em !important;
            color: #1d1d1f !important; margin-bottom: 40px !important;
        }
        .cloudcontactheading span { color: #0071e3 !important }
        .cloudcontactimg { overflow: hidden !important; border-radius: 16px !important; height: 100% !important }
        .cloudcontactimg img { width: 100% !important; height: 100% !important; object-fit: cover !important; display: block !important; border-radius: 16px !important }
        .allcontactform label { font-family: 'Plus Jakarta Sans', sans-serif !important; font-weight: 500 !important; font-size: .82rem !important; color: #1d1d1f !important; margin-bottom: 6px !important }
        .allcontactform .form-control {
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            border: 1px solid #e8e8ed !important; border-radius: 10px !important;
            padding: 12px 16px !important; font-size: .9rem !important; color: #1d1d1f !important;
            transition: border-color .2s !important; box-shadow: none !important;
        }
        .allcontactform .form-control:focus { border-color: #0071e3 !important; box-shadow: 0 0 0 3px rgba(0,113,227,.1) !important }
        .allcontactform textarea.form-control { min-height: 120px !important; resize: vertical !important }
        .allcontactform .form-group { margin-bottom: 20px !important }
        .allcontactform .btnpart .btn-primary {
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            background: #0071e3 !important; border: none !important;
            border-radius: 980px !important; font-weight: 600 !important;
            font-size: 15px !important; color: #fff !important;
            transition: background .2s !important; box-shadow: none !important;
        }
        .allcontactform .btnpart .btn-primary:hover { background: #0077ed !important }

        /* ---------- Footer ---------- */
        body main footer.darkfooter, footer.darkfooter { background: #111113 !important; padding: 0 !important; overflow: hidden !important }
        footer.darkfooter > .container { padding-top: 64px !important; padding-bottom: 0 !important }
        footer.darkfooter > .container > .row { padding-bottom: 40px !important; border-bottom: 1px solid rgba(255,255,255,.07) !important }
        footer.darkfooter h6 {
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            font-weight: 600 !important; font-size: .68rem !important;
            letter-spacing: .1em !important; text-transform: uppercase !important;
            color: rgba(255,255,255,.35) !important; margin-bottom: 20px !important;
        }
        footer.darkfooter ul.fotnab { list-style: none !important; padding: 0 !important; margin: 0 !important }
        footer.darkfooter ul.fotnab li { margin-bottom: 10px !important }
        footer.darkfooter ul.fotnab li a {
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            color: rgba(255,255,255,.6) !important; font-size: .86rem !important;
            text-decoration: none !important; transition: color .15s !important; font-weight: 400 !important;
        }
        footer.darkfooter ul.fotnab li a:hover { color: #fff !important }
        footer.darkfooter div[style*="display:flex"] { gap: 16px !important; padding-top: 24px !important; align-items: center !important }
        footer.darkfooter a img { opacity: .5 !important; transition: opacity .15s !important; filter: none !important; vertical-align: middle !important }
        footer.darkfooter a:hover img { opacity: .85 !important; filter: none !important; transform: none !important }
        footer.darkfooter .fotcopy, .fotcopy { padding: 20px 0 !important; margin-top: 0 !important }
        footer.darkfooter .fotcopy p, .fotcopy p { font-family: 'Plus Jakarta Sans', sans-serif !important; color: rgba(255,255,255,.2) !important; font-size: .72rem !important; margin: 0 !important }

        /* ---------- Scroll reveal ---------- */
        .sr { opacity: 0; transform: translateY(48px); transition: opacity .8s cubic-bezier(.16,1,.3,1), transform .8s cubic-bezier(.16,1,.3,1) }
        .sr.v { opacity: 1 !important; transform: none !important }
        .sr-up { transform: translateY(48px) }
        .sr-left { transform: translateX(-40px) }
        .sr-right { transform: translateX(40px) }
        .sr-scale { transform: scale(.92); transform-origin: center }
        .sr-d1 { transition-delay: .08s }
        .sr-d2 { transition-delay: .16s }
        .sr-d3 { transition-delay: .24s }
        .sr-d4 { transition-delay: .32s }
        .sr-d5 { transition-delay: .4s }

        /* ---------- Responsive ---------- */
        @media(max-width:992px) {
            body > main { padding-top: 66px !important }
            .glancegrid { grid-template-columns: 1fr !important; gap: 32px !important }
            .blockpart .blockrow { grid-template-columns: 1fr !important; gap: 18px !important }
            .blockpart ul.steplist { grid-template-columns: 1fr !important }
            .maincontainer { grid-template-columns: repeat(2, 1fr) !important }
            .glancepart { padding: 60px 0 48px !important }
            .blockpart { padding: 48px 0 !important }
            .quotepart { padding: 60px 0 !important }
            .morecases { padding: 60px 0 48px !important }
            .contactpart { padding: 60px 0 !important }
            .contactbond { padding: 32px !important }
        }
        @media(max-width:640px) {
            .bannerslider.oneuspage { min-height: 48vh !important }
            .bannerslider .captionheader h1 { font-size: 1.7rem !important; line-height: 1.15 !important }
            .bannerslider .captionheader .herolede { font-size: .92rem !important }
            .maincontainer { grid-template-columns: 1fr !important; gap: 16px !important }
            .maincontainer .imgseccont { height: 180px !important }
            .maincontainer figcaption { padding: 18px 18px 20px !important }
            .contactbond { padding: 24px 20px !important; border-radius: 14px !important }
            .homenav .nav .nav-item .nav-link { font-size: 13px !important; padding: 6px 10px !important }
            #mainlogo img.logo1 { height: 24px !important }
            #mainlogo img.logo2 { height: 18px !important }
            .darkfooter > .container { padding-top: 40px !important }
        }
        @media(max-width:400px) {
            .bannerslider .captionheader h1 { font-size: 1.4rem !important }
            .bannerslider.oneuspage { min-height: 42vh !important }
        }
    </style>
</head>
"""

HEADER = """<body>
    <main>
        <div class="headercls">
            <div class="container">
                <div class="row">
                    <nav class="navbar navbar-expand-lg homenav">
                        <div class="container-fluid">
                            <a href="index.html" class="d-flex align-items-center mb-3 mb-md-0 me-md-auto text-dark text-decoration-none">
                                <div id="mainlogo" style="display:flex;align-items: center; gap: 10px;">
                                    <img class="logo1" src="web/images/mainlogo.svg" alt="DIS Services Inc Logo">
                                    <span style="width:1px; height:40px; background:#3482AD;"></span>
                                    <img class="logo2" src="web/images/micro.png" alt="Microsoft Partner">
                                </div>
                            </a>
                            <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                                data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent"
                                aria-expanded="false" aria-label="Toggle navigation">
                                <span class="navbar-toggler-icon"></span>
                            </button>
                            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                                <ul class="nav nav-pills d-flex align-items-center">
                                    <li class="nav-item"><a href="we-are.html" class="nav-link">We Are</a></li>
                                    <li class="nav-item"><a href="our-services.html" class="nav-link">Services</a></li>
                                    <li class="nav-item"><a href="data-world.html" class="nav-link">Data World</a></li>
                                    <li class="nav-item"><a href="we-care.html" class="nav-link">We Care</a></li>
                                    <li class="nav-item"><a href="cloud-providers.html" class="nav-link">Cloud Providers</a></li>
                                    <li class="nav-item"><a href="contact-us.html" class="nav-link">Contact Us</a></li>
                                    <li class="nav-item"><a href="privacy-policy.html" class="nav-link">Privacy Policy</a></li>
                                    <li class="nav-item"><a href="join-us.html" class="nav-link">Join Us</a></li>
                                </ul>
                            </div>
                        </div>
                    </nav>
                </div>
            </div>
        </div>
"""

FOOTER = """        <footer class="darkfooter">
            <div class="container">
                <div class="row">
                    <div class="col-lg-4 col-md-4 col-sm-6 col-6">
                        <h6>Company</h6>
                        <ul class="fotnab">
                            <li><a href="index.html">About</a></li>
                            <li><a href="our-services.html">Services</a></li>
                            <li><a href="privacy-policy.html">Privacy Policy</a></li>
                        </ul>
                    </div>
                    <div class="col-lg-4 col-md-4 col-sm-6 col-6">
                        <h6>Help</h6>
                        <ul class="fotnab">
                            <li><a href="contact-us.html">Contact Us</a></li>
                            <li><a href="join-us.html">Join Us</a></li>
                        </ul>
                    </div>
                    <div class="col-lg-4 col-md-4 col-sm-6 col-6">
                        <h6>Other Links</h6>
                        <ul class="fotnab">
                            <li><a href="data-world.html">Data World</a></li>
                            <li><a href="we-care.html">We Care</a></li>
                            <li><a href="cloud-providers.html">Cloud Provider</a></li>
                        </ul>
                    </div>
                    <div style="display:flex">
                        <a href="https://www.instagram.com/dataintegrityservices/">
                            <img style="width:30px; height:30px" src="web/images/insta.png" alt="Instagram">
                        </a>
                        <a href="https://www.facebook.com/profile.php?id=61556158206869">
                            <img style="width:55px; height:30px" src="web/images/fb.svg" alt="Facebook">
                        </a>
                        <a href="https://www.linkedin.com/company/data-integrity-services-us/">
                            <img style="width:38px; height:35px" src="web/images/linked-in.png" alt="LinkedIn">
                        </a>
                    </div>
                </div>
                <div class="container fotcopy" style="margin-top: 10px;">
                    <div class="row">
                        <div class="col-lg-6 col-md-6 col-sm-12 col-12">
                            <p>&copy; Copyright 2024, All Rights Reserved by DIS</p>
                        </div>
                        <div class="col-lg-6 col-md-6 col-sm-12 col-12"></div>
                    </div>
                </div>
            </div>
        </footer>

    </main>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>
    <script>
        window.addEventListener('scroll', function () {
            var h = document.querySelector('.headercls');
            if (h) h.classList.toggle('scrolled', window.scrollY > 20);
        }, { passive: true });

        document.addEventListener('DOMContentLoaded', function () {
            var bh = document.querySelector('.bannerslider .captionheader');
            if (bh) bh.classList.add('sr');
            document.querySelectorAll('.glanceblock').forEach(function (el, i) {
                el.classList.add('sr', i % 2 === 0 ? 'sr-left' : 'sr-right');
            });
            document.querySelectorAll('.blockpart .blockrow').forEach(function (el, i) {
                el.classList.add('sr');
            });
            var qp = document.querySelector('.quotepart blockquote');
            if (qp) qp.classList.add('sr', 'sr-scale');
            var csh = document.querySelector('.morecases .wemake');
            if (csh) csh.classList.add('sr');
            document.querySelectorAll('.maincontainer figure').forEach(function (el, i) {
                el.classList.add('sr');
                el.classList.add('sr-d' + (i % 3 + 1));
            });
            var cb = document.querySelector('.contactbond');
            if (cb) cb.classList.add('sr', 'sr-scale');
            document.querySelectorAll('.darkfooter .col-lg-4,.darkfooter .col-md-4').forEach(function (el, i) {
                el.classList.add('sr');
                el.classList.add('sr-d' + (i + 1));
            });
            var o = new IntersectionObserver(function (entries) {
                entries.forEach(function (e) {
                    if (e.isIntersecting) { e.target.classList.add('v'); o.unobserve(e.target); }
                });
            }, { threshold: 0.08, rootMargin: '0px 0px -50px 0px' });
            document.querySelectorAll('.sr').forEach(function (el) { o.observe(el); });
        });
    </script>
</body>
</html>
"""


def html_escape(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def render_benefits(items: list[str]) -> str:
    return "\n".join(f"                            <li>{html_escape(i)}</li>" for i in items)


def render_steps(items: list[str]) -> str:
    return "\n".join(f"                            <li>{html_escape(i)}</li>" for i in items)


def render_more_cases(current_slug: str) -> str:
    cards = []
    for c in CASES:
        if c["slug"] == current_slug:
            continue
        cards.append(f"""                    <figure>
                        <div class="imgseccont">
                            <a href="{c['filename']}">
                                <img src="{c['image']}" alt="{html_escape(c['headline'])}">
                            </a>
                        </div>
                        <figcaption>
                            <a href="{c['filename']}" class="cases">
                                <span class="eyebrow">{html_escape(c['industry'])}</span>
                                <p>{html_escape(c['headline'])}</p>
                                Read case study
                            </a>
                        </figcaption>
                    </figure>""")
    return "\n".join(cards)


def render_page(case: dict) -> str:
    hero_image = case.get("hero_image", case["image"])
    # OG/Twitter meta uses the original (live-server) image since the _hq
    # variant only exists in the local checkout.
    head = (HEAD_AND_STYLE
        .replace("__PAGE_TITLE__", html_escape(case["page_title"]))
        .replace("__META_DESCRIPTION__", html_escape(case["meta_description"]))
        .replace("__FILENAME__", case["filename"])
        .replace("__IMAGE__", case["image"]))

    body = f"""
        <div class="bannerslider oneuspage">
            <div class="captionheader shadownone lefttextcap nohome">
                <div class="container">
                    <span class="eyebrow">Case Study &middot; {html_escape(case['industry'])}</span>
                    <h1>{html_escape(case['hero_main'])} <span>{html_escape(case['hero_accent'])}</span></h1>
                    <p class="herolede">{html_escape(case['summary'])}</p>
                </div>
            </div>
            <img width="100%" height="100%" src="{hero_image}" alt="{html_escape(case['headline'])}">
        </div>

        <section class="glancepart">
            <div class="container">
                <div class="glancegrid">
                    <div class="glanceblock">
                        <h2><span class="eyebrow">At a glance</span>{html_escape(case['headline'])}</h2>
                        <p>{html_escape(case['challenge_short'])}</p>
                    </div>
                    <div class="glanceblock">
                        <span class="label">Outcomes</span>
                        <ul class="benefitlist">
{render_benefits(case['benefits'])}
                        </ul>
                    </div>
                </div>
            </div>
        </section>

        <section class="blockpart">
            <div class="container">
                <div class="blockrow">
                    <div>
                        <h3><span class="eyebrow">The Challenge</span>What stood in the way</h3>
                    </div>
                    <div>
                        <p>{html_escape(case['challenge_body'])}</p>
                    </div>
                </div>
            </div>
        </section>

        <section class="blockpart alt">
            <div class="container">
                <div class="blockrow">
                    <div>
                        <h3><span class="eyebrow">Our Approach</span>How DIS got to work</h3>
                    </div>
                    <div>
                        <p>{html_escape(case['approach_lead'])}</p>
                        <ul class="steplist">
{render_steps(case['approach_steps'])}
                        </ul>
                    </div>
                </div>
            </div>
        </section>

        <section class="quotepart">
            <div class="container">
                <blockquote>{html_escape(case['quote'])}</blockquote>
                <div class="qauthor">DIS Services Inc &middot; {html_escape(case['industry'])}</div>
            </div>
        </section>

        <section class="blockpart">
            <div class="container">
                <div class="blockrow">
                    <div>
                        <h3><span class="eyebrow">Our Solution</span>The result we delivered</h3>
                    </div>
                    <div>
                        <p>{html_escape(case['solution_lead'])}</p>
                        <ul class="steplist">
{render_steps(case['solution_results'])}
                        </ul>
                    </div>
                </div>
            </div>
        </section>

        <section class="morecases">
            <div class="container">
                <div class="text-center">
                    <h4 class="wemake">More case studies</h4>
                    <p class="lede">Bringing innovation across all industries</p>
                </div>
                <div class="maincontainer">
{render_more_cases(case['slug'])}
                </div>
            </div>
        </section>

        <section id="contactexp" class="contactpart">
            <div class="container">
                <div class="contactbond">
                    <div class="row">
                        <div class="col-lg-12 text-center">
                            <h4 class="cloudcontactheading">Talk to an <span>Expert</span></h4>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-lg-5">
                            <div class="cloudcontactimg">
                                <img src="web/images/cloudcontact-img.jpg" alt="Talk to a cloud expert">
                            </div>
                        </div>
                        <div class="col-lg-7">
                            <form action="contact/store" method="post">
                                <input type="hidden" name="_token" value="" autocomplete="off">
                                <div class="allcontactform">
                                    <div class="row">
                                        <div class="col-lg-12">
                                            <div class="form-group">
                                                <label>Full Name</label>
                                                <input type="text" name="full_name" placeholder="First Name" class="form-control" required>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col-lg-6">
                                            <div class="form-group">
                                                <label>Email</label>
                                                <input type="email" name="email" placeholder="demo@yopmail.com" class="form-control" required>
                                            </div>
                                        </div>
                                        <div class="col-lg-6">
                                            <div class="form-group">
                                                <label>Phone Number</label>
                                                <input type="number" name="phone_number" min="0" placeholder="Enter Phone Number" class="form-control" required>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col-lg-12">
                                            <div class="form-group">
                                                <label>Message</label>
                                                <textarea class="form-control" name="message" placeholder="Write your message.." required></textarea>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col-lg-12">
                                            <div class="form-group btnpart">
                                                <input type="submit" value="Send Message" class="btn btn-primary">
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </section>
"""
    return head + HEADER + body + FOOTER


def main() -> int:
    for case in CASES:
        path = ROOT / case["filename"]
        path.write_text(render_page(case), encoding="utf-8")
        print(f"wrote {case['filename']} ({path.stat().st_size:,} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
