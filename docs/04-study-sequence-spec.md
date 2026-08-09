# Study Sequence Specification

Status: **APPROVED v1.1 — technically validated; study start remains frozen**  
Pilot certification: **AWS Certified Solutions Architect – Professional (SAP-C02)**  
Research/approval date: **2026-08-09**

## 1. Purpose

Define the approved order in which official AWS material, grounded AI extraction, architectural contextualization, hands-on work, retrieval, assessment, and mastery evidence are used for SAP-C02.

The sequence has two equal outcomes:

1. pass SAP-C02;
2. improve professional architecture judgment and implementation skill.

## 2. Architecture-first, service-second

Do not study service manuals one service at a time and do not mirror the four exam domains sequentially. SAP-C02 repeatedly reuses security, reliability, cost, performance, networking, operations, deployment, and migration capabilities across domains.

Approved pattern:

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

## 3. Well-Architected framework sandwich

### Pass A — foundation before architecture units
Read the compact framework-level scope fully: purpose/definitions, general design principles, six pillars, high-level pillar design principles, and Well-Architected review/trade-off concepts.

### Pass B — detailed pillar guidance interleaved
Read/selectively extract detailed pillar guidance when the corresponding architecture unit provides service/scenario context.

### Pass C — integrated review near the end
Use framework questions/tooling against complete architectures and capstone scenarios to force cross-pillar trade-off reasoning.

Do not read every pillar end-to-end before service/domain study.

## 4. Role of official AWS courses

Official courses are teaching aids, not curriculum authority. Exam guide/task pages remain the syllabus.

Experienced-architect default:

- Solutions Architect Learning Plan — gap modules only;
- Architecting on AWS — optional refresher;
- AWS Well-Architected Foundations — optional companion to Pass A;
- Well-Architected for Enterprises — optional advanced extension;
- Advanced Architecting on AWS — optional high-value synthesis/capstone;
- Official SAP-C02 Exam Prep — required late exam-readiness overlay.

Use a course/module only when it closes a measured gap, provides a valuable integrated scenario, gives official exam calibration, or materially reduces study time without reducing architecture depth.

## 5. Approved architecture-domain sequence

Exact duration is mastery-driven rather than calendar-driven.

### U00 — Exam scope and baseline
Snapshot current SAP-C02 guide/task pages and coverage map; use the official practice question set once as an early diagnostic when available. Preserve the full official practice exam for late readiness.

### U01 — Well-Architected foundation and architecture decision method
Establish business requirement -> quality attribute -> trade-off -> decision reasoning, six-pillar vocabulary, and a small architecture-review exercise.

### U02 — Organizations, accounts, governance, and identity
Organizations/OU/account design, Control Tower/landing-zone concepts, SCP/RCP/guardrails, resource sharing/delegated administration, workforce identity/cross-account access, centralized logging/security and cost-allocation boundaries. Primary mapping: 1.2, 1.4, 1.5; supports 4.2.

### U03 — Network architecture and hybrid connectivity
VPC/subnet/routing/IP, multi-VPC connectivity, Transit Gateway, PrivateLink/endpoints, Direct Connect/VPN, Route 53/hybrid DNS, edge/global traffic flow, monitoring/troubleshooting. Primary mapping: 1.1. Mandatory implementation plus troubleshooting/change challenge.

### U04 — Security architecture and data protection
Least privilege/cross-account access, encryption/key/certificate strategy, secrets/credentials, preventive/detective controls, centralized security, WAF/Shield/Firewall Manager/Network Firewall, audit/compliance/remediation. Primary mapping: 1.2, 2.3, 3.2. Mandatory control and audit/remediation exercise.

### U05 — Reliability, availability, backup, and disaster recovery
Failure domains, SLAs, RTO/RPO, Multi-AZ vs multi-Region, backup/restore, pilot light/warm standby/multi-site, replication/failover, quotas, static stability, self-healing and DR testing. Primary mapping: 1.3, 2.2, 2.4, 3.4. Mandatory recovery/failure exercise.

### U06 — Compute, platform, and deployment architecture
EC2/Auto Scaling/Elastic Beanstalk, ECS/EKS/Fargate/ECR, Lambda placement, managed vs self-managed, IaC, CI/CD, rollout/rollback, Systems Manager and change automation. Primary mapping: 2.1, 2.5, 3.1, 4.3; supports 4.4. Mandatory deployment plus rollback/change scenario.

### U07 — Storage and data architecture
S3/EBS/EFS/FSx/Storage Gateway, lifecycle/tiering/replication, RDS/Aurora, DynamoDB, ElastiCache, OpenSearch and self-managed database decisions; durability, consistency, availability, scaling, performance, backup and migration. Primary mapping: 2.4, 2.5, 2.6, 4.3, 4.4.

### U08 — Integration, serverless, and decoupled architecture
SQS/SNS/EventBridge/Step Functions, API Gateway, Lambda/serverless placement, buffering/retries/idempotency/failure isolation, sync vs async coupling and modernization. Primary mapping: 2.4, 4.4; supports 2.5, 3.4. Mandatory integrated failure/retry scenario.

### U09 — Performance and scalability engineering
Access-pattern analysis, scaling, caching/buffering/replicas, compute/storage/database selection, CloudFront/Global Accelerator/edge, bottleneck diagnosis and measurable objectives. Primary mapping: 2.5, 3.3. Require measured performance evidence.

### U10 — Observability, operations, automation, and continuous improvement
KPIs, metrics/logs/traces/events, CloudWatch/X-Ray/CloudTrail/Config, alerting/remediation, Systems Manager, runbooks/playbooks, deployment improvement and feedback loops. Primary mapping: 3.1. Mandatory observability + automated-remediation/troubleshooting scenario.

### U11 — Cost architecture and FinOps decisions
Allocation/tagging/account boundaries, Cost Explorer/Budgets/CUR/Trusted Advisor/Compute Optimizer, Savings Plans/RIs/Spot, rightsizing, storage tiering, data transfer, managed-service cost trade-offs and TCO. Primary mapping: 1.5, 2.6, 3.5. Cost-model/report exercises; no artificial spend required.

### U12 — Migration and modernization
Portfolio/wave planning, 7Rs/TCO, Migration Hub/discovery/MGN, DMS/SCT/DataSync/Transfer Family/Snow, networking/identity/governance/security, target architecture and rehost/replatform/refactor/modernization decisions. Primary mapping: 4.1–4.4. Integrated migration scenario.

### U13 — Enterprise architecture capstone and Well-Architected review
Integrate all architecture domains. Required: greenfield architecture, existing-workload improvement, migration/modernization architecture, changed/failure constraint, and Well-Architected review. Maps to all scored tasks.

### U14 — Official exam prep, timed practice, and remediation
Official exam-prep review, task-targeted questions, first full official practice exam, error classification, targeted remediation, and final timed readiness assessment. Exam prep cannot replace missing architecture mastery.

### U15 — Emerging/pretest topics
Low priority. Re-check current exam guide before coverage; do not displace scored-domain work.

## 6. Standard per-unit workflow (U02–U12)

1. **Objective framing** — map tasks, architecture decisions and prerequisites.
2. **Architecture-first human reading** — approved `READ_FULL_CONTEXTUALIZE` scope before service-manual detail.
3. **Architecture guidance synthesis** — Decision Guides, Prescriptive Guidance, reference architectures, WAF sections and other approved sources.
4. **Service decision packet** — targeted documentation for competing services/mechanisms.
5. **Factual compression** — `EXTRACT_VALIDATE` for FAQs, quotas, pricing mechanics, feature matrices and volatile facts.
6. **Decision artifacts + instructor discussion** — choices, trade-offs, failure behavior, security/operations/cost, changed requirement.
7. **Hands-on** — lowest-friction activity that exercises required behavior.
8. **Failure/change challenge** — alter a material assumption/requirement.
9. **Assessment/remediation** — scenario reasoning plus appropriate official/generated questions.
10. **Mastery update** — separate E/A/H evidence; reading completion alone is never mastery.

## 7. Read/extract/reference/lab policy

- `READ_FULL_CONTEXTUALIZE` — exception; use when reasoning continuity is high-value.
- `READ_SELECTIVE_EXTRACT` — default for large architecture/service guidance.
- `EXTRACT_VALIDATE` — dense factual/volatile material.
- `REFERENCE_ONLY` — APIs/CLI/low-level details retrieved only when needed.
- `HANDS_ON` — validate behavior and consequences, not console navigation.
- `ASSESSMENT` — measurement, not primary teaching.

Hands-on levels: H0 none, H1 focused behavior, H2 integrated scenario, H3 open requirements challenge, H4 failure/change injection. Important architecture units normally reach at least H2; networking, security, reliability/DR, deployment, integration, observability and capstone include H3/H4 where practical.

## 8. Source-packet size control

Start small and expand only for demonstrated gaps:

- 1 scope/objective source;
- 1–2 core architecture sources;
- 1 decision/reference architecture source where useful;
- targeted service sections;
- factual references as needed;
- 1 primary hands-on activity plus optional challenge extension.

## 9. New-service rule

A new or newly in-scope service does not automatically create a unit. Map it to an existing architecture decision, assess whether it changes a decision matrix/task coverage, update affected sources/artifacts, and create a new unit only for a genuinely new architecture capability.

## 10. Freshness checkpoints

Re-check current AWS sources at project/start-of-study boundary, before each unit source packet, on relevant AWS changes, before U14, and shortly before the real exam. Apply `docs/13-change-control-freshness.md`.

## 11. Gate relationship

The sequence and resource-treatment policy are operationally approved. The extraction pilot, artifact QA, mastery/session/chat controls, coordinator governance, retention routine, tool policy, change/freshness controls, pipeline-health controls, and synthetic end-to-end dry run have been implemented and validated.

Real study remains independently blocked while `state/project-state.json` has `study_start_approval=BLOCKED`.

If a current pipeline/control/freshness check later fails, affected study work fails closed until the control is restored.

## 12. Authority

The objective-level coverage authority is `aws/sap-c02/objective-map.md`. Source eligibility is governed by `docs/03-source-policy.md`; pipeline use by `docs/05-extraction-pipeline-spec.md` and `docs/17-pipeline-health-spec.md`; mastery/session/chat execution by `docs/09`, `docs/11`, `docs/12`, `docs/14`, and `docs/16`.
