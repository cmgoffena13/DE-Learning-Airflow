from airflow.decorators import dag, task
from datetime import datetime
import random
 
 
@dag(
    'random_number_checker',
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    description='A simple DAG to generate and check random numbers',
    catchup=False
)
def random_number_checker_taskflow():

    @task
    def generate_random_number():
        number = random.randint(1, 100)
        print(f"Generated random number: {number}")
        return number

    @task
    def check_even_odd(number: int):
        result = "even" if number % 2 == 0 else "odd"
        print(f"The number {number} is {result}.")

    # Define the flow of tasks
    check_even_odd(generate_random_number())

# Invoke the DAG
random_number_checker_taskflow()