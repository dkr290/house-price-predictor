from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from inference import batch_predict, predict_price
from schemas import HousePredictionRequest, PredictionResponse


def create_app(version: str, title_suffix: str = "") -> FastAPI:
    """Factory function to create versioned FastAPI apps"""
    app = FastAPI(
        title=f"House Price Prediction API{title_suffix}",
        description=(
            "An API for predicting house prices based on various features. "
            "This application is part of the MLOps Bootcamp by School of Devops. "
            "Authored by Gourav Shah."
        ),
        version=version,
        contact={
            "name": "School of Devops",
            "url": "https://schoolofdevops.com",
            "email": "learn@schoolofdevops.com",
        },
        license_info={
            "name": "Apache 2.0",
            "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
        },
    )

    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Health check endpoint
    @app.get("/health", response_model=dict)
    async def health_check():
        return {"status": "healthy", "model_loaded": True}

    # Prediction endpoint
    @app.post("/predict", response_model=PredictionResponse)
    async def predict(request: HousePredictionRequest):
        return predict_price(request)

    # Batch prediction endpoint
    @app.post("/batch-predict", response_model=list)
    async def batch_predict_endpoint(requests: list[HousePredictionRequest]):
        return batch_predict(requests)

    return app


# Create main app
main_app = FastAPI()

# Create and mount versioned apps
v1_app = create_app("v1", " v1")
latest_app = create_app("latest", " Latest")

main_app.mount("/v1", v1_app)
main_app.mount("/latest", latest_app)


# Root endpoint
@main_app.get("/")
async def root():
    return {"message": "Use /v1 or /latest endpoints"}


app = main_app
