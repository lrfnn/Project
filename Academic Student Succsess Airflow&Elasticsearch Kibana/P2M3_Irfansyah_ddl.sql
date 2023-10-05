CREATE TABLE table_M3 (
    "Marital status" INT,
    "Application mode" INT,
    "Application order" INT,
    "Course" INT,
    "Daytime/evening attendance" INT,
    "Previous qualification" INT,
    "Nacionality" INT,
    "Mother's qualification" INT,
    "Father's qualification" INT,
    "Mother's occupation" INT,
    "Father's occupation" INT,
    "Displaced" INT,
    "Educational special needs" INT,
    "Debtor" INT,
    "Tuition fees up to date" INT,
    "Gender" INT,
    "Scholarship holder" INT,
    "Age at enrollment" INT,
    "International" INT,
    "Curricular units 1st sem (credited)" INT,
    "Curricular units 1st sem (enrolled)" INT,
    "Curricular units 1st sem (evaluations)" INT,
    "Curricular units 1st sem (approved)" INT,
    "Curricular units 1st sem (grade)" NUMERIC,
    "Curricular units 1st sem (without evaluations)" INT,
    "Curricular units 2nd sem (credited)" INT,
    "Curricular units 2nd sem (enrolled)" INT,
    "Curricular units 2nd sem (evaluations)" INT,
    "Curricular units 2nd sem (approved)" INT,
    "Curricular units 2nd sem (grade)" NUMERIC,
    "Curricular units 2nd sem (without evaluations)" INT,
    "Unemployment rate" NUMERIC,
    "Inflation rate" NUMERIC,
    "GDP" NUMERIC,
    "Target" VARCHAR (100)
);

COPY table_M3 (
    "Marital status",
    "Application mode",
    "Application order",
    "Course",
    "Daytime/evening attendance",
    "Previous qualification",
    "Nacionality",
    "Mother's qualification",
    "Father's qualification",
    "Mother's occupation",
    "Father's occupation",
    "Displaced",
    "Educational special needs",
    "Debtor",
    "Tuition fees up to date",
    "Gender",
    "Scholarship holder",
    "Age at enrollment",
    "International",
    "Curricular units 1st sem (credited)",
    "Curricular units 1st sem (enrolled)",
    "Curricular units 1st sem (evaluations)",
    "Curricular units 1st sem (approved)",
    "Curricular units 1st sem (grade)",
    "Curricular units 1st sem (without evaluations)",
    "Curricular units 2nd sem (credited)",
    "Curricular units 2nd sem (enrolled)",
    "Curricular units 2nd sem (evaluations)",
    "Curricular units 2nd sem (approved)",
    "Curricular units 2nd sem (grade)",
    "Curricular units 2nd sem (without evaluations)",
    "Unemployment rate",
    "Inflation rate",
    "GDP",
    "Target"
	)
FROM '/Users/irfan/Desktop/Hacktiv/GC7/P2G7_Irfansyah_data_raw.csv' DELIMITER ',' CSV HEADER;
SELECT * FROM table_M3