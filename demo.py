class Task:  
    def __init__(self, description):  
        self.description = description  
  
    async def run(self, **kwargs):  
        # Placeholder method to be overridden by subclasses  
        pass  
  
class DecisionTask(Task):  
    def __init__(self, description, decision_function):  
        super().__init__(description)  
        self.decision_function = decision_function  
  
    async def run(self, **kwargs):  
        print(f"Executing task: {self.description}")  
        result = self.decision_function(**kwargs)  
        print(f"Result of '{self.description}': {result}\n")  
        return result  
  
class CustomProcess:  
    def __init__(self, tasks):  
        self.tasks = tasks  
  
    async def run(self, **kwargs):  
        results = {}  
        for task in self.tasks:  
            result = await task.run(**kwargs)  
            # Store results using task description as the key  
            results[task.description] = result  
            # Update kwargs with new results for subsequent tasks if needed  
            kwargs.update({task.description: result})  
        return results  
  
class Agent:  
    def __init__(self):  
        pass  
  
    async def execute_process(self, process, **kwargs):  
        return await process.run(**kwargs)  
  
async def main():  
    # Input data  
    weather_input = 'Cloudy'  # Try changing this to 'Sunny', 'Rainy', or 'Cloudy'  
    humidity_input = 'High'   # Used if weather is 'Cloudy'  
  
    print("Agent is starting the decision-making process...\n")  
  
    # Define decision functions  
    def is_rainy(weather):  
        print(f"Checking if weather '{weather}' is 'rainy'")  
        return weather.lower() == 'rainy'  
  
    def is_cloudy(weather):  
        print(f"Checking if weather '{weather}' is 'cloudy'")  
        return weather.lower() == 'cloudy'  
  
    def is_high_humidity(humidity):  
        print(f"Checking if humidity '{humidity}' is 'high'")  
        return humidity.lower() == 'high'  
  
    # Create decision tasks  
    task1 = DecisionTask("Check if weather is rainy", lambda weather, **kwargs: is_rainy(weather))  
    task2 = DecisionTask("Check if weather is cloudy", lambda weather, **kwargs: is_cloudy(weather))  
    task3 = DecisionTask("Check if humidity is high", lambda humidity, **kwargs: is_high_humidity(humidity))  
  
    # Create a custom process with the tasks  
    my_process = CustomProcess([task1, task2, task3])  
  
    # Instantiate an agent  
    agent = Agent()  
  
    # Execute the process with the agent  
    results = await agent.execute_process(  
        my_process,  
        weather=weather_input,  
        humidity=humidity_input  
    )  
  
    # Make final decision based on the results  
    print("Agent has completed the tasks. Now making the final decision...\n")  
    if results["Check if weather is rainy"]:  
        decision = "Yes, you should bring an umbrella."  
    elif results["Check if weather is cloudy"]:  
        if results["Check if humidity is high"]:  
            decision = "Yes, you should bring an umbrella."  
        else:  
            decision = "No need to bring an umbrella."  
    else:  
        decision = "No need to bring an umbrella."  
  
    print(f"Final Decision: {decision}")  
  
if __name__ == "__main__":  
    import asyncio  
    asyncio.run(main())  



"""
Test Case 1:
Weather: rainy
It's raining.
Decision: Yes, you should bring an umbrella.

Test Case 2:
Weather: cloudy
It's cloudy.
Humidity: high
Humidity is high.
Decision: Yes, you should bring an umbrella.

Test Case 3:
Weather: cloudy
It's cloudy.
Humidity: low
Humidity is low.
Decision: No need to bring an umbrella.

Test Case 4:
Weather: sunny
It's sunny.
Decision: No need to bring an umbrella.

Test Case 5:
Weather: cloudy
It's cloudy.
Humidity information is missing.
Decision: Cannot make a decision without humidity information.

Test Case 6:
Weather: windy
Invalid weather value.
Decision: Cannot make a decision due to invalid weather input.

Test Case 7:
Weather: cloudy
It's cloudy.
Humidity: medium
Invalid humidity value.
Decision: Cannot make a decision due to invalid humidity input.

fabian.valle-simmons@M-JKMXP345RW yt-chat % vi mmmm.py     
fabian.valle-simmons@M-JKMXP345RW yt-chat % python3 mmmm.py
Agent is starting the decision-making process...

Executing task: Check if weather is rainy
Checking if weather 'Cloudy' is 'rainy'
Result of 'Check if weather is rainy': False

Executing task: Check if weather is cloudy
Checking if weather 'Cloudy' is 'cloudy'
Result of 'Check if weather is cloudy': True

Executing task: Check if humidity is high
Checking if humidity 'High' is 'high'
Result of 'Check if humidity is high': True

Agent has completed the tasks. Now making the final decision...

Final Decision: Yes, you should bring an umbrella.
"""
