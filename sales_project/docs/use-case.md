# Description

Customer and Sales data needs to be processed to enable business value that is unavailable today.
- Sales team has no accurate access to aggregated information to create good business strategy. They need more input on daily bases
- Marketing team could accelarate their marketing campaigns via external tools. It is a prerequirement to provide customer information with aggregated, historical order data.

The goal of this project is to build a Databricks pipeline to process available data and provide business case specific data tables for underlying teams.

# Data Sources

External systems serve the following entities in CSV format. The data update is infrequent, unreliable and manual. The processing data pipeline needs to be triggered manually.

Entities

- customers.csv
Customer master data. Information available like name, address, email, phone associated with a uniqe customer_id. Customer_id is used to reference the customers by other entities

- sales.csv
Product, pricing and product availability information. 

- sales_orders.csv
Status of the an individual order of products by a customer

## Location of the data

The latest version of the CSV sources are uploaded into a Databricks Unity Catalog Volume:
'/Volumes/zoltan-verebes-catalog-m/dg-day/volume/'

# Databricks Catalog and Workspace

**Target Catalog**: zoltan-verebes-catalog-m
**Target Schema**:  dg-day

**Workspace**: 

# Business Goals

1. **Use Case 1 - Sales reporting with BI tools**: 

Sales team needs access to aggregated data. it needs to support annual, monthly, weekly and daily aggregation of sales per product and per product categories.

Sales team have no access to PII data like names, email addresses, phone numbers.

**Downstream**: Databricks Dashboards
**Update frequency**: Daily
**Performance**: Sales team needs prompt access to aggregated data.


2. **Use Case 2 - Marketing Team**

Marketing team would like to implement a direct email and phone marketing campaign. 
They need access to customer names, email addresses and phone numbers per product category. They want to create clusters of the customers by products and product categories. They need aggregated data of number of orders, spent amount, last purchase per customer joint with their name, email and phone numbers.

Each customer needs to be associated with a timezone, so call center makes calls in business hours. Use the available state information to identify the appropiate timezone.

Any customer provided to the marketing team needs to have a phone number or email address. Others need to be dropped.

**Downstream**: External, automated call center - Rest API
**Update Frequency**: Weekly
**Performance**: Modarate


# Out of Scope

The project is not intended to implement any of the downstream tools or connection to the downstream tools. The expected outcome is a set of data tables containing high-quality, accessable data that provides access to the sales and marketing teams with the necessary permissions.