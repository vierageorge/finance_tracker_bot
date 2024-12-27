import requests
import logging
from dotenv import load_dotenv
import os
load_dotenv()

main_url = os.getenv("MAIN_API_URL")

def save_cash_expense(description: str, value: int):
  url = f"{main_url}?cash=1"
  payload = {
    "description": description,
    "value": value
  }
  headers = {
    "Content-Type": "application/json"
  }

  response = requests.post(url, json=payload, headers=headers)
  response_data = response.json()

  if response_data.get("status") != "OK":
    logging.error(f"Error: {response_data.get('message')}")

def get_categories():
  url = f"{main_url}?categories=1"
  response = requests.get(url)
  response_data = response.json()

  if response_data.get("status") != "OK":
    logging.error(f"Error: {response_data.get('message')}")
    return []

  return response_data.get("categories")

def save_money_transfer(description: str, value: int, category: str):
  url = f"{main_url}?moneytransfer=1"
  payload = {
    "description": description,
    "value": value,
    "category": category
  }
  headers = {
    "Content-Type": "application/json"
  }

  response = requests.post(url, json=payload, headers=headers)
  response_data = response.json()

  if response_data.get("status") != "OK":
    logging.error(f"Error: {response_data}")