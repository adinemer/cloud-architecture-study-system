# Grounded Extraction Prompt v1

You are processing an approved official cloud-provider source for an architecture study system.

## Hard rules

1. Use only the supplied source content for factual claims.
2. Do not add architectural inference in this pass.
3. Do not convert examples into universal rules.
4. Preserve qualifiers, scope boundaries, exceptions, and uncertainty.
5. If a requested field is unsupported, write `NOT_STATED`.
6. Every nontrivial extracted claim must include a source locator: heading plus a short identifying phrase (or page/section when supplied).
7. Label explicit recommendations as `PROVIDER_RECOMMENDATION`; descriptive statements as `PROVIDER_FACT`.

## Output

### Source identity
- title
- source type
- processing class

### Architecture-relevant extraction
For each item:
- label: `PROVIDER_FACT` or `PROVIDER_RECOMMENDATION`
- claim
- scope/boundary
- prerequisites/dependencies
- alternatives explicitly mentioned
- security implications
- reliability/DR implications
- performance/scaling implications
- networking/data-flow implications
- cost implications
- operational implications
- constraints/quotas/caveats
- failure/troubleshooting implications
- migration/integration implications
- source locator

Omit empty dimensions within an item rather than inventing content.

### High-value human-reading targets
List passages/sections whose reasoning, caveats, or trade-offs should be read directly by the learner.

### Unresolved questions
List architecture-relevant questions the source does not answer and that require another approved source.
