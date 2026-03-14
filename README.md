# Aurora Forecasting & Astrophotographer Intelligence Platform

## Overview
This project builds a real-time aurora forecasting system that combines space weather telemetry, meteorological data, and astronomical conditions to determine whether auroras are visible from a specific location.

## Features
- Real-time solar wind monitoring
- OVATION aurora probability visualization
- Hyper-local aurora visibility scoring
- Alert system for aurora visibility
- Interactive map interface

## Tech Stack
Frontend: React + Mapbox  
Backend: Python FastAPI  
Data Sources: NOAA SWPC, Open-Meteo

## Architecture
Data Pipeline → Visibility Score Engine → API → Frontend Map Interface

## Repository Structure
frontend/        → UI and map visualization
backend/         → API and visibility score engine
data_pipeline/   → NOAA data ingestion
docs/            → project documentation


## Status
Initial development phase.
