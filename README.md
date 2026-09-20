# Lab Fabric

Lab Fabric is a local-first event processing pipeline.

## Current MVP

The initial pipeline contains:

- Go ingester
- Python anomaly detector
- Automated tests

## Pipeline

JSON/syslog input → Go ingester → detector → anomaly output

## Development status

The project is currently in MVP construction and validation.

Performance claims will only be published after they are measured and reproduced.

## No telemetry

The intended architecture is local-first. No telemetry or external reporting is part of the MVP.
