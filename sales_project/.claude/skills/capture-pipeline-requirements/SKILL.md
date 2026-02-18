---
name: capture-pipeline-requirements
description: This is an ETL Pipeline Requirement Specification Framework. The skill supports capturing the functional and non-functional requirements of a Databricks ETL Pipeline.
---

You are an expert of understanding and document high level requirements of an ETL Pipeline. Get the necessary input of the project to fill up the following strucutre with relevant content. Make sure to discuss each topic.

**Outcome**: Product Requirement Document (prd) written as an md file into the */docs* folder.

***IMPORTANT***: This is not an implementation task! The expected output is a markdown file!

***Out of scope***: Technical and implementation details. They will be part of the technical documentation written in upcoming phases of the planning.

The product document contains the following sections to set the scope of the project:

# High level business goals & objectives

Understand the "why"s behind the project.
- What are the expected outcome of a successful implementation. 
- What are the main reasons to do it
- What are the pain-points without this solution

# Data Sources

Collect basic things to know about the data sources.
The following characteristics of the data can be different per entity. Make sure to capture the information for all of the main entities!

- Main entities - have a short description of each - details will be unpacked in the architecture/design documents
- **Source System**: where is the data coming from. Is it an external system like a SaaS tool or external database or static files arrive into a storage
- **Connection to Source System**: How Databricks can connect to the source system
- **Data Format**: The original format of the ingested data.
    -- Raw data format like csv, json, Parquet etc
    -- Event based streaming system like a Kafka, Pub/Sub, Kinesis
    -- External tool like Snowflake or an SQL database
- **Ingestion Pattern:**
    -- Batch or Incremental
    -- Streraming or Schedudled.
    -- Data Update Frquency: one time, continues, periodic (dayly, weekly, monthly, etc)
- **Volume Size**: size of the data in terms of number of records or data size.
    -- Get the information by entity type
    -- total size or over a period (in case of incremental data)
- **Location of data**: it depends on the source system

# Use Cases

Find use cases to be implemented once the high quality, cleaned and governed data can be accessed by downstream tools. The purpose to collect use cases is to undertstand the required output schema of the ETL pipeline. 

- Who should have access to what data
- What is the format the data needs to be served to sink/consumer systems
- What is the required data update frequency
- Get a short name and description of the system

# Functional Requirements

Capture functional requirements in a structural format. They are just summaries of them.

# Non-Functional Requirements & Constraints

Capture any alreday known NFRs.
For example:
- Expected Data Quaility,
- Performance,
- Availablity,
- Security and permissions,
- Monitoring - Data and pipeline

Constraints of the current system. For example:
- Databricks Unity Catalog or workspaces to be used
- External systems and connections
- Resource or budget limits

# Out of scope

This to be explicitly excluded from the productproject

# Open questions

Document any open questions that is not answered in this phase of the project, but needs to be clearified later
