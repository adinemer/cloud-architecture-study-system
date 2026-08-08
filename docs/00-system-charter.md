# Study System Charter

Status: **DRAFT**  
System version: `0.1`  
Pilot certification: **AWS Certified Solutions Architect – Professional (SAP-C02)**  
Study state: **NOT STARTED**

## Purpose

Design, validate, and operate a controlled AI-assisted study system that has two equal outcomes:

1. Pass the target cloud certification exam.
2. Improve professional cloud-architecture knowledge, decision-making, and hands-on capability.

## Source-of-truth hierarchy

1. Current official certification exam guide and objective definitions.
2. Current official provider architecture guidance and documentation.
3. Approved repository specifications and source inventory.
4. Approved study artifacts generated from those sources.
5. Model background knowledge only when explicitly identified as supplementary and never as a substitute for an authoritative source.

## Core operating rules

- No certification study begins until the study structure and extraction pipeline are approved.
- Official provider material is authoritative.
- Third-party certification courses are excluded from the default study curriculum.
- AI must distinguish provider facts, provider recommendations, cross-source synthesis, architectural inference, and exam interpretation.
- AI-generated material is unapproved until it passes the applicable QA gates.
- Human reading is concentrated on reasoning-heavy material; repetitive factual/reference material should be compressed when reliable.
- The first pipeline must be simple to build, inspect, test, and modify.
- Open-source Fedora-compatible tooling is preferred when it offers comparable quality and lower operational burden.
- Additional infrastructure (RAG, vector DBs, agent frameworks, custom applications) is added only after a measured need is demonstrated.
- Study sequence is controlled by the approved curriculum and prerequisite model, not by conversational drift.

## ChatGPT roles

ChatGPT may act as:

- coordinator;
- study partner;
- instructor;
- documentation analyst;
- architecture mentor;
- assessor.

Each role operates under repository specifications rather than improvising a new process per session.

## Completion gate for planning phase

Certification study may start only when all of the following are approved:

- official resource inventory;
- resource classification and read/extract/reference/lab policy;
- study sequence;
- ChatGPT operating specification;
- extraction and architectural-enrichment pipeline;
- study-artifact schemas;
- provenance and QA rules;
- mastery/progress model;
- toolchain;
- representative extraction-pipeline pilot with documented results.

## Change control

Material changes to the certification blueprint, source policy, extraction schema, QA policy, or study sequence require a repository change and version increment before they become operational.
