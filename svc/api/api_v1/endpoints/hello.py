from fastapi import APIRouter

from svc.core.models.output import MessageOutput
from svc.core.models.input import MessageInput
from svc.core.logic.business_logic import run_prime_factor_calculation

router = APIRouter()

@router.post("/hello", response_model=MessageOutput, tags=["hello post"])
def hello_endpoint(inputs: MessageInput):
    """
    Respond to requests on the hello endpoint
    """

    n, largest_prime_factor, elapsed_time = run_prime_factor_calculation()

    return {
        "first": "Hello pal",
        "second": f"The largest prime factor of {n} is {largest_prime_factor}. Calculation took {elapsed_time:0.3f} seconds.",
        "n": n,
        "largest_prime_factor": largest_prime_factor,
        "elapsed_time": elapsed_time,
    }
