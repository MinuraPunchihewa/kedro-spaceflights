from kedro.pipeline import node, Pipeline
from spaceflights.pipelines.data_engineering.nodes import preprocess_companies, preprocess_shuttles, create_master_table


def create_pipeline(**kwargs):
	return Pipeline(
		[
			node(
				func=preprocess_companies,
				inputs="companies",
				outputs="preprocessed_companies",
				name="preprocess_companies"
			),
			node(
				func=preprocess_shuttles,
				inputs="shuttles",
				outputs="preprocessed_shuttles",
				name="preprocess_shuttles"
			),
			node(
				func=create_master_table,
				inputs=["preprocessed_shuttles", "preprocessed_companies", "reviews"],
				outputs="master_table",
				name="create_master_table"
			)
		]
	)