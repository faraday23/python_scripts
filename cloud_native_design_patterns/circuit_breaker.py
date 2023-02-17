# This script uses the resilient library to implement the circuit breaker pattern for cloud-native applications. The CircuitBreaker class is used to create a circuit breaker with a failure threshold of 3 and a recovery timeout of 5 seconds. This means that if the external service fails 3 times in a row, the circuit breaker will open and any subsequent calls to the service will fail immediately for the next 5 seconds.

# The script includes a function called call_service that uses the requests library to call the external service. This function is wrapped in the @circuit_breaker decorator to create a version of the function that uses the circuit breaker.

# The script also includes a function called call_service_async that calls call_service_with_circuit_breaker asynchronously using the concurrent.futures library. This function returns a Future object that can be used to get the result of the call to the external service.

# The script includes two examples of calling the external service using the circuit breaker. The first example calls the external service synchronously using the call_service_with_circuit_breaker function. The second example calls the external service asynchronously using the call_service_async function and the result method of the Future object.

# In both examples, the script tries to call the external service and prints the response if the call is successful. If the call fails, the circuit breaker is reset and any subsequent calls to the service will be allowed.

# To use this script, you will need to replace the service_url variable with the URL of the external service you want to call. You may also need to modify the failure_threshold and recovery_timeout parameters of the CircuitBreaker constructor to match the needs of your application.


from resilient import CircuitBreaker, Future
from concurrent.futures import ThreadPoolExecutor
import requests

# URL of the external service to call
service_url = 'https://api.example.com'

# Create a circuit breaker with a 5 second timeout and a maximum of 3 failures before opening the circuit
circuit_breaker = CircuitBreaker(failure_threshold=3, recovery_timeout=5)

# Function to call the external service using the requests library
def call_service():
    response = requests.get(service_url)
    response.raise_for_status()
    return response.json()

# Function to call the external service using the circuit breaker
@circuit_breaker
def call_service_with_circuit_breaker():
    return call_service()

# Function to call the external service asynchronously using the circuit breaker
def call_service_async():
    with ThreadPoolExecutor() as executor:
        future = Future(executor.submit(call_service_with_circuit_breaker))
        return future

# Call the external service using the circuit breaker
try:
    response = call_service_with_circuit_breaker()
    print(f"Response from external service: {response}")
except Exception as e:
    print(f"Error calling external service: {e}")
    circuit_breaker.reset()

# Call the external service asynchronously using the circuit breaker
future = call_service_async()
try:
    response = future.result()
    print(f"Response from external service: {response}")
except Exception as e:
    print(f"Error calling external service: {e}")
    circuit_breaker.reset()
