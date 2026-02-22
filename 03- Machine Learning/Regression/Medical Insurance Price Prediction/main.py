from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.security import APIKeyHeader
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

from utils.InsuranceInput import InsuranceInput
from utils.inference import predict_insurance_charges
from utils.config import forest_model, APP_NAME, VERSION, SECRET_KEY_TOKEN

# ===============================
# Initialize App
# ===============================
app = FastAPI(
    title=APP_NAME,
    version=VERSION
)

# ===============================
# Templates
# ===============================
templates = Jinja2Templates(directory="templates")

# ===============================
# CORS Middleware
# ===============================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ===============================
# API KEY SECURITY
# ===============================
api_key_header = APIKeyHeader(name="X-API-Key")

async def verify_api_key(api_key: str = Depends(api_key_header)):
    if api_key != SECRET_KEY_TOKEN:
        raise HTTPException(
            status_code=403,
            detail="You are not authorized to use this API"
        )
    return api_key

# ===============================
# Home Page (HTML Form)
# ===============================
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "prediction": None})

# ===============================
# Form Submission Endpoint
# ===============================
@app.post("/predict/form", response_class=HTMLResponse)
async def predict_form(request: Request):
    form = await request.form()
    try:
       
        input_data = InsuranceInput(
            age=int(form.get("age")),
            sex=form.get("sex"),
            bmi=float(form.get("bmi")),
            children=int(form.get("children")),
            smoker=form.get("smoker"),
            region=form.get("region")
        )

        prediction = predict_insurance_charges(input_data)

        return templates.TemplateResponse(
            "index.html",
            {"request": request, "prediction": prediction}
        )
    except Exception as e:
        return templates.TemplateResponse(
            "index.html",
            {"request": request, "prediction": f"Error: {str(e)}"}
        )

# ===============================
# API Endpoint for JSON Requests
# ===============================
@app.post("/predict/forest", tags=["Models"])
async def predict_forest(
    data: InsuranceInput,
    api_key: str = Depends(verify_api_key)
):
    try:
        result = predict_insurance_charges(data)
        return {"predicted_charges": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
