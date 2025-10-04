#!/bin/bash

# House Price Predictor - Go Application Runner

echo "🏠 House Price Predictor - Go Version"
echo "===================================="

# Check if Go is installed
if ! command -v go &> /dev/null; then
    echo "❌ Go is not installed. Please install Go 1.21 or later."
    echo "   Download from: https://golang.org/dl/"
    exit 1
fi

# Check Go version
GO_VERSION=$(go version | awk '{print $3}' | sed 's/go//')
REQUIRED_VERSION="1.21"

if [ "$(printf '%s\n' "$REQUIRED_VERSION" "$GO_VERSION" | sort -V | head -n1)" != "$REQUIRED_VERSION" ]; then
    echo "⚠️  Go version $GO_VERSION detected. Recommended: Go $REQUIRED_VERSION or later."
fi

echo "📦 Installing dependencies..."
go mod tidy

echo "🔧 Building application..."
go build -o house-price-predictor .

echo "🚀 Starting server..."
echo "   Access the application at: http://localhost:8080"
echo "   Press Ctrl+C to stop the server"
echo ""

# Run the application
./house-price-predictor