import pandas as pd
import numpy as np
from .InsuranceInput import InsuranceInput
from .config import forest_model

# Case-insensitive mapping
smoker_map = {'yes': 1, 'no': 0}
sex_map = {'male': 0, 'female': 1}
region_map = {'northwest': 0, 'northeast': 1, 'southeast': 2, 'southwest': 3}

def predict_insurance_charges(input_data: InsuranceInput):
    print("\n" + "=" * 60)
    print("📥 RECEIVED INPUT:")
    print(f"   Age: {input_data.age}")
    print(f"   Sex: {input_data.sex}")
    print(f"   BMI: {input_data.bmi}")
    print(f"   Children: {input_data.children}")
    print(f"   Smoker: {input_data.smoker}")
    print(f"   Region: {input_data.region}")
    
    # Map categorical values
    smoker_encoded = smoker_map.get(input_data.smoker.lower())
    sex_encoded = sex_map.get(input_data.sex.lower())
    region_encoded = region_map.get(input_data.region.lower())
    
    # Validate mappings
    if smoker_encoded is None:
        raise ValueError(f"Invalid smoker value: {input_data.smoker}")
    if sex_encoded is None:
        raise ValueError(f"Invalid sex value: {input_data.sex}")
    if region_encoded is None:
        raise ValueError(f"Invalid region value: {input_data.region}")
    
    print("\n🔢 ENCODED VALUES:")
    print(f"   Smoker: {input_data.smoker} → {smoker_encoded}")
    print(f"   Sex: {input_data.sex} → {sex_encoded}")
    print(f"   Region: {input_data.region} → {region_encoded}")
    
    # ⚠️ CRITICAL: Match the EXACT order used during training
    # Check what order your model expects:
    if hasattr(forest_model, 'feature_names_in_'):
        expected_features = forest_model.feature_names_in_
        print(f"\n📋 Model expects features: {list(expected_features)}")
        
        # Create DataFrame with exact column order
        df = pd.DataFrame([[
            input_data.age,
            sex_encoded,
            input_data.bmi,
            input_data.children,
            smoker_encoded,
            region_encoded
        ]], columns=expected_features)
    else:
        # Fallback: Use standard order (age, sex, bmi, children, smoker, region)
        print("\n⚠️  Model doesn't have feature names saved!")
        print("   Using assumed order: age, sex, bmi, children, smoker, region")
        
        df = pd.DataFrame({
            'age': [input_data.age],
            'sex': [sex_encoded],
            'bmi': [input_data.bmi],
            'children': [input_data.children],
            'smoker': [smoker_encoded],
            'region': [region_encoded]
        })
    
    # Final verification
    print("\n🎯 FINAL INPUT TO MODEL:")
    print(df)
    print(f"\n   Shape: {df.shape}")
    print(f"   Values: {df.values[0]}")
    
    # Make prediction
    prediction = forest_model.predict(df)[0]
    
    print(f"\n✅ RAW PREDICTION: {prediction}")
    print(f"✅ ROUNDED: ${round(float(prediction), 2)}")
    print("=" * 60 + "\n")
    
    return round(float(prediction), 2)