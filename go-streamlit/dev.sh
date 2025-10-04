#!/bin/bash

# Development runner for House Price Predictor

echo "🔧 Development Mode - House Price Predictor"
echo "=========================================="

# Check if Go is installed
if ! command -v go &> /dev/null; then
    echo "❌ Go is not installed. Please install Go 1.21 or later."
    exit 1
fi

echo "📦 Installing dependencies..."
go mod tidy

echo "🚀 Starting development server with auto-reload..."
echo "   Access the application at: http://localhost:8080"
echo "   Press Ctrl+C to stop the server"
echo ""

# Install air for hot reload if not present
if ! command -v air &> /dev/null; then
    echo "📥 Installing air for hot reload..."
    curl -sSfL https://raw.githubusercontent.com/cosmtrek/air/master/install.sh | sh -s -- -b $(go env GOPATH)/bin
fi

# Run with air for hot reload
air