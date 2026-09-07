#!/usr/bin/env python3
"""Generate expanded knowledge library: projects, articles, SVG covers."""
from pathlib import Path
import html as H

ROOT = Path(__file__).resolve().parents[1]
PROJECTS = ROOT / "projects"
ARTICLES_DIR = ROOT / "articles"
COVERS = ROOT / "assets" / "covers"
DIAGRAMS = ROOT / "assets" / "diagrams"

NOTE = (
    "Knowledge / portfolio case study only. Not employment history, "
    "not a named client engagement, and not a certification claim."
)

NEW_PROJECTS = [
    {
        "slug": "fixed-assets-lifecycle",
        "num": "07",
        "title": "Fixed Assets Lifecycle Design",
        "tag": "Assets · Depreciation",
        "lede": "A complete fixed-asset process blueprint — from capitalization thresholds and category design to depreciation books, transfers, retirements, and period-end asset reporting.",
        "next": "cash-management-bank-rec.html",
        "next_label": "Cash Management →",
        "prev": "arcs-narrative-reporting.html",
        "modules": ["Fixed Assets", "GL", "Payables", "OTBI"],
        "sections": [
            ("objective", "Objective", "Design a Fixed Assets foundation that finance and operations can run every period without suspense buildup, missed capitalizations, or unclear retirement ownership."),
            ("context", "Context", "Multi-entity organizations often struggle with inconsistent asset categories, unclear CIP rules, and depreciation books that do not match reporting needs. This case study models a clean lifecycle."),
            ("scope", "Scope", "In scope: capitalization policy checkpoints, category & book design, addition/transfer/retirement flows, depreciation calendars, and asset reporting pack. Out of scope: detailed tax depreciation engine configuration for every jurisdiction."),
            ("approach", "Approach", "Workshop capitalization thresholds → map categories to GL accounts → define books & methods → design CIP-to-asset conversion → document transfers/retirements → build period checklist → validate with sample assets."),
            ("walkthrough", "Walkthrough", "1) Capture a CIP invoice and track WIP. 2) Capitalize to asset with correct category. 3) Run depreciation for two periods. 4) Transfer between cost centers. 5) Partially retire and confirm gain/loss treatment. 6) Extract asset rollforward report."),
            ("controls", "Controls", "No capitalization below policy without exception log; category changes require finance approval; depreciation cannot close until unposted assets are cleared; retirements require supporting evidence."),
            ("deliverables", "Deliverables", "Asset category matrix, CIP conversion checklist, depreciation calendar notes, UAT asset scenarios, OTBI rollforward starter pack, decision log."),
            ("outcomes", "Outcomes", "Shows end-to-end Fixed Assets thinking — process, configuration intent, controls, and reporting — ready for workshop or interview deep-dive."),
        ],
        "phases": [
            ("01", "Policy & threshold discovery", "Agree capitalization rules, useful life defaults, and CIP treatment."),
            ("02", "Category & account mapping", "Link categories to natural accounts and cost centers."),
            ("03", "Book & calendar design", "Corporate vs secondary books, methods, and calendars."),
            ("04", "Lifecycle process design", "Additions, adjustments, transfers, retirements."),
            ("05", "Close & reporting pack", "Period checklist + rollforward extracts."),
        ],
        "decisions": [
            ("Single corporate book first", "Stabilize corporate reporting before expanding tax books."),
            ("CIP as controlled staging", "Keep CIP visible and gated before capitalization."),
            ("Category ownership", "Finance owns categories; operations request via change log."),
        ],
    },
    {
        "slug": "cash-management-bank-rec",
        "num": "08",
        "title": "Cash Management & Bank Reconciliation Design",
        "tag": "Cash · Bank Rec",
        "lede": "Bank account structure, statement import patterns, reconciliation matching rules, and cash visibility for controllers — designed so daily cash and month-end reconcile without chaos.",
        "next": "tax-config-alignment.html",
        "next_label": "Tax Alignment →",
        "prev": "fixed-assets-lifecycle.html",
        "modules": ["Cash Management", "GL", "AR", "AP", "OTBI"],
        "sections": [
            ("objective", "Objective", "Build a cash and bank reconciliation design that gives daily cash clarity and a controlled month-end bank-to-book close."),
            ("context", "Context", "Finance teams often lose time to unmatched statements, unclear bank account ownership, and cash positions that do not agree to GL."),
            ("scope", "Scope", "Bank account model, statement intake, auto-match vs manual match, outstanding item aging, and cash position reporting. Out of scope: treasury deal management."),
            ("approach", "Approach", "Map legal entities to bank accounts → define GL cash accounts → design statement import cadence → set matching tolerance → build exception queues → publish daily cash view."),
            ("walkthrough", "Walkthrough", "Import a sample statement → auto-match receipts/payments → age unmatched items → clear a manual match → lock period bank rec → extract cash by entity."),
            ("controls", "Controls", "Every bank account has an owner; unmatched items older than SLA escalate; no period close with material unmatched balance without sign-off."),
            ("deliverables", "Deliverables", "Bank account matrix, matching rule sheet, exception playbook, daily cash dashboard sketch, UAT statement pack."),
            ("outcomes", "Outcomes", "Demonstrates practical Cash Management design that connects operations, GL, and controller reporting."),
        ],
        "phases": [
            ("01", "Account & ownership map", "Entity, bank, GL account, and owner."),
            ("02", "Statement design", "Formats, cadence, and import validation."),
            ("03", "Matching rules", "Auto vs manual, tolerances, references."),
            ("04", "Exception workflow", "Aging, escalation, and clearance."),
            ("05", "Cash reporting", "Daily position + month-end pack."),
        ],
        "decisions": [
            ("One GL cash account per bank account where possible", "Simplifies reconciliation ownership."),
            ("Match on reference + amount first", "Reduce false positives from amount-only matching."),
            ("Separate operational cash view from period lock", "Daily ops can move while close remains controlled."),
        ],
    },
    {
        "slug": "tax-config-alignment",
        "num": "09",
        "title": "Tax Configuration Alignment Blueprint",
        "tag": "Tax · Controls",
        "lede": "A practical alignment model for tax regimes, tax codes, invoice tax determination checkpoints, and reporting readiness — so AP/AR tax behavior stays consistent with finance policy.",
        "next": "otbi-smartview-pack.html",
        "next_label": "OTBI / Smart View →",
        "prev": "cash-management-bank-rec.html",
        "modules": ["Tax", "AP", "AR", "GL", "OTBI"],
        "sections": [
            ("objective", "Objective", "Align tax configuration thinking with invoice flows so tax determination is explainable, testable, and reportable."),
            ("context", "Context", "Tax issues often appear as invoice exceptions, unexpected tax amounts, or reports that cannot reconcile to GL."),
            ("scope", "Scope", "Regime/code inventory, AP/AR tax checkpoints, exemption handling notes, and tax reporting extracts. Not a full multi-country legal opinion."),
            ("approach", "Approach", "Inventory tax needs → map codes to invoice events → define exemption evidence → design exception handling → validate with invoice scenarios → build tax extract checklist."),
            ("walkthrough", "Walkthrough", "Create taxable AP invoice → create exempt AP invoice with evidence → AR invoice with tax → reverse and credit → reconcile tax to GL control account."),
            ("controls", "Controls", "Exemption requires documented evidence; tax code changes logged; tax control accounts reviewed every close."),
            ("deliverables", "Deliverables", "Tax code matrix, invoice scenario library, exception handling guide, tax-to-GL reconciliation sheet."),
            ("outcomes", "Outcomes", "Shows tax configuration as process + control design, not only setup screens."),
        ],
        "phases": [
            ("01", "Tax inventory", "Regimes, codes, and reporting needs."),
            ("02", "Invoice checkpoints", "Where tax is determined in AP/AR."),
            ("03", "Exemption model", "Evidence and approval path."),
            ("04", "Exception design", "Wrong tax, missing tax, overrides."),
            ("05", "Reporting & recon", "Extracts and control accounts."),
        ],
        "decisions": [
            ("Start with high-volume domestic scenarios", "Stabilize core before edge jurisdictions."),
            ("Treat overrides as controlled exceptions", "Never silent tax changes."),
            ("Reconcile tax every close", "Detect drift early."),
        ],
    },
    {
        "slug": "otbi-smartview-pack",
        "num": "10",
        "title": "OTBI & Smart View Reporting Pack",
        "tag": "OTBI · Smart View",
        "lede": "A controller-ready reporting pack design — trial balance, account analysis, AP/AR aging, close dashboards, and Smart View retrieval patterns that support decisions, not just extracts.",
        "next": "subledger-accounting-design.html",
        "next_label": "Subledger Accounting →",
        "prev": "tax-config-alignment.html",
        "modules": ["OTBI", "Smart View", "GL", "AP", "AR"],
        "sections": [
            ("objective", "Objective", "Design a finance reporting pack that answers close and operational questions quickly with consistent definitions."),
            ("context", "Context", "Teams often rebuild spreadsheets every month because reports are inconsistent, slow, or not trusted."),
            ("scope", "Scope", "Core GL/AP/AR report catalog, prompt standards, Smart View layout notes, and close dashboard wireframes."),
            ("approach", "Approach", "List decisions by role → map to reports → define prompts & filters → design folder structure → document refresh cadence → UAT with sample periods."),
            ("walkthrough", "Walkthrough", "Run TB by ledger → drill account analysis → pull AP aging → refresh Smart View close pack → compare to prior period."),
            ("controls", "Controls", "Report definitions owned by finance systems; ad-hoc extracts labeled as non-official; period prompts mandatory."),
            ("deliverables", "Deliverables", "Report catalog, prompt standard, Smart View pack outline, dashboard wireframes, UAT checklist."),
            ("outcomes", "Outcomes", "Demonstrates reporting design that supports close and leadership conversations."),
        ],
        "phases": [
            ("01", "Audience & decisions", "Controller, AP, AR, FP&A needs."),
            ("02", "Catalog design", "Official vs working reports."),
            ("03", "Prompt standards", "Ledger, period, entity filters."),
            ("04", "Smart View pack", "Close workbook structure."),
            ("05", "UAT & handover", "Validate and document owners."),
        ],
        "decisions": [
            ("One official TB definition", "Stop version wars."),
            ("Smart View for repeating close packs", "OTBI for operational queries."),
            ("Name reports by decision, not module only", "Improve findability."),
        ],
    },
    {
        "slug": "subledger-accounting-design",
        "num": "11",
        "title": "Subledger Accounting Rules Design",
        "tag": "SLA · GL",
        "lede": "How accounting events from AP, AR, and Assets should land cleanly in GL — event classes, journal line rules, description standards, and reconciliation checkpoints.",
        "next": "multi-ledger-currency.html",
        "next_label": "Multi-Ledger →",
        "prev": "otbi-smartview-pack.html",
        "modules": ["Subledger Accounting", "AP", "AR", "Assets", "GL"],
        "sections": [
            ("objective", "Objective", "Design SLA thinking so subledger activity creates clear, auditable GL journals with minimal suspense."),
            ("context", "Context", "When SLA rules are vague, journals are hard to explain and reconciliations fail."),
            ("scope", "Scope", "Event inventory, account derivation intent, journal descriptions, and recon points. Not every seeded rule customization."),
            ("approach", "Approach", "List key events → define debit/credit intent → map sources to accounts → standardize descriptions → test create accounting → reconcile to TB."),
            ("walkthrough", "Walkthrough", "Post AP invoice → create accounting → review journal → transfer to GL → reconcile subledger to GL."),
            ("controls", "Controls", "Unaccounted transactions tracked daily; suspense accounts aged; rule changes logged."),
            ("deliverables", "Deliverables", "Event-to-account matrix, description standard, recon checklist, UAT event pack."),
            ("outcomes", "Outcomes", "Shows systems thinking between subledgers and GL."),
        ],
        "phases": [
            ("01", "Event inventory", "AP/AR/Assets key events."),
            ("02", "Account intent", "Natural account & CC logic."),
            ("03", "Description standard", "Searchable journal text."),
            ("04", "Create accounting tests", "Happy path + exceptions."),
            ("05", "Reconciliation rhythm", "Daily and period-end."),
        ],
        "decisions": [
            ("Prefer clear seeded patterns before heavy customization", "Reduce upgrade risk."),
            ("Descriptions must include business key", "Invoice/asset number in journal text."),
            ("Suspense is temporary only", "Age and clear every close."),
        ],
    },
    {
        "slug": "multi-ledger-currency",
        "num": "12",
        "title": "Multi-Ledger & Multi-Currency Blueprint",
        "tag": "Ledgers · Currency",
        "lede": "Primary/secondary ledger relationships, currency representation, revaluation checkpoints, and reporting views for multi-entity finance landscapes.",
        "next": "fusion-security-roles.html",
        "next_label": "Security Roles →",
        "prev": "subledger-accounting-design.html",
        "modules": ["GL", "Ledgers", "Currency", "OTBI"],
        "sections": [
            ("objective", "Objective", "Design ledger and currency structures that support statutory and management views without duplicate chaos."),
            ("context", "Context", "Growing organizations often add ledgers reactively, creating reporting confusion and close delays."),
            ("scope", "Scope", "Ledger set thinking, currency representation, revaluation timing, and management reporting alignment."),
            ("approach", "Approach", "Map legal entities → choose primary ledgers → decide secondary needs → define currencies → set revaluation cadence → validate TB by ledger."),
            ("walkthrough", "Walkthrough", "Post multi-currency journal → revalue → review unrealized gain/loss → report TB in ledger currency and reporting currency."),
            ("controls", "Controls", "Ledger ownership matrix; revaluation before close gate; FX rate source documented."),
            ("deliverables", "Deliverables", "Ledger matrix, currency matrix, revaluation checklist, sample TB views."),
            ("outcomes", "Outcomes", "Clear story for multi-ledger / multi-currency design interviews and workshops."),
        ],
        "phases": [
            ("01", "Entity & reporting needs", "Statutory vs management."),
            ("02", "Ledger model", "Primary/secondary choices."),
            ("03", "Currency model", "Entered, accounted, reporting."),
            ("04", "Revaluation design", "Timing and accounts."),
            ("05", "Reporting validation", "TB packs by ledger."),
        ],
        "decisions": [
            ("Do not create a ledger for every report request", "Use reporting tools where possible."),
            ("Document rate source once", "Avoid silent FX differences."),
            ("Revaluation is a close gate", "Not an optional afterthought."),
        ],
    },
    {
        "slug": "fusion-security-roles",
        "num": "13",
        "title": "Fusion Finance Security Roles Model",
        "tag": "Security · SoD",
        "lede": "A practical role design for finance users — job roles, duty separation, period close privileges, and access review rhythm that supports control without blocking work.",
        "next": "budget-control-encumbrance.html",
        "next_label": "Budget Control →",
        "prev": "multi-ledger-currency.html",
        "modules": ["Security Console", "GL", "AP", "AR"],
        "sections": [
            ("objective", "Objective", "Design a finance access model with clear separation of duties and usable day-to-day roles."),
            ("context", "Context", "Over-broad access creates audit risk; over-tight access creates workarounds."),
            ("scope", "Scope", "Role catalog for AP/AR/GL/close, SoD checkpoints, access request path, and quarterly review. Not a full IAM implementation."),
            ("approach", "Approach", "List personas → map duties → identify SoD conflicts → propose role bundles → define request/approval → test with sample users."),
            ("walkthrough", "Walkthrough", "AP clerk posts invoice but cannot approve → approver cannot create supplier bank change → closer opens/closes periods → review access extract."),
            ("controls", "Controls", "No combined create+approve for high-risk duties; privileged access time-bound; quarterly access attestation."),
            ("deliverables", "Deliverables", "Persona-role matrix, SoD conflict list, access request form, UAT access scenarios."),
            ("outcomes", "Outcomes", "Shows control-aware Fusion finance security thinking."),
        ],
        "phases": [
            ("01", "Persona map", "Clerk, approver, accountant, closer."),
            ("02", "Duty analysis", "Create, approve, post, close."),
            ("03", "SoD matrix", "Conflicts and mitigations."),
            ("04", "Role bundles", "Usable packaged access."),
            ("05", "Review rhythm", "Quarterly attestation."),
        ],
        "decisions": [
            ("Prefer fewer well-named roles", "Easier to govern."),
            ("Break glass access is temporary", "Always expire."),
            ("Close privileges are restricted", "Period status is sensitive."),
        ],
    },
    {
        "slug": "budget-control-encumbrance",
        "num": "14",
        "title": "Budget Control & Encumbrance Design",
        "tag": "Budget · Controls",
        "lede": "Budget control structures, reservation points in P2P, override governance, and reporting so spend stays visible before it becomes an invoice surprise.",
        "next": "lease-accounting-process.html",
        "next_label": "Lease Accounting →",
        "prev": "fusion-security-roles.html",
        "modules": ["Budgetary Control", "AP", "Purchasing", "GL"],
        "sections": [
            ("objective", "Objective", "Design budget control thinking that prevents overspend early while allowing controlled exceptions."),
            ("context", "Context", "Without reservations, finance discovers overspend at invoice time — too late."),
            ("scope", "Scope", "Control budget structure, reservation events, override path, and budget vs actual reporting."),
            ("approach", "Approach", "Define control segments → set reservation points → design override approvals → test PO/invoice paths → build budget variance pack."),
            ("walkthrough", "Walkthrough", "Create PO that reserves funds → increase PO → attempt over-budget PO → override with approval → invoice and release → report variance."),
            ("controls", "Controls", "Overrides require named approver; override log reviewed monthly; soft vs hard controls documented."),
            ("deliverables", "Deliverables", "Control matrix, override playbook, UAT scenarios, variance report outline."),
            ("outcomes", "Outcomes", "Connects purchasing behavior to financial control outcomes."),
        ],
        "phases": [
            ("01", "Control design", "What is controlled and at what grain."),
            ("02", "Reservation points", "Requisition/PO/invoice."),
            ("03", "Override governance", "Who can break the rule."),
            ("04", "UAT paths", "Pass, fail, override."),
            ("05", "Reporting", "Budget vs actual & override log."),
        ],
        "decisions": [
            ("Hard control on high-risk cost centers", "Soft elsewhere initially."),
            ("Overrides are visible", "Never silent."),
            ("Align budget segments to CoA", "Avoid mapping gymnastics."),
        ],
    },
    {
        "slug": "lease-accounting-process",
        "num": "15",
        "title": "Lease Accounting Process Design",
        "tag": "Leases · Process",
        "lede": "A process-first lease accounting blueprint — inventory, classification checkpoints, payment schedules, accounting event rhythm, and close disclosures readiness.",
        "next": "edm-dimension-governance.html",
        "next_label": "EDM Governance →",
        "prev": "budget-control-encumbrance.html",
        "modules": ["Lease Accounting", "GL", "Assets", "OTBI"],
        "sections": [
            ("objective", "Objective", "Design a lease process that finance can operate monthly with clear data ownership and accounting checkpoints."),
            ("context", "Context", "Lease accounting fails when contract data is incomplete or ownership between legal, procurement, and finance is unclear."),
            ("scope", "Scope", "Lease inventory model, data checklist, payment & accounting cadence, and disclosure pack notes. Not legal advice."),
            ("approach", "Approach", "Build lease register → define required fields → set classification checklist → design payment/accounting calendar → validate journals → prepare disclosure extracts."),
            ("walkthrough", "Walkthrough", "Add a sample lease → schedule payments → generate periodic accounting → review GL impact → extract disclosure summary."),
            ("controls", "Controls", "No lease goes live without complete critical fields; modifications logged; month-end lease checklist signed."),
            ("deliverables", "Deliverables", "Lease data checklist, process calendar, UAT lease pack, disclosure extract outline."),
            ("outcomes", "Outcomes", "Shows lease accounting as an operable process, not only a standard reference."),
        ],
        "phases": [
            ("01", "Inventory & ownership", "Who owns lease master data."),
            ("02", "Data quality rules", "Critical fields before go-live."),
            ("03", "Accounting cadence", "Monthly events and reviews."),
            ("04", "Modification handling", "Change control."),
            ("05", "Disclosure pack", "Close reporting readiness."),
        ],
        "decisions": [
            ("Finance owns accounting completeness", "Legal/procurement own contract facts."),
            ("Incomplete leases stay in draft", "Protect close quality."),
            ("Treat modifications as controlled events", "Avoid silent schedule drift."),
        ],
    },
    {
        "slug": "edm-dimension-governance",
        "num": "16",
        "title": "EDM Dimension Governance Model",
        "tag": "EDM · Governance",
        "lede": "Enterprise dimension governance for CoA and EPM — request workflows, hierarchy ownership, validation rules, and sync checkpoints across Fusion and EPM Cloud.",
        "next": "month-end-controller-playbook.html",
        "next_label": "Month-End Playbook →",
        "prev": "lease-accounting-process.html",
        "modules": ["EDM", "GL", "EPBCS", "FCCS"],
        "sections": [
            ("objective", "Objective", "Design dimension governance so values and hierarchies stay consistent across finance systems."),
            ("context", "Context", "When dimensions drift between GL and EPM, plans and actuals stop aligning."),
            ("scope", "Scope", "Request-to-publish workflow, owner model, validation rules, and sync checkpoints."),
            ("approach", "Approach", "Define dimensions in scope → assign owners → design request form → set validations → publish cadence → verify consumers (GL/EPM)."),
            ("walkthrough", "Walkthrough", "Request new cost center → validate → approve → publish → confirm availability in GL and planning."),
            ("controls", "Controls", "No direct rogue values in consumers; every change has requester + approver; hierarchy orphans blocked."),
            ("deliverables", "Deliverables", "Dimension owner matrix, request workflow, validation catalog, sync checklist."),
            ("outcomes", "Outcomes", "Demonstrates cross-system dimension discipline for Fusion + EPM."),
        ],
        "phases": [
            ("01", "Dimension inventory", "What must be governed."),
            ("02", "Ownership model", "Business + finance owners."),
            ("03", "Workflow design", "Request, validate, approve, publish."),
            ("04", "Validation rules", "Format, hierarchy, duplicates."),
            ("05", "Consumer sync", "GL/EPM confirmation."),
        ],
        "decisions": [
            ("One master for shared dimensions", "EDM as control point."),
            ("Publish on a known cadence", "Reduce surprise breaks."),
            ("Reject incomplete hierarchy parents", "Protect rollups."),
        ],
    },
    {
        "slug": "month-end-controller-playbook",
        "num": "17",
        "title": "Month-End Controller Playbook",
        "tag": "Close · Playbook",
        "lede": "A dependency-based month-end playbook for controllers — task owners, gates, evidence, escalation paths, and a reporting pack that makes close status visible.",
        "next": "uat-test-scenario-library.html",
        "next_label": "UAT Library →",
        "prev": "edm-dimension-governance.html",
        "modules": ["GL", "AP", "AR", "Assets", "Cash", "OTBI"],
        "sections": [
            ("objective", "Objective", "Create a controller playbook that turns close from heroic effort into a repeatable operating rhythm."),
            ("context", "Context", "Close delays usually come from unclear ownership and hidden dependencies, not lack of effort."),
            ("scope", "Scope", "Close calendar, RACI, evidence checklist, escalation rules, and status dashboard outline."),
            ("approach", "Approach", "Map dependencies → assign owners → define done criteria → set escalations → run a mock close → refine timings."),
            ("walkthrough", "Walkthrough", "Start close day -2 checklist → clear AP/AR gates → run depreciation & reval → lock periods → publish TB pack → hold close readout."),
            ("controls", "Controls", "No soft close without evidence; blockers logged same day; post-close review within five business days."),
            ("deliverables", "Deliverables", "Close calendar, RACI, evidence checklist, status board wireframe, mock-close findings log."),
            ("outcomes", "Outcomes", "A recruiter-readable close leadership artifact grounded in process design."),
        ],
        "phases": [
            ("01", "Dependency map", "What blocks what."),
            ("02", "RACI", "Owner and backup per task."),
            ("03", "Evidence standard", "What 'done' means."),
            ("04", "Mock close", "Find the real bottlenecks."),
            ("05", "Steady-state rhythm", "Cadence + continuous improvement."),
        ],
        "decisions": [
            ("Visible status beats private spreadsheets", "One close board."),
            ("Backups for every critical owner", "Protect vacation risk."),
            ("Timebox investigations", "Escalate early."),
        ],
    },
    {
        "slug": "uat-test-scenario-library",
        "num": "18",
        "title": "Finance UAT Scenario Library",
        "tag": "UAT · Quality",
        "lede": "A reusable UAT library for Fusion Financials and EPM — happy paths, negatives, edge cases, expected results, and evidence capture so testing proves readiness.",
        "next": "fusion-financials-blueprint.html",
        "next_label": "Back to Case 01 →",
        "prev": "month-end-controller-playbook.html",
        "modules": ["GL", "AP", "AR", "Assets", "EPBCS", "FCCS", "ARCS"],
        "sections": [
            ("objective", "Objective", "Build a UAT scenario library that proves process readiness with clear expected results and evidence."),
            ("context", "Context", "Weak UAT creates production surprises. Strong UAT creates confidence."),
            ("scope", "Scope", "Scenario taxonomy, templates, priority model, evidence standard, and sample packs for GL/P2P/O2C/EPM."),
            ("approach", "Approach", "Define scenario types → write templates → prioritize by risk → execute sample set → capture evidence → triage defects."),
            ("walkthrough", "Walkthrough", "Run AP happy path → run duplicate invoice negative → run period close gate → log defect → retest → sign off."),
            ("controls", "Controls", "No go-live without critical scenario pass; defects severity-rated; evidence stored with scenario ID."),
            ("deliverables", "Deliverables", "Scenario template, priority matrix, sample scenario packs, evidence checklist, sign-off form."),
            ("outcomes", "Outcomes", "Shows quality thinking that connects process design to testable outcomes."),
        ],
        "phases": [
            ("01", "Taxonomy", "Happy, negative, edge, regression."),
            ("02", "Templates", "Steps, data, expected result."),
            ("03", "Priority model", "Critical vs nice-to-have."),
            ("04", "Execution", "Cycle plan and owners."),
            ("05", "Sign-off", "Evidence + residual risk."),
        ],
        "decisions": [
            ("Critical paths first", "Don't drown in low-risk cases."),
            ("Expected results must be measurable", "Pass/fail clarity."),
            ("Retest after every fix", "Avoid false confidence."),
        ],
    },
]

ARTICLE_DEFS = [
    {
        "slug": "coa-design-that-scales",
        "title": "Chart of Accounts Design That Scales",
        "kicker": "Fusion Financials",
        "minutes": "9 min read",
        "summary": "How to shape CoA segments for reporting, control, and growth — without over-engineering on day one.",
        "cover": "cover-coa.svg",
        "body": [
            ("Why CoA decisions feel permanent", "The Chart of Accounts is one of the hardest structures to change later. A segment added 'just in case' becomes permanent complexity. A segment missing for management reporting becomes a monthly spreadsheet tax. Good CoA design balances today's close with tomorrow's questions."),
            ("Start from decisions, not from screens", "Before touching value sets, list the decisions finance must answer: legal entity performance, department spend, product/contribution views, project tracking, and statutory needs. Each decision should map to a segment, hierarchy, or reporting workaround — deliberately."),
            ("A practical segment test", "For every proposed segment ask: Can I name five real reports that need it? Who owns values? What happens if it is wrong on an invoice? If those answers are weak, keep it out of CoA and handle it elsewhere."),
            ("Hierarchy ownership is half the design", "Segments fail when hierarchies are orphaned. Assign an owner for each hierarchy, a request path for new values, and a publish cadence. This is where EDM thinking connects to GL reality."),
            ("Workshop agenda you can reuse", "1) Decision inventory 2) Segment candidates 3) Kill list 4) Value examples 5) Hierarchy owners 6) Open questions log. End with a one-page CoA intent statement everyone can explain."),
        ],
    },
    {
        "slug": "period-close-dependency-map",
        "title": "Building a Period Close Dependency Map",
        "kicker": "Close",
        "minutes": "8 min read",
        "summary": "A simple method to turn month-end chaos into a visible sequence of owners, gates, and evidence.",
        "cover": "cover-close.svg",
        "body": [
            ("Close is a network, not a list", "A checklist without dependencies creates false progress. AP can look 'done' while unaccounted invoices still block GL. Map predecessors first."),
            ("Three columns that matter", "Task, Owner, Blocked-by. Add Done-when evidence as a fourth column. If evidence is vague, the task is not operable."),
            ("Gates beat hopes", "Examples: no depreciation until CIP review complete; no ledger close until bank rec exceptions below threshold; no reporting pack until TB tie-out signed."),
            ("Make status public", "A shared board reduces private follow-ups. Color by on-track / at-risk / blocked. Escalate blockers the same day."),
            ("Improve after every close", "Run a 30-minute post-close review: what slipped, what was unclear, what to change next month. Continuous improvement is part of the playbook."),
        ],
    },
    {
        "slug": "p2p-exception-matrix",
        "title": "The P2P Exception Matrix Starter Kit",
        "kicker": "P2P",
        "minutes": "10 min read",
        "summary": "Happy path is not enough. Design the exception matrix that AP actually lives in — holds, mismatches, and approvals.",
        "cover": "cover-p2p.svg",
        "body": [
            ("Why exceptions define the process", "Most AP effort sits in exceptions. If you only design the happy path, you design a brochure, not an operation."),
            ("Core exception types", "Price/quantity mismatch, missing receipt, duplicate invoice, incomplete supplier data, tax mismatch, coding errors, approval timeout."),
            ("For each exception define four things", "Detection signal, owner, resolution path, and time SLA. Without SLA, exceptions age quietly into close risk."),
            ("Holds are controls, not punishments", "Train users on why a hold exists. Provide a clear release checklist. Mystery holds create shadow process."),
            ("UAT must include negatives", "Duplicate invoice, over-receipt, and forced override scenarios prove the design. Capture evidence for each."),
        ],
    },
    {
        "slug": "epbcs-driver-patterns",
        "title": "EPBCS Driver Model Patterns That Stay Maintainable",
        "kicker": "EPM Planning",
        "minutes": "11 min read",
        "summary": "Driver-based planning patterns that FP&A can explain, maintain, and align with actuals through EDM-aware dimensions.",
        "cover": "cover-epm.svg",
        "body": [
            ("Drivers should tell a story", "Headcount × average cost, volume × price, and ramp curves are useful when business owners can explain them in one sentence."),
            ("Separate assumption input from calculated result", "Forms for drivers; calculations for outcomes. Mixing both on one form creates accidental overwrites."),
            ("Version discipline", "Working, what-if, and final versions need naming rules. Without them, leadership reviews the wrong number."),
            ("Calc sequence documentation", "Write the order of business rules like a close checklist. Opaque calc order becomes a support ticket machine."),
            ("Align dimensions with actuals", "If planning cost centers drift from GL, variance analysis dies. Governance belongs in the design, not as an afterthought."),
        ],
    },
    {
        "slug": "fccs-elimination-basics",
        "title": "FCCS Eliminations Without the Mystery",
        "kicker": "FCCS",
        "minutes": "9 min read",
        "summary": "A plain-language view of ownership, intercompany eliminations, and group close rhythm for consolidation conversations.",
        "cover": "cover-fccs.svg",
        "body": [
            ("Entity structure first", "Eliminations only make sense when the hierarchy and ownership story are clear."),
            ("Intercompany must be identifiable", "If partners and accounts are messy, eliminations become manual archaeology every month."),
            ("Distinguish process from automation", "Automation helps after the process is clear. Automating confusion scales confusion."),
            ("Adjustments need owners", "Top-side adjustments should have requester, approver, and expiry/review logic."),
            ("Group close readout", "End consolidation with a short narrative: what changed, what is open, what needs decision."),
        ],
    },
    {
        "slug": "arcs-risk-based-recs",
        "title": "Risk-Based Reconciliations in ARCS",
        "kicker": "ARCS",
        "minutes": "8 min read",
        "summary": "How to prioritize reconciliations by risk so close quality improves without reconciling everything at the same depth.",
        "cover": "cover-arcs.svg",
        "body": [
            ("Not all accounts are equal", "Cash and suspense deserve different rigor than low-movement prepaid accounts."),
            ("Risk signals", "Balance size, volatility, manual journals, prior defects, and regulatory sensitivity."),
            ("Automation boundaries", "Automate matching where references are reliable. Keep judgment-heavy accounts in guided manual flow."),
            ("Evidence standard", "Every reconciliation needs a definition of complete evidence. Otherwise reviews become taste-based."),
            ("Connect to narrative", "Material recon themes should feed the leadership close narrative — not stay buried in worksheets."),
        ],
    },
    {
        "slug": "otbi-report-catalog",
        "title": "Designing an OTBI Report Catalog Finance Will Trust",
        "kicker": "Reporting",
        "minutes": "7 min read",
        "summary": "Naming, prompts, ownership, and official-vs-working report standards that reduce spreadsheet shadow systems.",
        "cover": "cover-otbi.svg",
        "body": [
            ("Trust is a design outcome", "If two 'trial balances' disagree, users invent a third spreadsheet. Catalog discipline prevents that."),
            ("Name by decision", "Prefer 'Close TB — Official' over 'GL Report 14'. Findability matters."),
            ("Prompt standards", "Ledger, period, and entity prompts should be consistent across the catalog."),
            ("Ownership", "Every official report has a business owner and a technical steward."),
            ("Retirement path", "Old reports must die. Otherwise the catalog becomes a museum."),
        ],
    },
    {
        "slug": "interview-deep-dive-map",
        "title": "How to Walk an Oracle Finance Interview Deep-Dive",
        "kicker": "Career",
        "minutes": "8 min read",
        "summary": "A structure for explaining Fusion/EPM knowledge clearly — objective, process, controls, modules, and outcomes — without inventing employer stories.",
        "cover": "cover-career.svg",
        "body": [
            ("Lead with the business problem", "Interviewers remember clarity. Start with what finance needed to achieve."),
            ("Show process before buttons", "Screenshots fade. Dependency thinking and controls stick."),
            ("Use the case-study spine", "Objective → scope → approach → decisions → controls → outcomes. This portfolio is built that way on purpose."),
            ("Be honest about portfolio framing", "Knowledge projects are valid when labeled clearly. Do not blur them into employment claims."),
            ("End with learning edge", "What you would validate next in a real workshop. Curiosity reads as seniority."),
        ],
    },
]


def svg_cover(title: str, accent: str, path: Path):
    t = H.escape(title[:42])
    path.write_text(
        f"""<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630">
  <defs>
    <linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#0b1220"/>
      <stop offset="55%" stop-color="#102033"/>
      <stop offset="100%" stop-color="{accent}"/>
    </linearGradient>
  </defs>
  <rect width="1200" height="630" fill="url(#g)"/>
  <circle cx="980" cy="120" r="180" fill="{accent}" opacity="0.18"/>
  <circle cx="160" cy="520" r="220" fill="{accent}" opacity="0.12"/>
  <rect x="72" y="72" width="14" height="14" fill="{accent}"/>
  <text x="72" y="140" fill="#99f6e4" font-family="Segoe UI, Arial" font-size="28" letter-spacing="4">KAVYA PROJECT</text>
  <text x="72" y="230" fill="#eef3f8" font-family="Segoe UI, Arial" font-size="54" font-weight="700">{t}</text>
  <text x="72" y="560" fill="#94a3b8" font-family="Segoe UI, Arial" font-size="22">Knowledge library · Oracle Fusion &amp; EPM</text>
</svg>
""",
        encoding="utf-8",
    )


def svg_diagram(name: str, path: Path):
    path.write_text(
        f"""<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="420" viewBox="0 0 1000 420">
  <rect width="1000" height="420" rx="24" fill="#0d1420"/>
  <rect x="40" y="50" width="200" height="90" rx="16" fill="#134e4a"/>
  <rect x="280" y="50" width="200" height="90" rx="16" fill="#115e59"/>
  <rect x="520" y="50" width="200" height="90" rx="16" fill="#0f766e"/>
  <rect x="760" y="50" width="200" height="90" rx="16" fill="#14b8a6"/>
  <path d="M240 95 H280 M480 95 H520 M720 95 H760" stroke="#2dd4bf" stroke-width="3"/>
  <rect x="160" y="220" width="680" height="140" rx="20" fill="#121a28" stroke="#2dd4bf" stroke-opacity="0.35"/>
  <text x="200" y="300" fill="#eef3f8" font-family="Segoe UI, Arial" font-size="28" font-weight="700">{H.escape(name)}</text>
  <text x="200" y="335" fill="#94a3b8" font-family="Segoe UI, Arial" font-size="18">Process flow · control gates · reporting pack</text>
</svg>
""",
        encoding="utf-8",
    )


def project_html(p: dict) -> str:
    toc = "\n".join(f'        <a href="#{sid}">{H.escape(label)}</a>' for sid, label, _ in p["sections"])
    phases = "\n".join(
        f'          <li><span class="phase-num">{n}</span><div><strong>{H.escape(t)}</strong><span>{H.escape(d)}</span></div></li>'
        for n, t, d in p["phases"]
    )
    decisions = "\n".join(
        f"          <div><dt>{H.escape(k)}</dt><dd>{H.escape(v)}</dd></div>" for k, v in p["decisions"]
    )
    modules = "\n".join(f"          <span>{H.escape(m)}</span>" for m in p["modules"])
    deliverables = [x.strip() for x in p["sections"][6][2].replace("Deliverables:", "").split(",") if x.strip()]
    # use explicit deliverables from text - already in section; build chips from phases-like list in section text
    deliv_chips = "\n".join(f"          <span>{H.escape(d.strip())}</span>" for d in p["sections"][6][2].split(",") if d.strip())
    articles_blocks = []
    for sid, label, text in p["sections"]:
        extra = ""
        if sid == "approach":
            extra = f'<ol class="phase-list">\n{phases}\n        </ol>'
        elif sid == "decisions" or label == "Design decisions":
            pass
        if sid == "approach":
            articles_blocks.append(
                f'''      <article class="case-block" id="{sid}" data-reveal>
        <h2>{H.escape(label)}</h2>
        <p>{H.escape(text)}</p>
        <ol class="phase-list">
{phases}
        </ol>
        <figure class="case-figure">
          <img src="../assets/diagrams/{p["slug"]}.svg" alt="Diagram for {H.escape(p["title"])}" width="1000" height="420" loading="lazy" />
          <figcaption>Approach flow for this knowledge project.</figcaption>
        </figure>
      </article>'''
            )
        elif sid == "controls":
            articles_blocks.append(
                f'''      <article class="case-block" id="decisions" data-reveal>
        <h2>Key design decisions</h2>
        <dl class="decision-list">
{decisions}
        </dl>
      </article>
      <article class="case-block" id="{sid}" data-reveal>
        <h2>{H.escape(label)}</h2>
        <p>{H.escape(text)}</p>
      </article>'''
            )
        elif sid == "modules":
            articles_blocks.append(
                f'''      <article class="case-block" id="{sid}" data-reveal>
        <h2>Oracle modules in focus</h2>
        <div class="module-chips">
{modules}
        </div>
      </article>'''
            )
        elif sid == "deliverables":
            articles_blocks.append(
                f'''      <article class="case-block" id="{sid}" data-reveal>
        <h2>{H.escape(label)}</h2>
        <div class="deliverable-grid">
{deliv_chips}
        </div>
      </article>'''
            )
        else:
            articles_blocks.append(
                f'''      <article class="case-block" id="{sid}" data-reveal>
        <h2>{H.escape(label)}</h2>
        <p>{H.escape(text)}</p>
      </article>'''
            )

    # Ensure modules section exists in TOC flow - inject if not in sections as id modules
    section_ids = {s[0] for s in p["sections"]}
    if "modules" not in section_ids:
        # insert modules block before deliverables in rendered list - already handled in loop via deliverables
        # add standalone modules article before deliverables by splicing
        pass

    # Rebuild cleaner content blocks
    blocks = []
    for sid, label, text in p["sections"]:
        if sid == "approach":
            blocks.append(
                f'''      <article class="case-block" id="{sid}" data-reveal>
        <h2>{H.escape(label)}</h2>
        <p>{H.escape(text)}</p>
        <ol class="phase-list">
{phases}
        </ol>
        <figure class="case-figure">
          <img src="../assets/diagrams/{p["slug"]}.svg" alt="Diagram for {H.escape(p["title"])}" width="1000" height="420" loading="lazy" />
          <figcaption>Phased approach diagram for this knowledge project.</figcaption>
        </figure>
      </article>
      <article class="case-block" id="decisions" data-reveal>
        <h2>Key design decisions</h2>
        <dl class="decision-list">
{decisions}
        </dl>
      </article>'''
            )
        elif sid == "deliverables":
            blocks.append(
                f'''      <article class="case-block" id="modules" data-reveal>
        <h2>Oracle modules in focus</h2>
        <div class="module-chips">
{modules}
        </div>
      </article>
      <article class="case-block" id="{sid}" data-reveal>
        <h2>{H.escape(label)}</h2>
        <div class="deliverable-grid">
{deliv_chips}
        </div>
      </article>'''
            )
        else:
            blocks.append(
                f'''      <article class="case-block" id="{sid}" data-reveal>
        <h2>{H.escape(label)}</h2>
        <p>{H.escape(text)}</p>
      </article>'''
            )

    toc_full = toc + '\n        <a href="#decisions">Design decisions</a>\n        <a href="#modules">Modules</a>'

    return f'''<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
  <meta name="description" content="{H.escape(p["lede"])}" />
  <meta name="theme-color" content="#070b12" />
  <title>{H.escape(p["title"])} | Kavya Project</title>
  <link rel="icon" href="../assets/favicon.svg" type="image/svg+xml" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600;700&family=Syne:wght@600;700;800&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../css/styles.css" />
</head>
<body class="page-project is-loaded">
  <div class="cursor" aria-hidden="true"><span class="cursor-dot"></span><span class="cursor-ring"></span></div>
  <div class="noise" aria-hidden="true"></div>
  <canvas id="orb-canvas" aria-hidden="true"></canvas>
  <a class="skip-link" href="#main">Skip to content</a>
  <header class="site-header" data-header>
    <div class="shell header-inner">
      <a class="brand" href="../index.html" data-magnetic>
        <span class="brand-mark" aria-hidden="true"></span>
        <span>Kavya <em>Project</em></span>
      </a>
      <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav" data-nav-toggle>
        <span class="sr-only">Menu</span><span></span><span></span>
      </button>
      <nav id="site-nav" class="site-nav" data-nav>
        <a href="../index.html#about">About</a>
        <a href="../index.html#expertise">Expertise</a>
        <a href="../index.html#projects">Projects</a>
        <a href="../index.html#insights">Insights</a>
        <a href="../index.html#learning">Learning</a>
        <button class="theme-toggle" type="button" data-theme-toggle aria-label="Toggle theme">
          <span class="theme-icon theme-icon-sun" aria-hidden="true">☀</span>
          <span class="theme-icon theme-icon-moon" aria-hidden="true">☾</span>
        </button>
        <a class="nav-cta" href="../index.html#contact" data-magnetic>Contact</a>
      </nav>
    </div>
  </header>
  <main id="main">
    <section class="project-hero">
      <div class="shell project-hero-inner" data-reveal>
        <p class="breadcrumb-nav"><a href="../index.html#projects">&larr; Back to all projects</a></p>
        <div class="project-kicker">
          <span class="badge">Case study {p["num"]}</span>
          <span>Portfolio knowledge project</span>
        </div>
        <h1>{H.escape(p["title"])}</h1>
        <p class="section-lede">{H.escape(p["lede"])}</p>
        <p class="case-note">{NOTE}</p>
        <div class="hero-cta-row">
          <a class="btn btn-primary" href="#objective" data-magnetic>Read full case study</a>
          <a class="btn btn-ghost" href="../index.html#contact" data-magnetic>Contact Kavya</a>
        </div>
      </div>
    </section>
    <section class="shell case-grid">
      <nav class="case-toc" aria-label="On this page" data-reveal>
{toc_full}
      </nav>
{chr(10).join(blocks)}
      <aside class="project-cta-band" data-reveal>
        <h2>Want to discuss this blueprint?</h2>
        <p>Open to conversations about Oracle Fusion Financials and EPM Cloud process design.</p>
        <div class="hero-cta-row">
          <a class="btn btn-primary" href="mailto:kavyareddybindhu4@gmail.com" data-magnetic>Email Kavya</a>
          <a class="btn btn-ghost" href="../index.html#contact" data-magnetic>All contact options</a>
        </div>
      </aside>
    </section>
    <div class="shell project-nav">
      <a class="btn btn-ghost" href="../index.html#projects" data-magnetic>&larr; All projects</a>
      <a class="btn btn-primary" href="{p["next"]}" data-magnetic>Next: {H.escape(p["next_label"])}</a>
    </div>
  </main>
  <footer class="site-footer">
    <div class="shell footer-inner">
      <div>
        <p class="footer-brand">Kavya Project</p>
        <p class="footer-note">Knowledge portfolio · Oracle Fusion Financials &amp; EPM Cloud</p>
      </div>
      <p class="footer-copy">© <span data-year></span> Kavya Reddy</p>
    </div>
  </footer>
  <script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/ScrollTrigger.min.js"></script>
  <script src="../js/main.js"></script>
</body>
</html>
'''


def article_html(a: dict) -> str:
    sections = "\n".join(
        f'''      <article class="case-block" data-reveal>
        <h2>{H.escape(title)}</h2>
        <p>{H.escape(body)}</p>
      </article>'''
        for title, body in a["body"]
    )
    return f'''<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
  <meta name="description" content="{H.escape(a["summary"])}" />
  <meta name="theme-color" content="#070b12" />
  <title>{H.escape(a["title"])} | Kavya Project</title>
  <link rel="icon" href="../assets/favicon.svg" type="image/svg+xml" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600;700&family=Syne:wght@600;700;800&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../css/styles.css" />
</head>
<body class="page-project is-loaded">
  <div class="cursor" aria-hidden="true"><span class="cursor-dot"></span><span class="cursor-ring"></span></div>
  <div class="noise" aria-hidden="true"></div>
  <canvas id="orb-canvas" aria-hidden="true"></canvas>
  <a class="skip-link" href="#main">Skip to content</a>
  <header class="site-header" data-header>
    <div class="shell header-inner">
      <a class="brand" href="../index.html" data-magnetic>
        <span class="brand-mark" aria-hidden="true"></span>
        <span>Kavya <em>Project</em></span>
      </a>
      <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav" data-nav-toggle>
        <span class="sr-only">Menu</span><span></span><span></span>
      </button>
      <nav id="site-nav" class="site-nav" data-nav>
        <a href="../index.html#about">About</a>
        <a href="../index.html#expertise">Expertise</a>
        <a href="../index.html#projects">Projects</a>
        <a href="../index.html#insights">Insights</a>
        <a href="../index.html#learning">Learning</a>
        <button class="theme-toggle" type="button" data-theme-toggle aria-label="Toggle theme">
          <span class="theme-icon theme-icon-sun" aria-hidden="true">☀</span>
          <span class="theme-icon theme-icon-moon" aria-hidden="true">☾</span>
        </button>
        <a class="nav-cta" href="../index.html#contact" data-magnetic>Contact</a>
      </nav>
    </div>
  </header>
  <main id="main">
    <section class="project-hero">
      <div class="shell project-hero-inner" data-reveal>
        <p class="breadcrumb-nav"><a href="../index.html#insights">&larr; Back to insights</a></p>
        <div class="project-kicker">
          <span class="badge">{H.escape(a["kicker"])}</span>
          <span>{H.escape(a["minutes"])}</span>
        </div>
        <h1>{H.escape(a["title"])}</h1>
        <p class="section-lede">{H.escape(a["summary"])}</p>
        <p class="case-note">Insight article from the Kavya Project knowledge library. Educational content only — not employment history or certification claims.</p>
      </div>
    </section>
    <section class="shell case-grid article-layout">
      <figure class="article-hero-figure" data-reveal>
        <img src="../assets/covers/{a["cover"]}" alt="" width="1200" height="630" />
      </figure>
{sections}
      <aside class="project-cta-band" data-reveal>
        <h2>Explore related case studies</h2>
        <p>These insights connect directly to the portfolio project library.</p>
        <div class="hero-cta-row">
          <a class="btn btn-primary" href="../index.html#projects" data-magnetic>Browse projects</a>
          <a class="btn btn-ghost" href="../index.html#contact" data-magnetic>Contact Kavya</a>
        </div>
      </aside>
    </section>
  </main>
  <footer class="site-footer">
    <div class="shell footer-inner">
      <div>
        <p class="footer-brand">Kavya Project</p>
        <p class="footer-note">Knowledge portfolio · Oracle Fusion Financials &amp; EPM Cloud</p>
      </div>
      <p class="footer-copy">© <span data-year></span> Kavya Reddy</p>
    </div>
  </footer>
  <script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/ScrollTrigger.min.js"></script>
  <script src="../js/main.js"></script>
</body>
</html>
'''


def main():
    accents = ["#2dd4bf", "#14b8a6", "#5eead4", "#0d9488", "#2dd4bf", "#67e8f9", "#99f6e4", "#2dd4bf"]
    for i, p in enumerate(NEW_PROJECTS):
        svg_diagram(p["title"], DIAGRAMS / f"{p['slug']}.svg")
        (PROJECTS / f"{p['slug']}.html").write_text(project_html(p), encoding="utf-8")
        print("project", p["slug"])
    for i, a in enumerate(ARTICLE_DEFS):
        svg_cover(a["title"], accents[i % len(accents)], COVERS / a["cover"])
        (ARTICLES_DIR / f"{a['slug']}.html").write_text(article_html(a), encoding="utf-8")
        print("article", a["slug"])
    # index snippets
    rows = []
    for p in NEW_PROJECTS:
        rows.append(
            f'''            <a class="project-row" href="projects/{p["slug"]}.html" data-reveal data-magnetic>
              <span class="project-index">{p["num"]}</span>
              <div class="project-copy">
                <h3>{H.escape(p["title"])}</h3>
                <p>{H.escape(p["lede"][:110])}…</p>
                <span class="project-open">Open full case study →</span>
              </div>
              <span class="project-tag">{H.escape(p["tag"])}</span>
              <span class="project-arrow" aria-hidden="true">→</span>
            </a>'''
        )
    (ROOT / "tools" / "new_project_rows.html").write_text("\n".join(rows), encoding="utf-8")
    cards = []
    for a in ARTICLE_DEFS:
        cards.append(
            f'''            <a class="article-card" href="articles/{a["slug"]}.html" data-reveal data-magnetic>
              <img class="article-cover" src="assets/covers/{a["cover"]}" alt="" width="600" height="315" loading="lazy" />
              <div class="article-card-body">
                <p class="article-meta"><span>{H.escape(a["kicker"])}</span> · {H.escape(a["minutes"])}</p>
                <h3>{H.escape(a["title"])}</h3>
                <p>{H.escape(a["summary"])}</p>
              </div>
            </a>'''
        )
    (ROOT / "tools" / "article_cards.html").write_text("\n".join(cards), encoding="utf-8")
    print("done")


if __name__ == "__main__":
    main()
