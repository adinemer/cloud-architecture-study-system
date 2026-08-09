# SAP-C02 Curriculum / Coverage Map

Status: **APPROVED v1 planning map — study not started**  
Research/approval date: **2026-08-09**

## Purpose

Map every current scored SAP-C02 task to the approved architecture-domain learning sequence in `../../docs/04-study-sequence-spec.md`.

This map prevents curriculum drift: a unit may teach across exam domains, but no scored task may disappear from coverage.

## Unit key

- `U00` Exam scope and baseline
- `U01` Well-Architected foundation and architecture decision method
- `U02` Organizations, accounts, governance, and identity foundation
- `U03` Network architecture and hybrid connectivity
- `U04` Security architecture and data protection
- `U05` Reliability, availability, backup, and disaster recovery
- `U06` Compute, platform, and deployment architecture
- `U07` Storage and data architecture
- `U08` Integration, serverless, and decoupled architecture
- `U09` Performance and scalability engineering
- `U10` Observability, operations, automation, and continuous improvement
- `U11` Cost architecture and FinOps decisions
- `U12` Migration and modernization
- `U13` Enterprise architecture capstone and Well-Architected review
- `U14` Official exam prep, timed practice, and remediation
- `U15` Emerging/pretest topics

## Coverage map

| SAP-C02 task | Primary units | Supporting units | Required outcome |
|---|---|---|---|
| **1.1 Architect network connectivity strategies** | U03 | U02, U04, U05, U12, U13 | Design VPC/hybrid/global connectivity, DNS, routing, segmentation, monitoring, and connectivity trade-offs |
| **1.2 Prescribe security controls** | U04 | U02, U03, U05, U10, U13 | Select identity, access, encryption, network, detective/preventive, compliance and centralized-security controls |
| **1.3 Design reliable and resilient architectures** | U05 | U03, U07, U08, U09, U10, U13 | Design for failure domains, quotas, RTO/RPO, replication, backup, self-healing and multi-Region behavior |
| **1.4 Design a multi-account AWS environment** | U02 | U04, U11, U12, U13 | Design Organizations/OUs/accounts, governance, centralized identity/logging/security and account provisioning |
| **1.5 Determine cost optimization and visibility strategies** | U11 | U02, U07, U09, U13 | Design tagging/allocation, budgets/reporting, purchasing, rightsizing, storage/data-transfer and cost visibility |
| **2.1 Design a deployment strategy to meet business requirements** | U06 | U10, U13 | Choose IaC, CI/CD, rollout/rollback, immutable/change-management and deployment automation strategies |
| **2.2 Design a solution to ensure business continuity** | U05 | U03, U07, U10, U13 | Convert business continuity requirements into backup, recovery, failover, multi-Region and testing strategies |
| **2.3 Determine security controls based on requirements** | U04 | U02, U03, U13 | Convert workload requirements into correct identity, encryption, network, logging and protection controls |
| **2.4 Design a strategy to meet reliability requirements** | U05 | U03, U07, U08, U10, U13 | Choose scaling, decoupling, replication, failover, quotas and self-healing mechanisms from reliability targets |
| **2.5 Design a solution to meet performance objectives** | U09 | U03, U06, U07, U08, U13 | Map access patterns/performance targets to compute, storage, database, caching, network and edge decisions |
| **2.6 Determine a cost optimization strategy to meet solution goals and objectives** | U11 | U06, U07, U09, U13 | Optimize new designs using pricing models, purchasing, elasticity, storage tiers and data-transfer awareness |
| **3.1 Determine a strategy to improve overall operational excellence** | U10 | U06, U13 | Improve observability, deployment, automation, runbooks, feedback loops, remediation and operational metrics |
| **3.2 Determine a strategy to improve security** | U04 | U02, U03, U10, U13 | Assess an existing system and improve identity, detection, encryption, network controls, compliance and remediation |
| **3.3 Determine a strategy to improve performance** | U09 | U03, U06, U07, U08, U10, U13 | Diagnose bottlenecks and redesign compute/data/network/caching/scaling based on measured objectives |
| **3.4 Determine a strategy to improve reliability** | U05 | U03, U07, U08, U10, U13 | Diagnose reliability risks and improve recovery, quotas, isolation, scaling, decoupling and operational response |
| **3.5 Identify opportunities for cost optimizations** | U11 | U06, U07, U09, U10, U13 | Identify and prioritize rightsizing, purchasing, storage, transfer, architecture and governance savings |
| **4.1 Select existing workloads and processes for potential migration** | U12 | U11, U13 | Assess portfolio, dependencies, business value, readiness, TCO and migration candidates |
| **4.2 Determine the optimal migration approach** | U12 | U02, U03, U04, U05, U11, U13 | Choose 7R strategy, wave/landing-zone/network/security/data-transfer approach and migration tooling |
| **4.3 Determine a new architecture for existing workloads** | U12 | U03–U11, U13 | Use previously learned architecture domains to design target AWS architectures for migrated workloads |
| **4.4 Determine opportunities for modernization and enhancements** | U12 | U06, U07, U08, U09, U10, U11, U13 | Select replatform/refactor, managed services, containers, serverless, event-driven and purpose-built data improvements |

## Cross-cutting control units

### U00
Maps to all tasks for scope and baseline only; it does not satisfy mastery for any task.

### U01
Provides Well-Architected vocabulary/decision principles used across all tasks. Detailed pillar content is revisited in the relevant primary unit.

### U13
Required integration unit for **all scored tasks**. It validates the ability to balance security, reliability, performance, cost and operational requirements in complete architectures.

### U14
Maps to all tasks for exam readiness and remediation; it cannot replace missing architecture mastery from U02–U13.

## Coverage rule

A scored task is considered curriculum-covered only when:

1. its primary unit has approved sources and activities;
2. required supporting concepts are available;
3. at least one decision/scenario outcome maps explicitly to the task;
4. mastery evidence can be recorded under the project mastery model;
5. U13 integration exercises revisit the task in a complete-system context.

## Emerging/pretest content

Current SAP-C02 guidance identifies security/responsible-AI controls as emerging/pretest material. These are tracked under `U15`, not mixed into scored-task mastery. Re-check the exam guide before U14 and before the real exam.

## Drift prevention

- Do not add a unit because a service is fashionable or newly launched; first map it to an existing task/architecture decision.
- Do not remove a unit without demonstrating that all mapped task outcomes remain covered elsewhere.
- Any SAP-C02 task addition/removal/change requires this file to be versioned before study continues on affected units.
