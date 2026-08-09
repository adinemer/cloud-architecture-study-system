# Study Sequence Specification

Status: **APPROVED v1 — planning sequence; study remains blocked until pipeline/QA gates pass**  
Pilot certification: **AWS Certified Solutions Architect – Professional (SAP-C02)**  
Research/approval date: **2026-08-09**

## 1. Purpose

Define the order in which official AWS material, AI extraction, architectural contextualization, hands-on work, and assessment are used for SAP-C02.

This specification answers a core question: **what should be learned first, what should be read versus extracted, when should service documentation enter the process, and where should labs occur?**

The sequence is optimized for two equal outcomes:

1. pass SAP-C02;
2. improve professional architecture judgment and implementation skill.

## 2. Governing decision: architecture-first, service-second

The study plan must **not** begin by reading service user guides one service at a time, and it must **not** mirror the four exam domains in order.

SAP-C02 tasks repeatedly reuse the same architectural capabilities across different domains (for example security, reliability, cost, performance, networking, and deployment). Therefore the primary learning sequence is organized by **architectural dependency and capability**, then mapped back to all exam task IDs.

### The sequence pattern

```text
exam scope / requirements
  -> architecture framework and decision model
  -> architecture-domain guidance
  -> service alternatives and decision criteria
  -> targeted service documentation
  -> factual/volatile references
  -> hands-on implementation
  -> failure/change exercise
  -> scenario assessment
  -> mastery update
```

## 3. Governing decision: the “Well-Architected framework sandwich”

Do **not** read every Well-Architected pillar end-to-end before service/domain study.

Use Well-Architected in three passes:

### Pass A — foundation before architecture units
Human reads the compact framework-level material completely:

- purpose/definitions;
- general design principles;
- six-pillar model;
- high-level design principles for each pillar;
- how Well-Architected reviews and trade-offs are used.

Purpose: establish the architectural vocabulary and decision model used throughout SAP-C02.

### Pass B — detailed pillar guidance interleaved with units
Relevant detailed best-practice sections are selected while studying each architecture unit. Examples:

- Security pillar identity/detection/data-protection sections during security units;
- Reliability foundations/workload/failure-management/DR sections during reliability units;
- Operational Excellence observability/change/operations sections during operations units;
- Cost Optimization and Performance Efficiency guidance during their corresponding units.

Purpose: learn best practices when the associated service and scenario context exists.

### Pass C — integrated review near the end
Use the AWS Well-Architected Tool/framework questions against complete architectures and capstone scenarios.

Purpose: force cross-pillar trade-off reasoning rather than memorizing isolated best practices.

## 4. Role of official AWS courses

Official courses are **teaching aids**, not the curriculum authority. The exam guide/task pages remain the syllabus.

### Default experienced-architect track

- **Solutions Architect Learning Plan:** do not complete end-to-end by default. AWS positions it as a beginner-oriented guided path. Use individual modules only for diagnosed gaps.
- **Architecting on AWS (24h):** optional refresher/gap remediation, not mandatory.
- **AWS Well-Architected Foundations (3h):** optional companion to Pass A. The framework documentation remains authoritative; use the course if it improves retention or if the initial WAF baseline is weak.
- **Well-Architected for Enterprises:** optional professional-depth extension after integrated review; valuable for applying WAF across teams/workloads, not required for SAP-C02 coverage.
- **Advanced Architecting on AWS:** optional high-value synthesis/capstone because AWS positions it for experienced architects and SAP preparation. It is not mandatory because the controlled documentation/lab workflow should already provide this depth.
- **Official SAP-C02 Exam Prep:** required as the **exam-readiness overlay**, after architecture learning is substantially complete. It must not replace architecture study.

### Course selection rule

Use a course/module only if it does one of the following better than the existing source packet:

1. closes a measured prerequisite gap;
2. gives a useful integrated scenario that is difficult to reproduce efficiently;
3. provides official exam-style calibration;
4. materially reduces study time without reducing architectural depth.

Otherwise skip it.

## 5. SAP-C02 architecture-domain sequence

The approved v1 sequence is below. The exact duration is mastery-driven rather than calendar-driven.

### Phase 0 — scope, baseline, and architecture model

#### U00 — Exam scope and baseline

Purpose:
- snapshot current SAP-C02 guide/task pages;
- establish coverage map;
- take the official practice question set once as a diagnostic if available;
- identify foundational gaps without starting remediation yet.

Sources:
- SAP-C02 exam guide and task pages: `READ_FULL_CONTEXTUALIZE`;
- technologies/in-scope/out-of-scope lists: `EXTRACT_VALIDATE`;
- official practice question set: `ASSESSMENT`.

Do **not** consume the full official practice exam here; preserve it for late readiness measurement.

#### U01 — Well-Architected foundation and architecture decision method

Purpose:
- establish business-requirement -> quality-attribute -> trade-off -> decision reasoning;
- learn six pillars and general design principles;
- establish vocabulary used for all subsequent units.

Sources:
- WAF core/framework-level material: `READ_FULL_CONTEXTUALIZE`;
- pillar introductions/design principles: `READ_FULL_CONTEXTUALIZE` for the short approved scope;
- detailed pillar best practices: defer to later units.

Hands-on:
- no implementation lab required;
- one small architecture review exercise is required.

### Phase 1 — enterprise cloud foundation

#### U02 — Organizations, accounts, governance, and identity foundation

Core topics:
- AWS Organizations and OU/account design;
- management-account boundaries;
- Control Tower/landing-zone concepts;
- SCP/RCP/guardrail concepts;
- resource sharing and delegated administration;
- centralized workforce identity and cross-account access;
- centralized logging/event foundations;
- account/tagging/cost-allocation boundaries.

Primary exam mapping: 1.2, 1.4, 1.5; supports 4.2.

Architecture sources:
- Organizing Your AWS Environment Using Multiple Accounts;
- AWS SRA core/organization-account/identity sections;
- relevant WAF Security guidance.

Hands-on target:
- simulation/sandbox or controlled multi-account exercise where practical;
- avoid creating unnecessary permanent organizations/accounts solely for study.

#### U03 — Network architecture and hybrid connectivity

Core topics:
- VPC/subnet/routing/IP design;
- multi-VPC connectivity;
- Transit Gateway and transitive-routing decisions;
- PrivateLink/service endpoints;
- Direct Connect/VPN/hybrid connectivity;
- Route 53 and hybrid DNS;
- edge/global connectivity and traffic flow;
- network monitoring/troubleshooting.

Primary exam mapping: 1.1; supports 1.2, 2.2, 2.3, 2.4, 3.3, 3.4, 4.2.

Hands-on target:
- mandatory focused implementation plus troubleshooting/change challenge.

#### U04 — Security architecture and data protection

Core topics:
- least privilege and cross-account access;
- encryption/key/certificate strategy;
- secrets and credential management;
- detective/preventive controls;
- centralized security services;
- WAF/Shield/Firewall Manager/Network Firewall decision patterns;
- audit/traceability;
- patching/compliance/security automation;
- data protection and incident-response implications.

Primary exam mapping: 1.2, 2.3, 3.2; supports 4.2.

Hands-on target:
- mandatory security-control lab and at least one audit/remediation exercise.

### Phase 2 — resilient workload architecture

#### U05 — Reliability, availability, backup, and disaster recovery

Core topics:
- AWS failure domains/global infrastructure;
- availability targets, SLAs, RTO/RPO;
- Multi-AZ versus multi-Region decisions;
- backup/restore, pilot light, warm standby, multi-site patterns;
- replication/failover;
- service quotas as reliability constraints;
- static stability, data-plane recovery, self-healing;
- DR testing and recovery automation.

Primary exam mapping: 1.3, 2.2, 2.4, 3.4.

Hands-on target:
- mandatory recovery/failure exercise; a configuration-only lab is insufficient.

#### U06 — Compute, platform, and deployment architecture

Core topics:
- EC2/Auto Scaling/Elastic Beanstalk selection;
- containers: ECS/EKS/Fargate/ECR decisions;
- Lambda placement where compute-selection context matters;
- managed-service versus self-managed trade-offs;
- CloudFormation/IaC;
- CI/CD and deployment/rollback strategies;
- Systems Manager/configuration management;
- change safety and automation.

Primary exam mapping: 2.1, 2.5, 3.1, 4.3; supports 4.4.

Hands-on target:
- mandatory deployment lab plus rollback/change scenario.

#### U07 — Storage and data architecture

Core topics:
- S3/EBS/EFS/FSx/storage-gateway decisions;
- lifecycle/tiering/replication;
- RDS/Aurora, DynamoDB, ElastiCache, OpenSearch and self-managed database decision criteria;
- durability, consistency, availability, scaling and performance implications;
- backup and migration implications;
- purpose-built data-store selection.

Primary exam mapping: 2.4, 2.5, 2.6, 4.3, 4.4; supports reliability and migration tasks.

Hands-on target:
- targeted experiments where behavior/performance/replication is difficult to learn by reading alone.

#### U08 — Integration, serverless, and decoupled architecture

Core topics:
- SQS/SNS/EventBridge/Step Functions decision criteria;
- API Gateway and event-driven integration;
- Lambda/serverless architectural placement;
- buffering, retries, idempotency, failure isolation;
- asynchronous versus synchronous coupling;
- modernization opportunities.

Primary exam mapping: 2.4 and 4.4; supports 2.5 and 3.4.

Hands-on target:
- mandatory integrated event-driven scenario including a failure/retry behavior test.

### Phase 3 — optimize and continuously improve

#### U09 — Performance and scalability engineering

Core topics:
- workload/access-pattern analysis;
- scaling strategies;
- caching, buffering and replicas;
- instance/compute selection and rightsizing;
- storage/database performance selection;
- CloudFront/Global Accelerator/edge decisions;
- bottleneck identification and measurable performance objectives.

Primary exam mapping: 2.5, 3.3; supports 2.4 and 3.4.

Hands-on target:
- performance experiment with measured before/after evidence rather than only configuration steps.

#### U10 — Observability, operations, automation, and continuous improvement

Core topics:
- business/technical KPIs;
- metrics/logs/traces/events;
- CloudWatch/X-Ray/CloudTrail/Config relationships;
- alerting and automated remediation;
- Systems Manager;
- runbooks/playbooks;
- deployment improvement;
- failure exercises/game-day thinking;
- operational feedback loops.

Primary exam mapping: 3.1; supports 2.1, 2.2, 3.2, 3.3, 3.4.

Hands-on target:
- mandatory observability + automated-remediation/troubleshooting scenario.

#### U11 — Cost architecture and FinOps decisions

Core topics:
- cost allocation/tagging/account boundaries;
- Cost Explorer/Budgets/CUR/Trusted Advisor/Compute Optimizer;
- Savings Plans/Reserved Instances/Spot;
- rightsizing;
- storage tiering;
- data-transfer economics;
- managed-service cost trade-offs;
- Pricing Calculator/TCO reasoning.

Primary exam mapping: 1.5, 2.6, 3.5; supports 4.1.

Hands-on target:
- cost-modeling and report-analysis exercises; no artificial spend is required.

### Phase 4 — transform existing estates

#### U12 — Migration and modernization

Core topics:
- portfolio assessment and wave planning;
- 7Rs and TCO;
- Migration Hub/Application Discovery Service/Application Migration Service;
- DMS/SCT/DataSync/Transfer Family/Snow choices;
- migration networking, identity and governance;
- migration security;
- target architecture selection using U02–U11 knowledge;
- rehost/replatform/refactor decisions;
- containers/serverless/purpose-built data/integration modernization.

Primary exam mapping: 4.1–4.4.

Architecture sources:
- Migration Lens;
- relevant AWS CAF/prescriptive migration strategy material;
- targeted migration service guidance.

Hands-on target:
- integrated migration scenario/simulation; implementation only where it adds learning value.

### Phase 5 — integrate architecture knowledge

#### U13 — Enterprise architecture capstone and Well-Architected review

Purpose:
- combine organization, identity, networking, security, reliability, compute, data, integration, operations, performance and cost;
- perform Well-Architected reviews;
- resolve cross-pillar conflicts from business requirements;
- redesign existing systems under changed constraints.

Required activities:
- at least one greenfield architecture;
- at least one existing-workload improvement review;
- at least one migration/modernization architecture;
- at least one failure/change constraint introduced after the design;
- WAF review using approved framework questions/tooling.

Primary exam mapping: all scored domains.

### Phase 6 — exam readiness overlay

#### U14 — Official exam prep, timed practice, and remediation

Sequence:
1. official SAP-C02 exam-prep review/course;
2. domain/task-targeted official or QA-approved questions;
3. full official practice exam (preserve first-attempt value until here);
4. error classification by task and architecture principle;
5. targeted remediation from approved sources/labs;
6. final timed assessment(s) and readiness gate.

The exam-prep layer may change prioritization and remediation depth, but it may **not** retroactively redefine the curriculum source of truth.

### U15 — Emerging/pretest topics (low priority)

Current guide lists security/responsible-AI controls as emerging unscored/pretest content. Cover only after scored domains are controlled. Re-check the exam guide before the exam because emerging topics can change.

## 6. Standard per-unit workflow

Every architecture unit U02–U12 uses the same controlled sequence unless the source packet records a justified exception.

### Step 1 — objective framing
- identify mapped SAP-C02 task IDs;
- define architecture decisions the unit must enable;
- define prerequisite concepts;
- run a short diagnostic if prior knowledge is uncertain.

### Step 2 — architecture-first human reading
Read the approved `READ_FULL_CONTEXTUALIZE` source/sections **before** service-manual extraction.

Goal: understand the problem, design principles and trade-off vocabulary before learning product detail.

### Step 3 — architecture guidance synthesis
Use selected Decision Guides, Prescriptive Guidance, reference architectures, WAF sections and other approved architecture sources.

The learner reads high-value reasoning sections; AI extracts/contextualizes the approved remainder.

### Step 4 — service decision packet
Only now identify the competing AWS services/mechanisms and retrieve their relevant documentation sections.

Typical sections:
- overview/core concepts;
- architecture/design guidance;
- security;
- resilience;
- networking/data flow;
- scaling/performance;
- monitoring/troubleshooting;
- important constraints/quotas;
- pricing model/cost drivers.

### Step 5 — factual compression
AI extracts FAQs, quotas, pricing mechanics, feature matrices and other dense factual sources under `EXTRACT_VALIDATE`.

Human reads only flagged/high-impact facts or samples required by QA.

### Step 6 — decision artifacts and instructor discussion
Before the lab, the learner must be able to explain:
- when to choose each major option;
- trade-offs;
- failure behavior;
- security/operational/cost implications;
- what requirement would change the decision.

### Step 7 — hands-on
Select the lowest-friction official lab that exercises the needed behavior:

Priority order is **fit to learning objective**, not product prestige:
1. focused Builder Lab or targeted Workshop when mechanics/behavior is the gap;
2. SimuLearn when requirements + architecture + implementation are well aligned;
3. Well-Architected Lab when pillar/review behavior is the target;
4. custom controlled AWS-account challenge when official labs do not exercise the needed architecture behavior;
5. Cloud Quest/Jam Event only when its scenario is unusually well aligned or provides useful challenge practice.

### Step 8 — failure/change challenge
For important units, change one requirement or break one assumption after the solution works. Examples:
- Region failure;
- quota pressure;
- security policy change;
- lower RTO/RPO;
- acquisition/new account boundary;
- data residency;
- unexpected cost constraint;
- traffic growth.

### Step 9 — assessment and remediation
Use scenario questions, architecture explanation, and where appropriate official questions. Wrong answers are mapped to the underlying architectural misconception, not just the service fact.

### Step 10 — mastery update
Record separate evidence for:
- **Exam readiness (E)**;
- **Architecture mastery (A)**;
- **Hands-on capability (H)**.

No unit is marked complete solely because reading was finished.

## 7. Final read/extract/reference/lab policy

### 7.1 Full reading is the exception

Use `READ_FULL_CONTEXTUALIZE` only when all are true:

1. reasoning/argument continuity matters;
2. the approved scope is high-density and directly relevant;
3. selective extraction would likely hide assumptions or trade-offs;
4. the human reading cost is justified by broad/repeated value.

Examples:
- SAP-C02 exam guide/task pages;
- WAF framework-level foundation and short pillar design-principle scopes;
- selected high-value decision/strategy papers such as multi-account strategy when the approved scope remains cohesive.

**Do not interpret this as “read every WAF pillar completely.”**

### 7.2 Selective human reading + AI extraction is the default for large architecture/service sources

Use `READ_SELECTIVE_EXTRACT` for:
- WAF detailed pillar guidance;
- AWS SRA and extensions;
- Prescriptive Guidance;
- large decision/strategy guides;
- service user guides;
- extensive resilience/security/network/performance documentation.

AI must identify candidate high-value sections, but the source packet/policy controls the final human-reading scope.

### 7.3 AI factual extraction

Use `EXTRACT_VALIDATE` for:
- FAQs;
- quotas/limits;
- pricing mechanics;
- service availability/scope;
- feature matrices;
- dense configuration/capability references;
- selected monitoring/troubleshooting facts.

Do not turn volatile values into memorization material unless architecture/exam relevance justifies it.

### 7.4 Reference only

Use `REFERENCE_ONLY` for:
- API/SDK/CLI exhaustive references;
- low-level parameters;
- incidental implementation detail;
- document history except for freshness checks.

Reference-only material is retrieved during labs/troubleshooting or when a decision requires exact confirmation.

### 7.5 Hands-on policy

Hands-on exists to validate **behavior and architectural consequences**, not to prove that a console wizard can be followed.

Lab levels:

- `H0` — no lab; reading/discussion is sufficient.
- `H1` — focused mechanic/behavior lab.
- `H2` — integrated multi-service scenario.
- `H3` — open requirements challenge with limited implementation guidance.
- `H4` — failure/change injection after a working design.

Important architecture units should normally reach at least `H2`; networking, security, reliability/DR, deployment, integration, observability and capstone should include `H3` or `H4` evidence where practical.

Guided labs alone do not demonstrate architecture mastery.

### 7.6 Assessment policy

- Early official Practice Question Set: diagnostic only.
- Official Practice Exam: late readiness gate.
- Generated questions: allowed only after QA Gate 3 approves their schema/process.
- Repeatedly answering memorized official questions is not mastery evidence.

## 8. Source-packet size control

For a normal architecture unit, the coordinator should initially select a **small packet**, then expand only if gaps remain.

Default target:
- 1 scope/objective source;
- 1–2 core architecture sources;
- 1 decision/reference architecture source when useful;
- targeted service sections for the main alternatives;
- factual references only as needed;
- 1 primary hands-on activity plus optional challenge extension.

Do not preload dozens of documents. Retrieval is progressive and problem-driven.

## 9. When a new service appears

A newly launched or newly in-scope service does **not** automatically create a new study unit.

Process:
1. map it to an existing architecture decision/problem;
2. determine whether it changes a current decision matrix or exam task coverage;
3. update only the affected source packet/artifact;
4. create a new unit only if the architecture capability is genuinely new.

## 10. Freshness checkpoints

Re-check current AWS sources:

- at project start;
- before each architecture unit source packet is approved;
- when AWS announces a material service/guidance change affecting that unit;
- before official practice exam/readiness phase;
- shortly before the real exam.

The objective map is versioned against the current SAP-C02 guide.

## 11. Gate relationship

This sequence and resource-treatment policy are **approved as the v1 planning design**.

However, certification study remains blocked by the charter until:

- Issue #3 proves the extraction pipeline can execute `READ_SELECTIVE_EXTRACT` and `EXTRACT_VALIDATE` with acceptable fidelity/completeness/time savings;
- Issue #4 defines artifact schemas, provenance and QA controls;
- remaining mastery/change-control specifications are approved.

If the pipeline pilot fails, fix the pipeline/tooling first. Change this study policy only when the evidence shows the policy itself is defective.

## 12. Sources used to validate the sequence design

Official AWS sources consulted during this design pass include:

- SAP-C02 exam guide and Domain 1–4 task pages;
- AWS Well-Architected Framework, general design principles and pillar guidance;
- Security and Reliability pillar material;
- AWS Security Reference Architecture including its phased approach;
- Organizing Your AWS Environment Using Multiple Accounts;
- AWS Decision Guides;
- AWS Solutions Architect training page/learning-plan catalog;
- AWS Skill Builder digital training/Builder Labs information;
- current AWS training information for SimuLearn/Lab Maker and related hands-on formats;
- AWS Well-Architected Foundations / Well-Architected for Enterprises training information;
- AWS Advanced Architecting material;
- the authoritative resource inventory in `aws/sap-c02/source-inventory.md`.

## Gate status

**Issue #2 sequence-design deliverable complete, subject to creation/approval of the coverage map and source-policy update in the same gate.**
