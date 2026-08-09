# Issue #3 Manual Gold Checklist — v1

Status: **APPROVED PILOT BASELINE**  
Date: 2026-08-09

Purpose: define the minimum architecture-relevant facts, qualifiers, and direct-reading targets that the extraction pipeline must preserve. This is a compact QA baseline, not a replacement for the source.

## Sample A — AWS Well-Architected Framework: General design principles

Source: `https://docs.aws.amazon.com/wellarchitected/latest/framework/general-design-principles.html`

Processing intent: `READ_FULL_CONTEXTUALIZE`.

Mandatory provider recommendations/facts:

1. Stop guessing capacity needs; use elastic capacity and automatic scale in/out.
2. Test systems at production scale using on-demand environments that can be decommissioned.
3. Automate with architectural experimentation in mind; automation enables replication, auditability, and rollback.
4. Consider evolutionary architectures; cloud automation/testing reduces the risk of architectural change over time.
5. Drive architectures using data; use workload behavior data to inform architecture improvements.
6. Improve through game days; regularly simulate production events to identify improvements and build organizational experience.

Architecture-changing qualifiers to preserve:
- these are general design principles, not service-specific implementation requirements;
- production-scale testing is temporary/on-demand and cost is tied to when the environment is running;
- game days simulate events in production; the source does not state that every test must intentionally cause customer impact.

Direct-reading target: **entire source**. It is short and reasoning-dense.

## Sample B — Amazon VPC User Guide: Gateway route tables

Source: `https://docs.aws.amazon.com/vpc/latest/userguide/gateway-route-tables.html`

Processing intent: `READ_SELECTIVE_EXTRACT`.

Mandatory facts/constraints:

1. Gateway route tables can be associated with an internet gateway or virtual private gateway to control traffic entering a VPC.
2. Supported route targets are the default local route, a Gateway Load Balancer endpoint, or a network interface for a middlebox appliance.
3. When using a GWLB endpoint/network interface as target, allowed destinations are the full VPC CIDR or a subnet CIDR within the VPC.
4. A gateway route table cannot be associated if existing routes use unsupported targets.
5. A gateway route table cannot be associated if it contains routes to CIDRs outside the VPC ranges.
6. A gateway route table cannot be associated when route propagation is enabled.
7. Routes cannot be added to CIDR blocks outside the VPC ranges.
8. Prefix lists cannot be used as destinations.
9. A gateway route table cannot control/intercept traffic outside the VPC, including traffic through an attached transit gateway.
10. A target network interface must be attached to a running instance; for traffic through an internet gateway, it also requires a public IP address.
11. Return traffic from the destination subnet must traverse the same middlebox; asymmetric routing is not supported.
12. Route-table rules apply to traffic that leaves a subnet via its gateway router MAC, not same-subnet layer-2 traffic to another ENI MAC.

Qualifiers/examples to preserve:
- examples are illustrative; their specific CIDRs/ENI IDs are not universal requirements;
- the transit-gateway statement is specifically about gateway route tables, not a claim that transit-gateway traffic can never be inspected by another architecture;
- Local Zone edge-association support is not universal.

Direct-reading target: **Rules and considerations** section. The earlier route tables/examples may be extracted unless a learner needs mechanics clarification.

## Sample C — AWS Service Quotas User Guide: Introduction

Source: `https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html`

Processing intent: `EXTRACT_VALIDATE`.

Mandatory facts/constraints:

1. Quotas are maximum values for resources, actions, and items in an AWS account.
2. Services define their quotas and default values.
3. A quota can apply at account, resource, or Region scope depending on the quota.
4. Service Quotas shows defaults and whether quotas are adjustable at account level.
5. Applied quotas are quota overrides/increases over AWS defaults.
6. Adjustable account-level quotas can be requested through Service Quotas; some quotas can also be increased at resource level.
7. Increase requests can be approved, denied, or partially approved and take time to process.
8. Service Quotas can show current utilization after an account has been active for a period of time.
9. Automatic Management can monitor quota usage and notify before allocated quota is exhausted.
10. Global quotas apply at account level; increase requests for a global quota are made from a designated Region for each AWS partition.
11. Resource-level quotas include context information describing which resource(s) and scope the quota applies to.

Qualifiers to preserve:
- not all quotas are adjustable;
- quota scope must be checked rather than assumed;
- quota values and adjustability are operational reference data and can change;
- an increase request is not guaranteed to be approved.

Direct-reading target for conservative pilot measurement: **Terminology in Service Quotas** only. In production, `EXTRACT_VALIDATE` may require no full human section when QA passes and no architecture-sensitive ambiguity is flagged.

## Sample D — AWS Security Reference Architecture: Core architecture

Sources:
- `https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/architecture.html`
- supporting SRA library guidance.

Processing intent: `READ_SELECTIVE_EXTRACT` with selected core narrative read directly.

Mandatory facts/recommendations:

1. AWS SRA is a reference architecture for security services and controls in a multi-account AWS environment.
2. The architecture intentionally emphasizes security controls and simplifies the application/data tiers for readability.
3. Not every workload/environment must deploy every security service; selection depends on threat exposure, requirements, and risk.
4. The SRA is intended to provide options and architectural relationships that organizations can tailor.
5. For elements/services, the guide describes security purpose, recommended placement, relationships/data sharing, and design considerations.
6. Design considerations include optional features/configurations with important security implications and common variations driven by alternate requirements/constraints.
7. The core architecture uses organization/account boundaries including management, security tooling, log archive, network, shared services, and workload/application contexts.
8. AWS describes the core SRA as a starting/foundational security architecture and recommends consulting deep-dive architectures after the baseline as needed.

Architecture-changing qualifiers to preserve:
- **reference** architecture does not mean every component is mandatory;
- service placement recommendations may vary with requirements/constraints;
- the current guide is living guidance and should be checked for document history/freshness.

Direct-reading targets:
- SRA purpose/value and the paragraph explaining why not every workload needs every service;
- organization/account structure rationale;
- the design-considerations narrative for any unit that uses SRA recommendations.

## Critical fail examples across all samples

The extraction must fail QA if it says any of the following:

- “AWS requires all workloads to deploy every SRA security service.”
- “Gateway route tables support asymmetric middlebox routing.”
- “Gateway route tables can intercept Transit Gateway traffic.”
- “All AWS service quotas are adjustable.”
- “A quota-increase request will be approved.”
- “Well-Architected requires a fixed capacity value before deployment.”

These examples deliberately test the kinds of drift/overgeneralization the study system is designed to prevent.
