# Project Tracking: Databricks ETL Pipeline for Sales & Marketing

**Project**: Sales & Marketing Data Processing ETL Pipeline
**Target Workspace**: zoltan-verebes-catalog-m / dg-day schema
**Status**: In Progress

---

## Development Phases

### Phase 1: Capture Pipeline Requirements ✅ COMPLETED
- **Objective**: Define business goals, data sources, and functional/non-functional requirements
- **Completion Date**: 2026-02-18
- **Output**: Product Requirement Document (PRD)

**Activities Completed**:
- [x] Analyzed use case specification from docs/use-case.md
- [x] Captured high-level business goals and pain points
- [x] Documented data sources and their characteristics
- [x] Identified two primary use cases: Sales Reporting and Marketing Campaign Automation
- [x] Defined functional requirements (19 items)
- [x] Defined non-functional requirements (performance, quality, security, monitoring)
- [x] Documented system constraints and out-of-scope items
- [x] Listed open questions for clarification

**Deliverable**: ./docs/PRD.md

---

### Phase 2: Technical Design (PENDING)
- **Objective**: Design technical architecture, data schemas, and implementation approach
- **Expected Deliverable**: Technical Design Document (TDD)
- **Skills**: technical-design-document-writer

**Key Activities**:
- [ ] Review and validate PRD with stakeholders
- [ ] Answer open questions from Phase 1
- [ ] Design medallion architecture (bronze, silver, gold layers)
- [ ] Define table schemas for each layer
- [ ] Document data governance and security implementation
- [ ] Plan data transformation logic

---

### Phase 3: Implementation (PENDING)
- **Objective**: Implement the ETL pipeline based on technical documentation
- **Expected Deliverable**: Working Databricks SQL pipeline
- **Skills**: pipeline-implementation

**Key Activities**:
- [ ] Implement bronze layer (raw data ingestion)
- [ ] Implement silver layer (data cleansing and integration)
- [ ] Implement gold layer (business aggregations)
- [ ] Create security and access control
- [ ] Implement pipeline orchestration and error handling
- [ ] Write tests and validation logic

---

### Phase 4: Documentation (PENDING)
- **Objective**: Document pipeline architecture, objects, and operational procedures
- **Expected Deliverable**: Pipeline Operations & Architecture Documentation
- **Skills**: pipeline-documentation

**Key Activities**:
- [ ] Document data flow and architecture
- [ ] Create catalog and schema documentation
- [ ] Document table ownership and lineage
- [ ] Create operational runbooks

---

## Key Milestones

| Date | Milestone | Status |
|------|-----------|--------|
| 2026-02-18 | PRD document created | ✅ Complete |
| TBD | PRD validated with stakeholders | Pending |
| TBD | Technical Design Document completed | Pending |
| TBD | Phase 3 Implementation started | Pending |
| TBD | Phase 4 Documentation completed | Pending |
| TBD | Pipeline production deployment | Pending |

---

## Recent Updates

- **2026-02-18**: Product Requirement Document created: ./docs/PRD.md

---

## Configuration & Context

**Databricks Connection Details**:
- Workspace URL: (TBD)
- Workspace Client ID: (TBD)
- Target Catalog: zoltan-verebes-catalog-m
- Target Schema: dg-day
- Data Location: `/Volumes/zoltan-verebes-catalog-m/dg-day/volume/`

**Source Files**:
- customers.csv
- sales.csv
- sales_orders.csv

**Downstream Systems**:
- Sales Reporting: Databricks Dashboards
- Marketing Automation: External REST API

---

## Notes

- This is a phased development approach with human-in-the-loop validation between each phase
- Each phase builds upon the previous deliverables
- Open questions from PRD must be addressed before proceeding to Phase 2
