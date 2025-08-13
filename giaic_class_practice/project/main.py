
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, set_trace_disabled, UserContext, function_tool, RunContextWrapper
from pydantic import BaseModel
set_trace_disabled(disabled=True)

gemini_api_key = "AIzaSyA_PnRqMxfif_RHz6ISdPhK27tJAnHVwWM"

client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client
)

class UserContext(BaseModel):
    name: str
    age: int

@function_tool
async def check_age(wrapper: RunContextWrapper[UserContext]) -> str:
    user = wrapper.context
    if user.age >= 18:
        return f"{user.name} is an adult"
    else:
        return f"{user.name} is not an adult"

agent = Agent(
    name="Assistant",
    instruction="You are helpful",
    model=model
)


context =UserContext(name="subhan", age=17)
result = Runner.run_sync(
    agent,
    "helo",
    context=context

)

print(result.final_output)