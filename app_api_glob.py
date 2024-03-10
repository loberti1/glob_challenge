#importo librerias
import pandas as pd
import numpy as np
import os
from flask import Flask, jsonify, request
from sqlalchemy import create_engine

serie = pd.Series([1,2,3,4])
print(serie)