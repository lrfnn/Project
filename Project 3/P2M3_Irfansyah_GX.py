import pandas as pd
import great_expectations as gx
from great_expectations.checkpoint import Checkpoint

context = gx.get_context()
datasource = context.sources.add_pandas(name="my_pandas_datasource")
dataframe = pd.read_csv('P2M3_Irfansyah_data_clean.csv')

name = "graduated"
data_asset = datasource.add_dataframe_asset(name=name)
my_batch_request = data_asset.build_batch_request(dataframe=dataframe)

expectation_suite_name = "milestone3"
context.add_or_update_expectation_suite(expectation_suite_name=expectation_suite_name)
validator = context.get_validator(
    batch_request=data_asset.build_batch_request(dataframe=dataframe),
    expectation_suite_name=expectation_suite_name,)

validator.expect_column_values_to_not_be_null(column="target")
validator.expect_column_values_to_not_be_null(column="daytime/evening_attendance")
validator.expect_column_to_exist(column="gdp")
validator.expect_column_values_to_not_be_null(column="gender")
validator.expect_column_values_to_be_between(column="age_at_enrollment", min_value=1, max_value=70)
validator.expect_column_values_to_not_be_null(column="course")
validator.expect_column_values_to_be_in_set("gender", [0, 1])
validator.save_expectation_suite(discard_failed_expectations=False)

my_checkpoint_name = "milestone3_checkpoint"

checkpoint = Checkpoint(
    name=my_checkpoint_name,
    run_name_template="%Y%m%d-%H%M%S-milestone3_checkpoint",
    data_context=context,
    batch_request=my_batch_request,
    expectation_suite_name=expectation_suite_name,
    action_list=[
        {
            "name": "store_validation_result",
            "action": {"class_name": "StoreValidationResultAction"},
        },
        {"name": "update_data_docs", "action": {"class_name": "UpdateDataDocsAction"}},
    ],
)

context.add_or_update_checkpoint(checkpoint=checkpoint)
checkpoint_result = checkpoint.run()
context.open_data_docs()
