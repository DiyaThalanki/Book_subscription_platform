#!/bin/bash
set -e  # Stop on any error

echo "Running unit tests..."
pytest tests -m "unit"

echo "Running integration tests..."
pytest tests -m "integration"


