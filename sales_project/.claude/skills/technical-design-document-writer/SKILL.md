---
name: technical-design-document-writer
description: This is an ETL Pipeline Technical Specification and Documentation Framework. The skill supports documenting technical details of an ETL Pipeline implementation. It captures information about data ingestion, bronze, silver and gold layer schema design, architectural and deployment in Databricks.
---

You are an expert to write a Technical Design Document (TDD) of an ETL pipeline. There is already available information from the PRD (Product Requirement Document) and from project source.

**Outcome**: The output is a Technical Design Document (tdd) written as and md file into the */docs* folder.

***IMPORTANT***: This is not an implementation task! The expected output is a markdown file!

***Out of scope**: Implementation of the pipeline and architectures

**Skills**: ./medallion-arcitecture/**

# General Instructions

- This is intended to use Databricks Pipeline development with Delta Live Tables (DLTs)
- Find Databricks specific skills and best practicies to design the pipeline
- Consider the PRD documentation
- Use the Medallion Architecture (Bronze, Silver, Gold tables) to design the pipeline
- Use Databricks terminology

**Diagrams**: Use inline marmaide notion - Markdown tools can display them

The document contains the following sections:

# Architecture Overview

Create an architecture overview diagram containing details of the layers of the Medallion Architecture including the source layer. (Source, Bronze, Silver, Gold, Downstream tools)

Show small details of the source files, source systems and tables

## Unity Catalog Structure

Document workspace and catalog structure to be used. Have a clear naming and follow best practicies for each layer.

**Skills**: Look for skills to implement state-of-the-art Databricks solution

## Data Flow Summary

Summarize the task and purpuse of each layer. Take into account project and use-case specific details documented in the PRD document.

# Data Source

Document the source system or source files of the system. Be precise!

1. Identify entity sources and the locations of the sources
2. Document characteristics of each entity - size, volume, number of records
3. Document the schema or structure of the source
- take sample data to analyze and infer attributes and types
- take sample data to what is nullable and what is not
- take sample data to assume contraints (about numbers or lenght of texts)
- write sample data into the TDD document for later reuse
4. Identify Keys and Primary Keys of possible
5. Create a table to document each property of the raw source
6. Classify the attributes PII or Non-PII

Use appropiate scripts and tools to take sample data of the provided source. Document the following details for each id

**Output**
1. Attribute documentation
2. Documentation code block to read the source (pyspark DataFrame API or SQL)
- schema definition
- sample to read the source

# Unity Catalog Object Defintions

## Naming Convention

**Pattern:** `{layer}_{domain}_{type}`

Where:
- **layer:** bronze | silver | gold
- **domain:** customers | products | sales_orders | customer | product | order_status
- **type:** raw | fact | summary | performance (optional)

**Examples:**
- `bronze_customers_raw` - Bronze layer raw customer data
- `silver_customers` - Silver layer cleaned customer dimension
- `gold_sales_orders_fact` - Gold layer denormalized sales order fact table
- `gold_customer_summary` - Gold layer customer aggregation

**Standards:**
- Use lowercase with underscores (snake_case)
- No abbreviations unless industry-standard (e.g., "id", "pii")
- Descriptive names that indicate content and purpose
- Layer prefix for clear separation

## Table documentation

List all of the bronze tables to be created. Documuemnt the following properties of each:
- Name
- Type: Managed vs External
- Location if external
- Purpose (Example: Stores raw data from a specific source + metadata)
- Retention

All tables will include:
- **Comment:** Human-readable description of table purpose
- **Column Comments:** Description of each column's meaning and constraints
- **Properties:** Key-value metadata for governance and discovery
- **Tags:** Classification tags (e.g., PII, Confidential, Public)

Create a sub section for each layer (bronze, silver and gold)


# Medallion Architecture Implementation

***IMPORTANT*** This is still a documentation and not an implementation task

This section contains a list of implementation tasks. It is expected to contain a lot of example codes, table defintions, data transformation and business logic implementation examples as SQL or Python (PySpark) code.

- Document the purpose of each task
- Name the scripts to be implemented! (with location)
- Find an appropiate structure of the source code structure

## Data Cleaning

Document expectations, default values, etc to build the silver layer

## Aggregation

Use the input use-case to design the gold layer for each documented use-cases.

## JOIN stragegy and performance

Consider expected data volume of accessed tables and define the appropiate JOIN startegies. Consider best practicies of using them.

Split the documentation to logical layers of the architcture.

## Unity Catalog Objects

Consider using tables, views, temporary views, materialized views accordingly to the Databricks Best practicies


# Data Governance & Security

## Access Control

- Identify PII: audit and masking
- Retention

Document implementation hints to GRANT and REVOKE permissions

# Deployment Architecture & Process

## Execution Mode

Continuoues or on-demand

## Compute Resources

Serverless, Job Cluster, All porpuse

## Target Envirnments

Production, Staging, Development

## CI/CD integration

## Infrastructure-as-a-Code

Document to use Databricks Asset Bundels (DAB) or different way to deploy the application.

## Monitoring and Notifications

## Tools

- Manual deployment example codes for local dev env
- CI/CD deployment documentation

# Databricks Enviornment

Ask and document explicitly for the workspace URL and the client ID of the Databricks environment.
Ask if the same URL/ClientId is used for the target envs (prod,stage,dev).

It is required to setup proper databricks.yml in the next step
