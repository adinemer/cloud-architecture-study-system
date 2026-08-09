# AWS SAP-C02 Official Resource Inventory

Status: **APPROVED v1.1 — classifications validated; study start remains frozen**  
Research date: **2026-08-09**  
Certification: **AWS Certified Solutions Architect – Professional (SAP-C02)**  
Source policy: **Official AWS only; current canonical English source preferred**

## 1. Purpose

This inventory defines the official AWS source universe available to the approved SAP-C02 study plan. It is a source inventory, not the study sequence; sequencing and reading depth are governed by `../../docs/04-study-sequence-spec.md`.

The processing-class model has been validated by the extraction-pipeline pilot and artifact QA controls. Per-topic source selection remains objective-driven and is refreshed under the project freshness policy before use.

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

These classifications are the approved baseline. A current source packet may apply a documented section-level override under source policy.

---

# A. Certification scope authorities — mandatory control sources

| Resource | Purpose | Access | Treatment | Study-plan role | Freshness / notes |
|---|---|---|---|---|---|
| [SAP-C02 Exam Guide](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-professional-02/solutions-architect-professional-02.html) | Defines target candidate, exam mechanics, four scored domains, emerging/pretest topics, and links to scope references | Free | `READ_FULL_CONTEXTUALIZE` | **Mandatory control source**; snapshot before study and re-check before exam | Current guide is living content; exam code can remain SAP-C02 while guide details evolve |
| Domain 1–4 task pages | Exact knowledge/skill statements for each task | Free | `READ_FULL_CONTEXTUALIZE` + structured extraction | **Mandatory curriculum mapping source** | Treat task statements as higher authority than course/catalog organization |
| [Technologies and Concepts](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-professional-02/sap-technologies-concepts.html) | Non-exhaustive architecture concept categories | Free | `EXTRACT_VALIDATE` | Coverage cross-check | Subject to change; no implied weighting from order |
| [In-Scope AWS Services](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-professional-02/sap-02-in-scope-services.html) | Current non-exhaustive list of services/features considered in scope | Free | `EXTRACT_VALIDATE` + versioned snapshot | Coverage/reference control; **not** a service-by-service curriculum | Subject to change; objective mapping determines depth |
| [Out-of-Scope AWS Services](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-professional-02/sap-02-out-of-scope-services.html) | Current explicit exclusions | Free | `REFERENCE_ONLY` + snapshot | Prevent unnecessary study | Re-check periodically |
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

The current guide separately identifies **security and responsible-AI controls** as emerging/pretest material. The guide states these questions do not affect the score. Track for freshness, do not displace scored-domain study time, and revisit only after scored-domain coverage is controlled.

---

# B. Official AWS structured learning and exam-prep resources

| Resource family | Purpose | Access model | Treatment | Role |
|---|---|---|---|---|
| **SAP-C02 Exam Prep Plan** on AWS Skill Builder | AWS-created certification preparation workflow | Mix of free and subscription content | `ASSESSMENT` + selective teaching | **Exam-prep overlay**, not architecture curriculum |
| **AWS Certification Official Practice Question Set** | Short official exam-style question set | Free | `ASSESSMENT` | Early calibration; do not consume repeatedly as teaching material |
| **Exam Prep digital course / enhanced exam prep** | Domain review, explanations, flashcards, labs/questions depending access | Free core / subscription-enhanced | `READ_SELECTIVE_EXTRACT` + `ASSESSMENT` | Use near/after architecture learning to detect exam gaps |
| **AWS Certification Official Practice Exam** | Full official readiness assessment | Subscription/access-dependent | `ASSESSMENT` | Late readiness gate; preserve first attempt value |
| [Solutions Architect Learning Plan](https://aws.amazon.com/training/learn-about/architect/) | Broad guided architecture learning path | Skill Builder | `REFERENCE_ONLY` / gap-remediation | Do not take end-to-end by default for an experienced architect |
| **Architecting on AWS** | Broad architecture fundamentals and service integration | Skill Builder | `READ_SELECTIVE_EXTRACT` / optional | Gap remediation/refresher |
| **AWS Well-Architected Foundations** | Concise Well-Architected introduction | Skill Builder | `READ_SELECTIVE_EXTRACT` | Optional orientation |
| **Advanced Architecting on AWS** | Advanced scenario-based architecting | Availability varies | `READ_SELECTIVE_EXTRACT` / optional synthesis | Optional high-value capstone/synthesis |
| **Solutions Architect Ramp-Up Guide** | AWS-curated architect resource index | Free | `REFERENCE_ONLY` | Discovery only |
| **AWS Digital Classroom** | Digital structured learning plus labs | Subscription | Optional | Use only when it materially improves learning efficiency |

### Course decision

Official courses are eligible resources, not automatically mandatory resources. `docs/04-study-sequence-spec.md` defines which components add unique value versus duplicating architecture publications and labs.

---

# C. Official hands-on resources

| Resource | What it provides | Access / environment | Treatment | Study role |
|---|---|---|---|---|
| **AWS Builder Labs** | Self-paced guided labs in real AWS environments | Skill Builder subscription | `HANDS_ON` | Core candidate for focused service/integration practice |
| **AWS SimuLearn** | Requirements conversations, architecture work and live implementation | Skill Builder | `HANDS_ON` | High-value architecture candidate |
| **AWS Workshops** | AWS-authored self-guided workshops | Free content; workload charges may apply | `HANDS_ON` | Targeted integrated/advanced labs |
| [AWS Well-Architected Labs](https://www.wellarchitectedlabs.com/) | Labs organized around Well-Architected practices | Free content; account/cost may apply | `HANDS_ON` | Architecture review and pillar practice |
| **AWS Cloud Quest** | Role-based immersive/gamified scenarios | Skill Builder | `HANDS_ON` optional | Reinforcement where aligned |
| **Lab Maker** | AI-generated personalized guided labs | Skill Builder Team subscription | `HANDS_ON` experimental | Optional; generated labs require QA |
| **AWS Jam Events** | Collaborative challenges | Event/team availability | `HANDS_ON` optional | Optional challenge format |
| **AWS Jam Journeys** | Former role/domain challenge journeys | **Retired June 30, 2026** | **EXCLUDED** | Do not include |

Hands-on selection prioritizes fit to the learning objective and architectural behavior, not product prestige or duration.

---

# D. Core architecture publications and decision material

| Resource family | Architectural value | Treatment | Role |
|---|---|---|---|
| [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/) | Provider-wide principles/trade-offs across six pillars | `READ_FULL_CONTEXTUALIZE` for foundation; section overrides later | Core foundation/review framework |
| Well-Architected pillar guidance | Pillar-specific best practices | Mix of full/selective reading | Objective-linked architecture principles |
| [Well-Architected Lenses](https://docs.aws.amazon.com/wellarchitected/latest/userguide/lenses.html) | Workload/industry interpretation | `READ_SELECTIVE_EXTRACT` | Relevant lenses only; Migration Lens directly supports Domain 4 |
| [AWS Well-Architected Tool](https://docs.aws.amazon.com/wellarchitected/latest/userguide/intro.html) | Structured workload reviews | `HANDS_ON` / `REFERENCE_ONLY` | Architecture-review exercises |
| [AWS Architecture Center](https://aws.amazon.com/architecture/) | Architecture guidance/reference patterns | discovery + selected `READ_*` | Primary discovery hub |
| [AWS Decision Guides](https://aws.amazon.com/getting-started/decision-guides/) | Structured service/option criteria | usually `READ_FULL_CONTEXTUALIZE` | High-value decision material |
| AWS Reference Architecture Diagrams | Integrated target designs | `READ_SELECTIVE_EXTRACT` + review | Pattern/context source |
| [AWS Prescriptive Guidance](https://docs.aws.amazon.com/prescriptive-guidance/) | Strategies/patterns for migration, modernization, deployment, security, data, operations | usually `READ_SELECTIVE_EXTRACT` | Major implementation/architecture source |
| [AWS Security Reference Architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/introduction.html) | Multi-account security placement/guardrails | `READ_SELECTIVE_EXTRACT` + selected full reading | Enterprise security/multi-account anchor |
| [Organizing Your AWS Environment Using Multiple Accounts](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/) | OU/account isolation/governance | `READ_FULL_CONTEXTUALIZE` candidate | Domain 1 multi-account anchor |
| **Establishing Your Cloud Foundation on AWS** | Enterprise cloud foundation | selected `READ_*` | Landing-zone/governance context |
| **AWS Fault Isolation Boundaries** | Failure containment mental model | `READ_FULL_CONTEXTUALIZE` candidate | Reliability anchor |
| [AWS Cloud Adoption Framework](https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/) | Transformation perspectives/capabilities | `READ_SELECTIVE_EXTRACT` | Migration/transformation context |
| **AWS Solutions Library** | Vetted deployable solutions | `REFERENCE_ONLY` / `HANDS_ON` | Relevant examples/implementations |
| [Amazon Builders' Library](https://aws.amazon.com/builders-library/) | Amazon engineering reasoning | `READ_SELECTIVE_EXTRACT` supplemental | Deep reasoning only; not service-behavior authority |

Architecture publications are selected by objective and decision problem, not blanket “read all whitepapers” rules.

---

# E. Service-level official documentation

Service user guides are necessary, but full-guide reading is not the default.

| Source/section type | Treatment | Why |
|---|---|---|
| Service overview/core concepts | selective; full only when foundational | Capabilities/scope/terminology |
| Architecture/design guidance | full or selective | High architecture value |
| Security/security best practices | `READ_SELECTIVE_EXTRACT` | IAM/encryption/boundaries/controls |
| Resilience/availability/DR | `READ_SELECTIVE_EXTRACT` | Failure/continuity reasoning |
| Networking/data-flow behavior | `READ_SELECTIVE_EXTRACT` | Connectivity/routing/private access |
| Scaling/performance | `READ_SELECTIVE_EXTRACT` | Decision drivers |
| Monitoring/troubleshooting | `EXTRACT_VALIDATE` or targeted selective | Operating/failure signals |
| Quotas/limits | `EXTRACT_VALIDATE` + `REFERENCE_ONLY` | Architecture constraints |
| API/SDK/CLI | `REFERENCE_ONLY` | Implementation lookup |
| How-to tutorials | `HANDS_ON` when selected | Mechanics when relevant |
| Document history/change log | `REFERENCE_ONLY` + freshness signal | Change detection |

For each unit, start from the architecture decision/problem and retrieve only relevant service sections.

---

# F. FAQs, quotas, pricing, and factual references

| Resource family | Treatment | Study role |
|---|---|---|
| AWS Product and Technical FAQs | `EXTRACT_VALIDATE` | Feature distinctions/common constraints; validate high-impact facts in canonical docs |
| Service Quotas / General Reference | `EXTRACT_VALIDATE` + `REFERENCE_ONLY` | Architecturally meaningful limits/scope/adjustability |
| AWS Pricing pages | `EXTRACT_VALIDATE` + `REFERENCE_ONLY` | Pricing models/cost drivers, not volatile-price memorization |
| AWS Pricing Calculator | `HANDS_ON` / `REFERENCE_ONLY` | Scenario cost modeling |
| Compute Optimizer / Cost Explorer / Budgets / CUR docs | selective + hands-on | Cost governance/rightsizing/visibility |
| Regional service availability | `REFERENCE_ONLY` | Use only when scenario depends on availability |

Do not create flashcards for volatile prices or low-value limits unless an exam/architecture distinction truly requires it. Teach the model and lookup method.

---

# G. Migration and modernization corpus

| Resource | Treatment | Role |
|---|---|---|
| [AWS Well-Architected Migration Lens](https://docs.aws.amazon.com/wellarchitected/latest/migration-lens/migration-lens.html) | full/selective by approved scope | Domain 4 anchor |
| Prescriptive Guidance migration strategy/patterns | selective; selected strategy full-read | Detailed migration patterns |
| AWS Cloud Adoption Framework | `READ_SELECTIVE_EXTRACT` | Transformation context |
| Migration service guides (MGN, DMS, DataSync, Migration Hub, Snow, Transfer Family, etc.) | section-level selective | Mechanics/constraints mapped to decisions |
| Reference architectures/modernization patterns | `READ_SELECTIVE_EXTRACT` | Replatform/refactor context |

---

# H. Official assessment resources

| Assessment | When to use | Control rule |
|---|---|---|
| Official Practice Question Set | Early baseline/style | Record first-attempt reasoning; memorization is not mastery |
| Exam-prep domain questions/flashcards | After relevant learning | Gap detection, not primary teaching |
| Official Practice Exam | Late readiness | Preserve first attempt |
| System-generated questions | Throughout when authorized | Must pass QA; clearly label as generated, not official AWS |

---

# I. Supplemental official AWS sources — allowed but not default curriculum

| Source | Policy |
|---|---|
| AWS Architecture Blog | Recent patterns/examples when canonical architecture/docs are insufficient; supplemental |
| AWS What's New | Freshness/change detection; follow to canonical docs before changing material |
| AWS Training & Certification Blog | Training availability/change announcements only |
| AWS re:Post / Knowledge Center | Optional troubleshooting; mixed authorship means not default authority |
| re:Invent / AWS event sessions | Optional deep-dive enrichment |
| AWS Samples / AWS-owned GitHub | Labs/reference implementations after provenance/maintenance check |

---

# J. Explicit exclusions / anti-bloat rules

The default plan does not include:

- third-party certification courses;
- exam dumps;
- blanket reading of every AWS whitepaper/service guide;
- API/CLI/SDK references as curriculum;
- all Solutions Architect Learning Plan courses end-to-end merely because AWS lists them;
- every Well-Architected lens;
- every in-scope AWS service at equal depth;
- AWS Jam Journeys (retired June 30, 2026);
- stale localized/cached pages as scope authority;
- blog posts as substitutes for canonical documentation;
- generated labs/AI notes that have not passed project QA.

---

# K. Current SAP-C02 in-scope service snapshot

Source: canonical English **In-Scope AWS Services** page, retrieved 2026-08-09. AWS states the list is non-exhaustive and subject to change. This appendix is traceability, not equal-depth curriculum.

### Analytics
Amazon Athena; AWS Data Exchange; Amazon Data Firehose; Amazon EMR; AWS Glue; Amazon Kinesis Data Streams; AWS Lake Formation; Amazon Managed Service for Apache Flink; Amazon MSK; Amazon OpenSearch Service; Amazon QuickSight.

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

# L. Required metadata for per-unit source packets

Each selected source carries at least:

- source ID and exact title;
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
- access model;
- QA state;
- conflict/freshness notes.

---

# M. Operational conclusions

1. The exam guide/task pages are syllabus authority; courses are teaching resources.
2. Well-Architected is foundational but does not replace service/decision documentation.
3. Service guides are section-selected, not read end-to-end by default.
4. Decision Guides, Prescriptive Guidance, SRA, selected whitepapers/reference architectures, and Migration Lens are central architecture-enrichment sources.
5. Hands-on mixes focused labs and integrated scenarios; Builder Labs, SimuLearn, Workshops, and Well-Architected Labs are primary candidates; Cloud Quest/Jam Events optional; Jam Journeys retired.
6. Official exam prep is an overlay/assessment layer, not the primary professional-architecture learning path.
7. Freshness is first-class because AWS scope/docs can change during study.
8. Resource selection is objective-driven; the in-scope list does not imply equal depth.

## Gate status

**Resource inventory, sequence classification, pipeline pilot, and artifact QA dependencies are complete.** The inventory remains freshness-controlled and must be rechecked where `docs/13-change-control-freshness.md` requires it. Real study remains separately frozen by `state/project-state.json`.
