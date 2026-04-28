from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Congruity Ride Gate Demo")

class RideInput(BaseModel):
    depot_to_pickup_km: float
    service_km: float
    return_km: float
    price_eur: float
    cost_per_km: float = 1.0
    impact_cost_eur: float = 40.0
    structural_cost_eur: float = 20.0

@app.post("/evaluate-ride")
def evaluate_ride(data: RideInput):
    total_km = data.depot_to_pickup_km + data.service_km + data.return_km
    energy_cost = total_km * data.cost_per_km
    total_system_cost = energy_cost + data.impact_cost_eur + data.structural_cost_eur

    if total_system_cost == 0:
        congruity_score = 0
    else:
        congruity_score = data.price_eur / total_system_cost

    if congruity_score > 1.0:
        decision = "EXECUTE"
    elif congruity_score > 0.6:
        decision = "SIMPLIFY"
    else:
        decision = "REJECT"

    return {
        "total_km": total_km,
        "energy_cost_eur": round(energy_cost, 2),
        "total_system_cost_eur": round(total_system_cost, 2),
        "price_eur": data.price_eur,
        "congruity_score": round(congruity_score, 3),
        "decision": decision
    }
