import mlflow

# List all experiments including deleted ones
client = mlflow.tracking.MlflowClient()

for experiment in client.search_experiments(view_type=mlflow.entities.ViewType.ALL):
    print(f"{experiment.experiment_id} - {experiment.name} - {experiment.lifecycle_stage}")

# Replace with the ID of the deleted experiment you want to restore
experiment_id_to_restore = "1"  # ← change this based on printed output

# Restore or delete permanently
client.restore_experiment(experiment_id_to_restore)

# OR permanently delete it:
# client.delete_experiment(experiment_id_to_restore)
