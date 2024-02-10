import autogen
# for access through litellm
#BASE_URL="http://0.0.0.0:8000"
# direct access to Ollama since 0.1.24, compatible with OpenAI /chat/completions
BASE_URL="http://localhost:11434/v1"

config_list_mistral = [
    {
        'base_url': BASE_URL,
        'api_key': "fakekey",
        'model': "mistral:latest",
    }
]

config_list_codellama = [
    {
        'base_url': BASE_URL,
        'api_key': "fakekey",
        'model': "codellama:7b-code-q4_K_M",
    }
]

llm_config_mistral={
    "config_list": config_list_mistral,
}

llm_config_codellama={
    "config_list": config_list_codellama,
}

user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={"work_dir": "web", "use_docker": False},
    llm_config=llm_config_mistral,
    system_message="""Reply TERMINATE if the task has been solved at full satisfaction.
Otherwise, reply CONTINUE, or the reason why the task is not solved yet."""
)

coder = autogen.AssistantAgent(
    name="Coder",
    llm_config=llm_config_codellama
)

#task="""
#Write a python script to implement the snake game and then the user_proxy agent should run the script
#"""

task="""
Write a python script that lists the number from 1 to 100
"""

user_proxy.initiate_chat(coder, message=task)
