# AWS SAP-C02 Official Resource Inventory

Status: **GATE 1 COMPLETE — classifications remain provisional until Gate 2 / pipeline pilot**  
Research date: **2026-08-09**  
Certification: **AWS Certified Solutions Architect – Professional (SAP-C02)**  
Source policy: **Official AWS only; current canonical English source preferred**

## 1. Purpose

This inventory defines the official AWS source universe that may be used to build the SAP-C02 study plan. It is an inventory, **not yet the final study sequence**.

The final sequence, reading depth, and per-topic source selection will be defined in Planning Gate 2. The processing classes below are provisional and must be validated by the extraction-pipeline pilot.

## 2. Authority hierarchy

Use sources in this order when scope or guidance conflicts:

1. **Current SAP-C02 Exam Guide and its domain/task pages** — authoritative certification scope.
2. **Current canonical AWS service/framework documentation** — authoritative provider behavior and recommendations.
3. **Current AWS architecture guidance** — Well-Architected, Decision Guides, Prescriptive Guidance, reference architectures, security/migration guidance.
4. **Current AWS Training and Certification catalog** — authoritative for available AWS-created courses, labs, and assessment products, but not for exam scope.
5. **AWS engineering/blog material** — supplemental context or freshness signal; never overrides current canonical documentation.

### Freshness rule

- Prefer canonical English pages under current/`latest` documentation paths.
- Record retrieval date and any visible document revision/change log.
- Treat localized mirrors, cached search results, old PDFs, and old blog posts as potentially stale.
- When a course/catalog page conflicts with a newer retirement/change announcement, use the newer official announcement for availability status.
- The SAP-C02 in-scope service list is explicitly non-exhaustive and subject to change; it is a scope signal, not a mandate to study every listed service equally.

## 3. Processing classes

Defined in [`../../docs/03-source-policy.md`](../../docs/03-source-policy.md):

- `READ_FULL_CONTEXTUALIZE`
- `READ_SELECTIVE_EXTRACT`
- `EXTRACT_VALIDATE`
- `REFERENCE_ONLY`
- `HANDS_ON`
- `ASSESSMENT`

All classifications below are **PROVISIONAL** until validated in the extraction pilot.

---

# A. Certification scope authorities — mandatory control sources

| Resource | Purpose | Access | Proposed treatment | Study-plan role | Freshness / notes |
|---|---|---|---|---|---|
| [SAP-C02 Exam Guide](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-professional-02/solutions-architect-professional-02.html) | Defines target candidate, exam mechanics, four scored domains, emerging/pretest topics, and links to scope references | Free | `READ_FULL_CONTEXTUALIZE` | **Mandatory control source**; snapshot before plan construction and re-check before exam | Current guide is living content; exam code can remain SAP-C02 while guide details evolve |
| Domain 1–4 task pages | Exact knowledge/skill statements for each task | Free | `READ_FULL_CONTEXTUALIZE` + structured extraction | **Mandatory curriculum mapping source** | Treat task statements as higher authority than course/catalog organization |
| [Technologies and Concepts](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-professional-02/sap-technologies-concepts.html) | Non-exhaustive architecture concept categories | Free | `EXTRACT_VALIDATE` | Coverage cross-check | Subject to change; no implied weighting from order |
| [In-Scope AWS Services](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-professional-02/sap-02-in-scope-services.html) | Current non-exhaustive list of services/features considered in scope | Free | `EXTRACT_VALIDATE` + versioned snapshot | Coverage/reference control; **not** a service-by-service curriculum | Subject to change; objective mapping determines depth |
| [Out-of-Scope AWS Services](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-professional-02/sap-02-out-of-scope-services.html) | Current explicit exclusions | Free | `REFERENCE_ONLY` + snapshot | Prevent unnecessary study | Current canonical page should be re-checked periodically |
| Mentions of AWS Services on the Exam | Service naming/short-name behavior | Free | `REFERENCE_ONLY` | Exam mechanics | Re-check near exam date |
| [Certification landing page](https://aws.amazon.com/certification/certified-solutions-architect-professional/) | Exam logistics and current AWS-recommended preparation entry points | Free | `REFERENCE_ONLY` | Discovery of official prep resources | Training links can change independently of exam guide |

## Current scored domain snapshot

- **Domain 1 — Design Solutions for Organizational Complexity: 26%**
  - 1.1 Architect network connectivity strategies
  - 1.2 Prescribe security controls
  - 1.3 Design reliable and resilient architectures
  - 1.4 Design a multi-account AWS environment
  - 1.5 Determine cost optimization and visibility strategies
- **Domain 2 — Design for New Solutions: 29%**
  - 2.1 Design a deployment strategy to meet business requirements
  - 2.2 Design a solution to ensure business continuity
  - 2.3 Determine security controls based on requirements
  - 2.4 Design a strategy to meet reliability requirements
  - 2.5 Design a solution to meet performance objectives
  - 2.6 Determine a cost optimization strategy to meet solution goals and objectives
- **Domain 3 — Continuous Improvement for Existing Solutions: 25%**
  - 3.1 Determine a strategy to improve overall operational excellence
  - 3.2 Determine a strategy to improve security
  - 3.3 Determine a strategy to improve performance
  - 3.4 Determine a strategy to improve reliability
  - 3.5 Identify opportunities for cost optimizations
- **Domain 4 — Accelerate Workload Migration and Modernization: 20%**
  - 4.1 Select existing workloads and processes for potential migration
  - 4.2 Determine the optimal migration approach
  - 4.3 Determine a new architecture for existing workloads
  - 4.4 Determine opportunities for modernization and enhancements

## Current technology/concept categories

Compute; cost management; database; disaster recovery; high availability; management and governance; microservices and component decoupling; migration and data transfer; networking/connectivity/content delivery; security; serverless design principles; storage.

## Emerging/pretest content

The current guide separately identifies **security and responsible-AI controls** as emerging/pretest material. The guide states these questions do not affect the score. Therefore:

- track this section for freshness;
- do not allow it to displace scored-domain study time;
- revisit only after scored-domain coverage is controlled.

---

# B. Official AWS structured learning and exam-prep resources

| Resource family | Purpose | Access model | Proposed treatment | Proposed role |
|---|---|---|---|---|
| **SAP-C02 Exam Prep Plan** on AWS Skill Builder | AWS-created certification preparation workflow | Mix of free and subscription content | `ASSESSMENT` + selective teaching | Use as an **exam-prep overlay**, not the architecture curriculum |
| **AWS Certification Official Practice Question Set** | Short official exam-style question set | Free | `ASSESSMENT` | Early calibration and question-style familiarization; do not consume repeatedly as teaching material |
| **Exam Prep digital course / enhanced exam prep** | Domain review, exam-style explanations, flashcards, labs/questions depending access tier | Free core / subscription-enhanced | `READ_SELECTIVE_EXTRACT` + `ASSESSMENT` | Use near/after domain learning to detect exam gaps |
| **AWS Certification Official Practice Exam** | Full official readiness assessment | Subscription/access-dependent | `ASSESSMENT` | Late-stage readiness gate; preserve first attempt value |
| [Solutions Architect Learning Plan](https://aws.amazon.com/training/learn-about/architect/) | Broad AWS-created learning path explicitly aimed at beginners | Skill Builder | `REFERENCE_ONLY` / gap-remediation | **Do not take end-to-end by default** for an experienced architect; use as a catalog/map for gaps |
| **Architecting on AWS** (listed as 24-hour on-demand course) | Broad architecture fundamentals and AWS service integration | Skill Builder | `READ_SELECTIVE_EXTRACT` / optional course | Gap-remediation or structured refresher, not mandatory if official documentation path covers objectives efficiently |
| **AWS Well-Architected Foundations** (listed as 3-hour on-demand course) | Concise introduction to Well-Architected concepts | Skill Builder | `READ_SELECTIVE_EXTRACT` | Optional orientation; framework documentation remains authoritative |
| **Advanced Architecting on AWS** | Advanced scenario-based architecting course | Classroom/Digital Classroom availability varies | `READ_SELECTIVE_EXTRACT` / optional structured synthesis | High-value optional synthesis if access/time justify it; **not required** by system design |
| **Solutions Architect Ramp-Up Guide** | AWS-curated index of courses, blogs, whitepapers and other architect resources | Free | `REFERENCE_ONLY` | Discovery aid only; inventory/plan decides what is actually used |
| **AWS Digital Classroom** | Instructor-led-style digital learning plus labs | Subscription | Optional | Use only if it materially improves learning efficiency over approved source + lab workflow |

### Decision for Issue #1

Official courses are **eligible resources**, not automatically mandatory resources. Planning Gate 2 will decide which course components add unique value versus duplicating architecture publications and labs.

---

# C. Official hands-on resources

| Resource | What it provides | Access / environment | Proposed treatment | Proposed study role |
|---|---|---|---|---|
| **AWS Builder Labs** | Self-paced guided labs in real AWS environments | Skill Builder subscription | `HANDS_ON` | Core candidate for focused service/integration practice without maintaining every environment manually |
| **AWS SimuLearn** | Customer/requirements conversations followed by architecture work and live AWS implementation; a Solutions Architect Learning Plan is currently listed | Skill Builder | `HANDS_ON` | **High-value architecture candidate** because it joins requirements, design, communication, and implementation |
| **AWS Workshops** | AWS-authored self-guided workshops, generally using an AWS account | Free content; workload charges may apply | `HANDS_ON` | Targeted integrated/advanced labs when a workshop maps directly to an objective or architecture unit |
| [AWS Well-Architected Labs](https://www.wellarchitectedlabs.com/) | Workshops/labs organized around Well-Architected practices | Free content; AWS account/cost may apply | `HANDS_ON` | Architecture review, reliability, cost, operational and other pillar practice |
| **AWS Cloud Quest** | Role-based immersive/gamified cloud scenarios including solutions architect | Skill Builder | `HANDS_ON` optional | Reinforcement where a relevant advanced scenario exists; not core if slower than direct labs |
| **Lab Maker** | AI-generated personalized guided labs in a simulated AWS console | Skill Builder Team subscription | `HANDS_ON` experimental | Optional targeted practice; generated labs require QA and must not define curriculum |
| **AWS Jam Events** | Collaborative challenge-based exercises | Event/team availability | `HANDS_ON` optional | Useful challenge format if accessible; not required |
| **AWS Jam Journeys** | Former role/domain-based challenge journeys | **Retired June 30, 2026** | **EXCLUDED** | Do not include in plan despite older/generic catalog references |

### Hands-on selection rule

The plan should prefer the **lowest-friction official lab that exercises the architectural behavior required by the objective**. A long immersive experience is not automatically better than a focused Builder Lab or Workshop.

---

# D. Core architecture publications and decision material

| Resource family | Architectural value | Proposed treatment | Proposed role |
|---|---|---|---|
| [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/) | Provider-wide principles, trade-offs, best practices across six pillars | `READ_FULL_CONTEXTUALIZE` for foundation/core; pillar sections may use section-level overrides | **Core architecture foundation** and recurring review framework |
| Well-Architected pillar guidance | Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, Sustainability | Mix of `READ_FULL_CONTEXTUALIZE` and `READ_SELECTIVE_EXTRACT` | Objective-linked architecture principles; avoid reading every subsection indiscriminately |
| [Well-Architected Lenses](https://docs.aws.amazon.com/wellarchitected/latest/userguide/lenses.html) | Workload/industry-specific interpretation of WAF | `READ_SELECTIVE_EXTRACT` | Use only relevant lenses; **Migration Lens is directly relevant to Domain 4** |
| [AWS Well-Architected Tool](https://docs.aws.amazon.com/wellarchitected/latest/userguide/intro.html) | Structured workload reviews against WAF | `HANDS_ON` / `REFERENCE_ONLY` | Architecture-review exercises and evidence of design reasoning, not primary reading |
| [AWS Architecture Center](https://aws.amazon.com/architecture/) | Curated architecture guidance, reference diagrams, patterns, decision material | `REFERENCE_ONLY` discovery + selected `READ_*` sources | Primary discovery hub for architecture-specific sources |
| [AWS Decision Guides](https://aws.amazon.com/getting-started/decision-guides/) | Structured criteria for choosing among AWS services/options | Usually `READ_FULL_CONTEXTUALIZE`; long guides may be selective | **High-value decision material** for architecture and exam alternatives |
| AWS Reference Architecture Diagrams | Integrated target designs and service relationships | `READ_SELECTIVE_EXTRACT` + architectural review | Pattern/context source; never copy without deriving requirements/trade-offs |
| [AWS Prescriptive Guidance](https://docs.aws.amazon.com/prescriptive-guidance/) | Vetted strategies/patterns for migration, modernization, deployment, security, data, operations | Usually `READ_SELECTIVE_EXTRACT`; selected strategy documents may be full-read | Major source for real implementation/architecture patterns |
| [AWS Security Reference Architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/introduction.html) | Holistic multi-account security-service placement, guardrails, account structure, alternatives | `READ_SELECTIVE_EXTRACT` with selected narrative/core architecture full-read | **High-value enterprise security/multi-account architecture source** |
| [Organizing Your AWS Environment Using Multiple Accounts](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/) | OU/account design and isolation/governance strategy | `READ_FULL_CONTEXTUALIZE` candidate | Domain 1 multi-account anchor source |
| **Establishing Your Cloud Foundation on AWS** | Foundational enterprise/cloud environment guidance | `READ_SELECTIVE_EXTRACT` / selected full-read | Landing-zone/governance context |
| **AWS Fault Isolation Boundaries** | Failure domains and containment boundaries | `READ_FULL_CONTEXTUALIZE` candidate | Reliability/resilience mental model |
| [AWS Cloud Adoption Framework (AWS CAF)](https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/) | Transformation perspectives and cloud adoption capabilities | `READ_SELECTIVE_EXTRACT` | Domain 4/enterprise transformation context; use architecture-relevant sections only |
| **AWS Solutions Library** | Vetted deployable solutions/reference implementations | `REFERENCE_ONLY` / `HANDS_ON` | Reusable examples and implementation references when directly relevant |
| [Amazon Builders' Library](https://aws.amazon.com/builders-library/) | Engineering articles from Amazon practitioners on resilient distributed-system operation/design | `READ_SELECTIVE_EXTRACT` supplemental | Deepen architecture reasoning on directly relevant topics (timeouts, retries, overload, shuffle-sharding, static stability, etc.); **not authoritative for AWS service behavior** |

### Architecture-publication rule

Architecture publications are selected by **objective and decision problem**, not by a blanket rule such as “read all whitepapers.” The Architecture Center and Ramp-Up Guide are discovery mechanisms; the approved source inventory for each unit determines what is actually read.

---

# E. Service-level official documentation

Service user guides are necessary, but **full user-guide reading is not the default**.

| Source/section type | Proposed treatment | Why |
|---|---|---|
| Service overview / core concepts | `READ_SELECTIVE_EXTRACT`; full-read only if conceptually foundational | Establish capabilities, scope, terminology and boundaries |
| Architecture / design guidance | `READ_FULL_CONTEXTUALIZE` or `READ_SELECTIVE_EXTRACT` | High architectural value |
| Security sections / security best practices | `READ_SELECTIVE_EXTRACT` | Extract IAM, encryption, network/security boundaries and operational controls |
| Resilience / availability / DR sections | `READ_SELECTIVE_EXTRACT` | Required for failure-domain and continuity reasoning |
| Networking/data-flow behavior | `READ_SELECTIVE_EXTRACT` | Required for connectivity, private access, routing and data-transfer decisions |
| Scaling/performance behavior | `READ_SELECTIVE_EXTRACT` | Required for architecture decision drivers |
| Monitoring/troubleshooting sections | `EXTRACT_VALIDATE` or targeted `READ_SELECTIVE_EXTRACT` | Architecture-relevant failure signals and operating model |
| Quotas/limits | `EXTRACT_VALIDATE` + `REFERENCE_ONLY` | Important constraints, but poor end-to-end reading material |
| API/SDK/CLI references | `REFERENCE_ONLY` | Implementation lookup, not architecture curriculum |
| How-to tutorials | `HANDS_ON` when chosen for a lab | Learn mechanics only when relevant |
| Document history/change log | `REFERENCE_ONLY` + automated freshness check candidate | Detect meaningful product/document changes |

### Service-document selection pattern

For each architecture unit, the eventual source packet should start from the decision/problem and pull only the relevant service sections. The system must **not** create a reading plan that walks service manuals from page 1 to the end.

---

# F. FAQs, quotas, pricing, and factual references

| Resource family | Proposed treatment | Study role |
|---|---|---|
| **AWS Product and Technical FAQs** | `EXTRACT_VALIDATE` | Fast extraction of feature distinctions, supported behaviors, and common constraints; validate high-impact facts in canonical docs |
| **Service Quotas / AWS General Reference quotas and endpoints** | `EXTRACT_VALIDATE` + `REFERENCE_ONLY` | Capture architecturally meaningful hard/default limits, scope (Region/account/resource), and adjustability only when they influence design |
| **AWS Pricing pages** | `EXTRACT_VALIDATE` + `REFERENCE_ONLY` | Pricing models and cost drivers, not memorization of volatile prices |
| **AWS Pricing Calculator** | `HANDS_ON` / `REFERENCE_ONLY` | Scenario-based cost modeling; explicitly relevant to SAP-C02 objectives |
| **AWS Compute Optimizer / Cost Explorer / Budgets / CUR documentation** | selective `READ_SELECTIVE_EXTRACT` + `HANDS_ON` | Cost governance, rightsizing, visibility and continuous-improvement scenarios |
| Service availability / Regional service data | `REFERENCE_ONLY` | Use when a scenario depends on Region/service availability |

### Volatility rule

Do not create flashcards for volatile numeric prices or low-value default limits unless the exam objective specifically makes the distinction important. Teach the **cost/constraint model and lookup method** instead.

---

# G. Migration and modernization corpus

| Resource | Proposed treatment | Role |
|---|---|---|
| [AWS Well-Architected Migration Lens](https://docs.aws.amazon.com/wellarchitected/latest/migration-lens/migration-lens.html) | `READ_FULL_CONTEXTUALIZE` / selected sections depending pilot | Domain 4 anchor: migration phases, 7 Rs, Well-Architected migration considerations |
| AWS Prescriptive Guidance — migration strategy and patterns | `READ_SELECTIVE_EXTRACT`; selected strategy sections full-read | Detailed assess/mobilize/migrate patterns and implementation guidance |
| AWS Cloud Adoption Framework | `READ_SELECTIVE_EXTRACT` | Organizational/transformation context around migration and modernization |
| Migration service user guides (MGN, DMS, DataSync, Migration Hub, Snow Family, Transfer Family, etc.) | Section-level `READ_SELECTIVE_EXTRACT` | Service mechanics/constraints only when mapped to Domain 4 decisions |
| Reference architectures / modernization patterns | `READ_SELECTIVE_EXTRACT` | Replatform/refactor/modernization decision context |

---

# H. Official assessment resources

| Assessment | When to use | Control rule |
|---|---|---|
| Official Practice Question Set | Early baseline and question-style familiarization | Record first-attempt reasoning; do not turn answer memorization into mastery evidence |
| Exam-prep domain questions / flashcards | After learning relevant domain/unit | Use for gap detection, not primary teaching |
| Official Practice Exam | Late readiness stage | Preserve first attempt; use only after substantial curriculum coverage |
| System-generated questions | Throughout | Must pass QA/artifact schema rules; clearly distinguish generated assessment from official AWS assessment |

---

# I. Supplemental official AWS sources — allowed but not default curriculum

| Source | Policy |
|---|---|
| AWS Architecture Blog | Use for recent patterns, launches, and examples when canonical architecture/docs are insufficient; label as supplemental |
| AWS What's New | Freshness/change detection only; follow through to canonical docs before changing study material |
| AWS Training & Certification Blog | Training availability/change announcements; not exam-scope authority |
| AWS re:Post / Knowledge Center | Optional troubleshooting evidence; mixed authorship means it is not part of the default authoritative corpus |
| re:Invent / AWS event sessions | Optional deep-dive enrichment when a topic has high value and current canonical docs are not enough |
| AWS Samples / AWS-owned GitHub repositories | Labs/reference implementation only after provenance and maintenance status are checked |

---

# J. Explicit exclusions / anti-bloat rules

The default plan **will not** include:

- third-party certification courses;
- exam dumps;
- blanket reading of every AWS whitepaper;
- blanket reading of every service user guide;
- API/CLI/SDK references as study curriculum;
- all Solutions Architect Learning Plan courses end-to-end merely because AWS lists them;
- every Well-Architected lens;
- every in-scope AWS service at equal depth;
- AWS Jam Journeys (retired June 30, 2026);
- stale localized/cached pages as certification-scope authority;
- blog posts as substitutes for current canonical documentation;
- generated labs or AI notes that have not passed the project QA lifecycle.

---

# K. Current SAP-C02 in-scope service snapshot

Source: current canonical English **In-Scope AWS Services** page, retrieved 2026-08-09. AWS states this list is **non-exhaustive and subject to change**. This appendix exists for traceability; it does **not** imply equal study depth.

### Analytics
Amazon Athena; AWS Data Exchange; Amazon Data Firehose; Amazon EMR; AWS Glue; Amazon Kinesis Data Streams; AWS Lake Formation; Amazon Managed Service for Apache Flink; Amazon Managed Streaming for Apache Kafka (Amazon MSK); Amazon OpenSearch Service; Amazon QuickSight.

### Application Integration
Amazon AppFlow; AWS AppSync; Amazon EventBridge; Amazon MQ; Amazon SNS; Amazon SQS; AWS Step Functions.

### Blockchain
Amazon Managed Blockchain.

### Business Applications
Amazon SES.

### Cloud Financial Management
AWS Budgets; AWS Cost and Usage Report; AWS Cost Explorer; Savings Plans.

### Compute
AWS App Runner; AWS Auto Scaling; AWS Batch; AWS Elastic Beanstalk; Amazon EC2; Amazon EC2 Auto Scaling; AWS Fargate; AWS Lambda; Amazon Lightsail; AWS Outposts; AWS Wavelength.

### Containers
Amazon ECR; Amazon ECS; Amazon ECS Anywhere; Amazon EKS; Amazon EKS Anywhere; Amazon EKS Distro.

### Database
Amazon Aurora; Amazon Aurora Serverless; Amazon DocumentDB; Amazon DynamoDB; Amazon ElastiCache; Amazon Keyspaces; Amazon Neptune; Amazon RDS; Amazon Redshift; Amazon Timestream.

### Developer Tools
AWS CodeArtifact; AWS CodeBuild; AWS CodeDeploy; Amazon CodeGuru; AWS CodePipeline; AWS X-Ray.

### End User Computing
Amazon AppStream 2.0; Amazon WorkSpaces.

### Frontend Web and Mobile
AWS Amplify; Amazon API Gateway; AWS Device Farm; Amazon Pinpoint.

### Internet of Things (IoT)
AWS IoT Core; AWS IoT Device Defender; AWS IoT Device Management; AWS IoT Events; AWS IoT Greengrass; AWS IoT SiteWise; AWS IoT Things Graph; AWS IoT 1-Click.

### Machine Learning
Amazon Comprehend; Amazon Fraud Detector; Amazon Kendra; Amazon Lex; Amazon Personalize; Amazon Polly; Amazon Rekognition; Amazon SageMaker AI; Amazon Textract; Amazon Transcribe; Amazon Translate.

### Media Services
Amazon Elastic Transcoder; Amazon Kinesis Video Streams.

### Management and Governance
AWS CloudFormation; AWS CloudTrail; Amazon CloudWatch; Amazon CloudWatch Logs; AWS CLI; AWS Compute Optimizer; AWS Config; AWS Control Tower; AWS Health Dashboard; AWS License Manager; Amazon Managed Grafana; Amazon Managed Service for Prometheus; AWS Management Console; AWS Organizations; AWS Proton; AWS Service Catalog; Service Quotas; AWS Systems Manager; AWS Trusted Advisor; AWS Well-Architected Tool.

### Migration and Transfer
AWS Application Discovery Service; AWS Application Migration Service; AWS DMS; AWS DataSync; AWS Migration Hub; AWS Schema Conversion Tool; AWS Snow Family; AWS Transfer Family.

### Networking and Content Delivery
Amazon CloudFront; AWS Direct Connect; Elastic Load Balancing; AWS Global Accelerator; AWS PrivateLink; Amazon Route 53; AWS Transit Gateway; Amazon VPC; AWS VPN.

### Security, Identity, and Compliance
AWS Artifact; AWS Audit Manager; AWS Certificate Manager; AWS CloudHSM; Amazon Cognito; Amazon Detective; AWS Directory Service; AWS Firewall Manager; Amazon GuardDuty; AWS IAM Identity Center; AWS IAM; Amazon Inspector; AWS KMS; Amazon Macie; AWS Network Firewall; AWS RAM; AWS Secrets Manager; AWS Security Hub; AWS STS; AWS Shield; AWS WAF.

### Storage
AWS Backup; Amazon EBS; AWS Elastic Disaster Recovery; Amazon EFS; Amazon FSx; Amazon S3; Amazon S3 Glacier; AWS Storage Gateway.

### Current explicit out-of-scope snapshot
Amazon GameLift (Game Tech). The AWS page states the exclusion list is also non-exhaustive and subject to change.

---

# L. Resource metadata required in the future per-unit inventory

Each selected source should carry at least:

- source ID;
- exact title;
- canonical URL;
- provider (`AWS`);
- source family/type;
- certification (`SAP-C02`);
- objective/task IDs;
- architecture-domain tags;
- processing class;
- human-reading scope;
- retrieval date;
- visible publication/revision date where available;
- supersession/change-log status;
- access model (`free`, `subscription`, `classroom`, `own-account-cost`, etc.);
- QA state;
- notes about conflicts or freshness risk.

---

# M. Gate 1 conclusions for Planning Gate 2

1. **The exam guide and task pages are the syllabus authority.** AWS courses are teaching resources, not the curriculum source of truth.
2. **Well-Architected is foundational but does not replace service/decision documentation.** Gate 2 must decide how much framework material is read upfront versus interleaved by architecture domain.
3. **Service user guides should be section-selected, not read end-to-end by default.**
4. **Decision Guides, Prescriptive Guidance, SRA, selected whitepapers, reference architectures, and Migration Lens are central architecture-enrichment sources.**
5. **Hands-on should mix focused labs and integrated scenarios.** Builder Labs, SimuLearn, Workshops, and Well-Architected Labs are the strongest current candidates; Cloud Quest/Jam Events are optional; Jam Journeys are retired.
6. **Official exam prep is an overlay and assessment layer**, not the primary professional-architecture learning path.
7. **Freshness must be a first-class control.** Live AWS scope pages and service documentation can change during a multi-month study program.
8. **Resource selection must remain objective-driven.** The in-scope service list is broad and non-exhaustive; studying every listed service equally would create unnecessary work.

## Gate status

**Issue #1 deliverable complete.**  
Next dependency: **Issue #2 — define the study sequence and final read/extract/lab policy.**
