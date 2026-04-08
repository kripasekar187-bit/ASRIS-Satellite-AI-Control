<<<<<<< HEAD
import pandas as pd
import numpy as np

np.random.seed(42)

data_size = 200

data = pd.DataFrame({
    "solar_activity": np.random.uniform(0, 100, data_size),
    "radiation_level": np.random.uniform(0, 100, data_size),
    "satellite_temp": np.random.uniform(20, 120, data_size)
})

def assign_risk(row):
    if row["solar_activity"] > 70 and row["radiation_level"] > 70:
        return "CRITICAL"
    elif row["solar_activity"] > 50:
        return "WARNING"
    else:
        return "SAFE"

data["risk_level"] = data.apply(assign_risk, axis=1)

data.to_csv("satellite_data.csv", index=False)

=======
import pandas as pd
import numpy as np

np.random.seed(42)

data_size = 200

data = pd.DataFrame({
    "solar_activity": np.random.uniform(0, 100, data_size),
    "radiation_level": np.random.uniform(0, 100, data_size),
    "satellite_temp": np.random.uniform(20, 120, data_size)
})

def assign_risk(row):
    if row["solar_activity"] > 70 and row["radiation_level"] > 70:
        return "CRITICAL"
    elif row["solar_activity"] > 50:
        return "WARNING"
    else:
        return "SAFE"

data["risk_level"] = data.apply(assign_risk, axis=1)

data.to_csv("satellite_data.csv", index=False)

>>>>>>> 198051d (Initial commit of ASRIS Project)
print("Dataset created successfully ✅")