# Portal submission
## Project name
SLAJURY
## One-line summary
Independent validators turn official outage and SLA evidence into challengeable on-chain service-credit receipts.
## Description (under 1000 characters)
SLAJURY turns service-outage evidence into challengeable SLA credit receipts. A claimant selects a service, tier, region and billing month, then submits the provider’s official incident page and customer monitoring evidence. GenLayer validators independently refetch sources and classify scope match, customer impact, exclusions and qualifying downtime. Decision fields must match; durations may differ by five minutes but must produce the same credit band. The contract deterministically calculates monthly uptime and credit percentage, rejecting inconsistent outputs. Eligible and partial claims receive an on-chain recommendation; missing or conflicting evidence fails closed to INSUFFICIENT_EVIDENCE. Versioned records, bounded state transitions, URL controls and prompt-injection isolation make it reusable across cloud and SaaS contracts. It recommends eligibility; it neither binds providers nor transfers funds.
## Suggested tags
Infrastructure · Oracle · Developer Tools
