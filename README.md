# adpred_dashboard

## For Lakshmi:
Wherever you are working in (python or ipython console, jupyter etc.):

```python
	from lakshmi_script import open_lakshmis_files
	all_results = {}

	# then go over all your files and for each pair of files (predictions and sm), do
	# the following (gcn4 in this example):
	all_results['GCN4_YEAST'] = open_lakshmis_files('GCN4_YEAST.predictions.csv',
							'gcn4_satMut_50-and-108.saturated_mutagenesis.csv')
```
