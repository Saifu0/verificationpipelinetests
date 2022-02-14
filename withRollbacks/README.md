# withRollBacks
This manifests contains pipeline with two linear steps `deploy_to_dev` and `deploy_to_int`. In step `deploy_to_dev`, `rollback_limit` is set to 1 and there is a bug in `verifyendpoints.sh` which will cause `TestCompletionEvent` failed and it will rollback and we will receive `TriggerStepEvent` of `deploy_to_dev` with failedStep populated after `PipelineCompletionEvent`.

Expected rules are also defined for this manifest.