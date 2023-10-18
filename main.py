import openai
import user_operations
import openai_operations
import pandas as pd

df = pd.read_csv("SDW2023.csv")
user_ids = df["UserID"].tolist()
print(user_ids)

users = user_operations.get_users(user_ids)

openai_api_key = "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"
openai.api_key = openai_api_key

for user in users:
    news = openai_operations.generate_ai_news(user)
    print(news)
    user["news"].append(
        {
            "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
            "description": news,
        }
    )

for user in users:
    success = user_operations.update_user(user)
    print(f"User {user['name']} updated? {success}!")
