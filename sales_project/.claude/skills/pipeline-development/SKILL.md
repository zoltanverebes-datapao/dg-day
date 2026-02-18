---
name: pipeline-development
description: Orchestrates Databricks ETL Pipeline Development process. Use this skill to find out sub-tasks, steps, phases to implement a new pipeline end-to-end.
---

Follow the phases of pipeline development to deliver a standard ETL pipeline in Databricks. There is human in the loop between each phases. The developer needs to verify and extend the actual output before steppig into the next phase.
Each phases use additional claude skills to do the job. Aim to find the corresponding ones of them.

- The primary format of any document is markdown
- The primary location of any document is the */docs* directory

# Phase 1 - Capture Pipeline Requirements

**The Primary Goal**:  Write a high level document to describe the actual business goals, Functional and non-functional requirements to achieve.
    - Capture data sources without analyzing them
    - Capture primary business usages of the processed data

**Exptected Output**: Write a Product Requirement Document (prd) file. Find appropiate skills that describes the structure and the content of the file.

**Skills**: capture-pipeline-requirements

# Phase 2 - Technical Design

**Primary Goal**: Write a technical docuemnt as part of the planning of the project. This is not an implementation task! Use the already captured requirements as input.
    - Capture technical requirements of the ETL pipeline
    - Understand data ingestion and transformations
    - Use Databricks best practicies, i.e.: Medalion Architecture, Lakeflow Connect, etc
    - Document Catalog objects to be created (tables, views, functions, schema, etc)
    - Cover Data Governance related topics (non-functional requirements)

**Expected Output**: Write a Technical Design Document (TDD) file. Find the appropiate skills to get the best resoult of the above mentioned topics

**Skills**: technical-design-document-writer

# Phase 3 - Implementation

**Primary Goal**: Implement the pipeline based on the technical documentation. This is the implementation task!
**Expected Output**: it is a working solution for the required functions documented bu the Product Requirement Document. Use the technical documentation to (Technical Design Document) as the primary source for implementation details.

Split the work into subtasks and find appropiate, bite-size pieces to iterate over the components of the implementation.

**Skills**: pipeline-implementation

# Phase 4 - Documentation (WIP)

**Primary Goal**: Technical details of implementation needs to be document. It is the input for future feature development and developers.
**Expected Output**: a set of documentation of the pipeline
    - high level architecture of data flow
    - catalog(s), schema(s), unity catalog objects with short description

**Skills**: pipeline-documentation


# Project Tracking

The primary goal of the project tracking file is to provide a starting point to build AI context of an existing or ongoing project. The development process has human-in-the-loop between and during phases of the described process. The project tracking file helps to initialize an empty context for the AI. When there is an empty context start by reading (and validating) the project tracking file to pickup context for the upcoming development phases.

**Project tracking file**: ./project.md
***IMPORTANT!*** Create track record when the developer explicitly say to do so espcially when a development is is finished or a document has been updated.

If the file does not exists, create one.
When creating a file, consider looking into the already existing documents and git history to figure out changes and timestamps of the records.

Make sure to track consice changes: one record per one action.

Example track records:

```
2026-02-18: Product documenttion created: ./docs/PRD_.....md
2026-23-19: Technical documentation updated: ./docs...
```