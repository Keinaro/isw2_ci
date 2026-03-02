# app.py
import os

API_KEY = os.getenv("API_KEY")


def sumar(a, b):
    resultado = a + b
    return resultado


def restar(a, b):
    return a - b