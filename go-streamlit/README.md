# House Price Predictor - Go Version

A Go web application that replicates the Streamlit house price prediction application using Bootstrap for the UI.

## Features

- **Responsive Design**: Built with Bootstrap 5 for mobile-friendly interface
- **Real-time Prediction**: Connects to ML model API for house price predictions
- **Modern UI**: Clean, professional design with smooth animations
- **Error Handling**: Graceful fallback to mock data when API is unavailable
- **Session Management**: Maintains form state and prediction results

## Architecture

- **Backend**: Go with Gin web framework
- **Frontend**: HTML templates with Bootstrap 5
- **Styling**: Custom CSS with Bootstrap theming
- **API Integration**: RESTful API calls to ML model service

## Project Structure

```
go-streamlit/
├── main.go                 # Main Go application
├── go.mod                  # Go module dependencies
├── Dockerfile              # Container build configuration
├── templates/
│   └── index.html          # HTML template with Bootstrap
├── static/
│   └── css/
│       └── style.css       # Custom CSS styling
└── README.md
```

## Environment Variables

- `PORT`: Server port (default: 8080)
- `APP_VERSION`: Application version (default: 1.0.0)
- `API_URL`: ML model API endpoint (default: http://model:8000)

## Getting Started

### Prerequisites

- Go 1.21 or later
- Docker (optional, for containerized deployment)

### Local Development

1. **Clone and navigate to the project:**
   ```bash
   cd go-streamlit
   ```

2. **Install dependencies:**
   ```bash
   go mod tidy
   ```

3. **Run the application:**
   ```bash
   go run main.go
   ```

4. **Access the application:**
   Open http://localhost:8080 in your browser

### Docker Deployment

1. **Build the Docker image:**
   ```bash
   docker build -t house-price-predictor-go .
   ```

2. **Run the container:**
   ```bash
   docker run -p 8080:8080 -e API_URL=http://your-model-api:8000 house-price-predictor-go
   ```

## API Endpoints

- `GET /` - Main application page
- `POST /predict` - Submit house data and get price prediction

## Form Fields

- **Square Footage**: Range slider (500-5000 sq ft)
- **Bedrooms**: Dropdown (1-6)
- **Bathrooms**: Dropdown (1, 1.5, 2, 2.5, 3, 3.5, 4)
- **Location**: Dropdown (Urban, Suburban, Rural, Waterfront, Mountain)
- **Year Built**: Range slider (1900-2025)

## Comparison with Streamlit Version

| Feature | Streamlit Version | Go Version |
|---------|------------------|------------|
| Framework | Streamlit (Python) | Go + Gin + Bootstrap |
| UI Components | Streamlit widgets | HTML forms + Bootstrap |
| Styling | Streamlit themes + CSS | Bootstrap 5 + Custom CSS |
| Session State | Streamlit session state | Form persistence |
| API Integration | Python requests | Go net/http |
| Deployment | Streamlit Cloud/Container | Container/Any Go hosting |

## Benefits of Go Version

- **Performance**: Compiled language with better performance
- **Resource Efficiency**: Lower memory footprint
- **Deployment Flexibility**: Single binary deployment
- **Type Safety**: Strongly typed language
- **Concurrency**: Built-in concurrency support

## License

Built for MLOps Bootcamp by [School of Devops](https://www.schoolofdevops.com)