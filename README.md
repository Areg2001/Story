# Database Schema and Pipeline Documentation

## Overview

This document explains the structure of the database schema used for recording user metrics and provides guidelines for maintaining and extending the data ingestion pipeline.

## Database Schema

### user_metrics Table

The `user_metrics` table is the central table that records each metric entry with a unique ID. It captures common fields applicable to all metric types.

**Columns:**
- **id**: Unique identifier for each metric entry.
- **timestamp**: Date and time when the metric was recorded.
- **user_id**: Identifier for the user associated with the metric.
- **session_id**: Identifier for the session in which the metric was recorded.
- **metric_type**: Type of metric (e.g., talked_time, microphone_used, etc.).

### talked_time Table

The `talked_time` table stores detailed information about the duration of talking sessions.

**Columns:**
- **id**: Unique identifier for each talked time record.
- **user_metric_id**: Foreign key referencing `user_metrics.id`, linking the talked time to a specific metric record.
- **duration**: Duration of the talking session.

### microphone_used Table

The `microphone_used` table records information about microphone usage, including its status and volume level.

**Columns:**
- **id**: Unique identifier for each microphone usage record.
- **user_metric_id**: Foreign key referencing `user_metrics.id`.
- **status**: Indicates whether the microphone was on or off.
- **volume_level**: Volume level when the microphone was in use.

### speaker_used Table

The `speaker_used` table tracks details about speaker usage similar to the microphone usage table.

**Columns:**
- **id**: Unique identifier for each speaker usage record.
- **user_metric_id**: Foreign key referencing `user_metrics.id`.
- **status**: Indicates whether the speaker was on or off.
- **volume_level**: Volume level when the speaker was in use.

### voice_sentiment Table

The `voice_sentiment` table captures sentiment analysis of the user's voice, providing insights into emotional tone.

**Columns:**
- **id**: Unique identifier for each sentiment record.
- **user_metric_id**: Foreign key referencing `user_metrics.id`.
- **sentiment_score**: Numerical score representing the sentiment of the voice.
- **confidence_level**: Confidence in the sentiment score provided.

## Guidelines for Maintaining and Extending the Pipeline

### Maintenance Guidelines

- Regularly verify that foreign key constraints are correctly enforced to maintain referential integrity between tables.
- Ensure appropriate security measures are in place.
- Plan for scaling the database if data volume increases significantly.

### Extending the Pipeline

- **Create New Tables**: Add new tables for each new type of metric.
- **Add New Fields**: Modify existing tables to include new fields as needed for additional metrics.
- **Update Relationships**: Adjust foreign key relationships if new tables are introduced.
- **Testing**: Thoroughly test the pipeline with new metrics to ensure correct data ingestion and processing.

### Potential Limitations

- Extremely high data volumes or very high query loads may require additional performance tuning or database scaling strategies.
- The use of multiple tables and foreign key relationships can introduce complexity in queries and data management.

## Suggestions for Future Improvements

- Regularly review and optimize indices based on query performance and usage patterns.
- Consider integrating real-time analytics tools if real-time processing and reporting are needed.
- Keep the documentation updated with any changes to the schema or pipeline to ensure clarity for future developers and maintainers.

## Assumptions

- The schema is designed for moderate to high data volumes. Very high data volumes may necessitate additional performance optimizations.
- Data entering the pipeline is assumed to be clean and conform to expected formats, including valid timestamps, user IDs, and metric values.
- Data consistency is assumed, following the expected format.

## Validation

- Basic validation of data types and constraints is performed to ensure data integrity.

