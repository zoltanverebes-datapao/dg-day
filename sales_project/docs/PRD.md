# Product Requirement Document (PRD)
## Databricks ETL Pipeline for Sales & Marketing Data Processing

**Document Version**: 1.0
**Date**: 2026-02-18
**Status**: Draft

---

## 1. High-Level Business Goals & Objectives

### Why This Project?
The organization lacks proper data infrastructure to serve business intelligence and marketing automation needs. Currently:
- **Sales team** operates without accurate, aggregated sales insights needed for daily strategic planning
- **Marketing team** cannot efficiently execute targeted campaigns due to lack of customer segmentation and historical order data
- Data processing is manual, unreliable, and results in delayed decision-making

### Expected Outcomes of Successful Implementation
- Sales team gains daily access to aggregated sales metrics across time dimensions (annual, monthly, weekly, daily) and dimensions (product, category)
- Marketing team can execute email and phone-based campaigns with properly segmented customer lists including contact information and behavioral metrics
- Data pipelines are automated and reliable, removing manual processing overhead
- Data governance ensures PII protection for sales team while enabling appropriate data sharing for marketing team

### Pain Points Without This Solution
1. **Lost revenue opportunities**: Sales team cannot quickly pivot strategies based on market trends
2. **Inefficient marketing**: Marketing campaigns are not targeted, leading to poor ROI and compliance risks
3. **Manual overhead**: Data processing consumes significant operational resources with high error rates
4. **Lack of data trust**: No unified source of truth for customer and sales metrics

---

## 2. Data Sources

### 2.1 Data Entities

#### Entity: Customers
**Description**: Master data containing customer identification, contact details, and address information
**Key Fields**: customer_id (unique identifier), name, address, email, phone, state

#### Entity: Sales
**Description**: Product catalog with pricing and availability information
**Key Fields**: product_id, product_name, category, price, availability_status

#### Entity: Sales Orders
**Description**: Individual order records representing product purchases by customers
**Key Fields**: order_id, customer_id, product_id, order_date, quantity, order_status

### 2.2 Source System Characteristics

| Attribute | Details |
|-----------|---------|
| **Source System** | External systems (legacy or SaaS) that export data as CSV files |
| **Connection Method** | CSV files uploaded to Databricks Unity Catalog Volume |
| **Data Format** | CSV (comma-separated values) |
| **Ingestion Pattern** | Batch mode |
| **Update Frequency** | Infrequent and unreliable (manual trigger required) |
| **Location** | `/Volumes/zoltan-verebes-catalog-m/dg-day/volume/` |

### 2.3 Data Characteristics by Entity

#### Customers
- **Format**: CSV
- **Update Pattern**: Batch, manual trigger
- **Expected Volume**: Estimated 10K-100K records (to be confirmed)
- **Data Freshness**: Stale data expected due to manual updates

#### Sales
- **Format**: CSV
- **Update Pattern**: Batch, manual trigger
- **Expected Volume**: Estimated 1K-10K product records (to be confirmed)
- **Data Freshness**: Reference data, infrequent changes expected

#### Sales Orders
- **Format**: CSV
- **Update Pattern**: Batch, manual trigger (incremental data loads expected)
- **Expected Volume**: 100K+ orders (historical + new records, to be confirmed)
- **Data Freshness**: Daily updates expected (after implementation)

---

## 3. Use Cases

### Use Case 1: Sales Reporting with BI Tools

**Stakeholder**: Sales Team
**Short Description**: Enable sales team to access aggregated sales metrics for strategic planning and performance monitoring

**Functional Requirements**:
- Aggregate sales data by multiple time dimensions: annual, monthly, weekly, daily
- Aggregate sales data by product and product category
- Calculate key metrics: total revenue, order count, average order value
- Exclude PII data (customer names, emails, phone numbers) from this dataset
- Data must be accessible via Databricks Dashboards

**Data Access Pattern**:
- **Format**: Structured tables (SQL queryable)
- **Update Frequency**: Daily
- **Performance**: Near real-time access required (seconds to minutes)
- **Compliance**: PII-free dataset

### Use Case 2: Marketing Campaign Automation

**Stakeholder**: Marketing Team
**Short Description**: Enable marketing team to execute targeted email and phone-based campaigns through automated call center integration

**Functional Requirements**:
- Provide customer-level aggregated metrics: number of orders, total spend amount, last purchase date
- Include customer PII: name, email, phone number
- Segment customers by product categories (which products they've purchased)
- Associate each customer with appropriate timezone based on state for call center timing
- Exclude customers without email or phone contact information
- Data must be accessible via REST API for downstream call center system

**Data Access Pattern**:
- **Format**: Structured tables or REST API responses (JSON recommended)
- **Update Frequency**: Weekly
- **Performance**: Moderate (background batch processing acceptable)
- **Compliance**: PII-included dataset with restricted access controls

---

## 4. Functional Requirements

### Data Ingestion
- [ ] FR-1: Ingest customers.csv from Unity Catalog Volume into pipeline
- [ ] FR-2: Ingest sales.csv from Unity Catalog Volume into pipeline
- [ ] FR-3: Ingest sales_orders.csv from Unity Catalog Volume into pipeline
- [ ] FR-4: Support manual trigger for pipeline execution
- [ ] FR-5: Validate data integrity upon ingestion (schema validation, row count checks)

### Data Transformation & Quality
- [ ] FR-6: Merge sales orders with customer and product data
- [ ] FR-7: Aggregate sales data by time dimensions (daily, weekly, monthly, annual)
- [ ] FR-8: Aggregate sales data by product and category
- [ ] FR-9: Calculate derived metrics (revenue, order counts, average values)
- [ ] FR-10: Identify and handle data quality issues (missing values, duplicates, invalid references)
- [ ] FR-11: Apply timezone mapping based on customer state
- [ ] FR-12: Filter marketing dataset to include only customers with email or phone

### Data Access & Output
- [ ] FR-13: Create sales reporting dataset (PII-free) for BI dashboards
- [ ] FR-14: Create marketing dataset (PII-included) with customer segmentation by product category
- [ ] FR-15: Ensure data is accessible via Databricks dashboards for sales team
- [ ] FR-16: Ensure data is accessible via REST API for marketing automation system

### Data Governance
- [ ] FR-17: Implement row-level or column-level security for PII columns
- [ ] FR-18: Track data lineage from source to output datasets
- [ ] FR-19: Log all pipeline execution events

---

## 5. Non-Functional Requirements & Constraints

### Performance Requirements
- **Sales Reporting**: Query response time < 5 seconds for common aggregations (daily, monthly, annual)
- **Marketing Data**: Weekly batch processing completion within 1 hour
- **Data Pipeline**: Daily execution should complete within 30 minutes

### Data Quality & Completeness
- **Accuracy**: All aggregations must reconcile with source data
- **Completeness**: Handle NULL values and missing references gracefully
- **Consistency**: Data should be consistent across duplicate requests within the same refresh period

### Availability & Reliability
- **Uptime**: Sales reporting data must be available 99% of the time during business hours
- **Failure Handling**: Pipeline must gracefully handle source data format issues and missing files
- **Retry Logic**: Failed ingestion attempts should be retried with appropriate backoff

### Security & Compliance
- **PII Protection**: Sales team must not have access to PII columns (name, email, phone)
- **Access Control**: Marketing dataset access restricted to authorized marketing team members
- **Data Classification**: Mark datasets appropriately (Public, Internal, Confidential)
- **Audit Logging**: All data access requests should be logged

### Monitoring & Observability
- **Pipeline Monitoring**: Track pipeline execution time, success/failure status
- **Data Monitoring**: Monitor row counts, schema changes, data quality metrics
- **Alerting**: Alert on pipeline failures, significant data drift, or quality issues
- **Lineage Tracking**: Maintain data lineage from source to destination

### System Constraints
- **Catalog**: zoltan-verebes-catalog-m (Databricks Unity Catalog)
- **Schema**: dg-day (target schema for all pipeline objects)
- **Workspace**: Databricks workspace (workspace URL to be provided)
- **File Location**: `/Volumes/zoltan-verebes-catalog-m/dg-day/volume/`
- **Technology**: Databricks SQL, Delta Lake
- **Resource Limits**: (To be defined based on workspace capacity)

---

## 6. Out of Scope

The following items are explicitly excluded from this project scope:

- **Downstream System Integration**: Implementation or configuration of Databricks Dashboards
- **Marketing Automation Platform**: Setup or integration with external call center systems or email platforms
- **Data Migration**: Migration of historical data from other data warehouses
- **Advanced ML/Analytics**: Predictive modeling or machine learning applications
- **Real-time Streaming**: Event streaming pipelines (batch processing only in Phase 1)
- **Custom Connectors**: Development of custom data connectors beyond Databricks native capabilities
- **Infrastructure Setup**: Databricks workspace creation or configuration (assumes workspace exists)

---

## 7. Open Questions & Clarifications Needed

- [ ] **Data Volumes**: What are the exact record counts and data sizes for each entity?
- [ ] **Update Strategy**: Should incremental loads (CDC) be implemented, or is full refresh acceptable?
- [ ] **Historical Data**: Do we need to preserve historical snapshots of aggregated data?
- [ ] **Timezone Mapping**: What is the complete state-to-timezone mapping? Should we use standard US timezones?
- [ ] **Workspace URL**: What is the Databricks workspace URL for this project?
- [ ] **Client Configuration**: What are the Databricks authentication credentials and workspace client ID?
- [ ] **Error Handling**: How should the pipeline handle malformed CSV records (skip, quarantine, fail)?
- [ ] **Schedule**: Once automated, what should be the exact schedule for daily/weekly pipeline runs?
- [ ] **SLA**: What are the agreed Service Level Agreements for data availability and freshness?
- [ ] **Cost Constraints**: Are there any compute cost limitations or budget constraints?
- [ ] **Metadata**: Are there data dictionaries or technical specifications for source CSV files?
- [ ] **Retention Policy**: How long should historical data be retained in the data lake?

---

## Document History

| Date | Version | Author | Changes |
|------|---------|--------|---------|
| 2026-02-18 | 1.0 | AI Assistant | Initial PRD document |
