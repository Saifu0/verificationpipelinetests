## Sample pipeline manifests for testing Verificationtool

### 1. simpleLinearPipeline
This manifests contains simple pipeline with two steps named `deploy_to_dev` and `deploy_to_int`. It tends to pass all the order, step status and pipeline status verification without any failed Events.

`deploy_to_int` is depend on `deploy_to_dev` which means after receiving all the events of `deploy_to_dev` we will expect events of `deploy_to_int`. 

### 2. parallelSteps
This manifests contains pipeline with two parallel steps named `deploy_to_dev` and `deploy_to_int`. It tends to pass all the order, step status and pipeline status verification without any failed Events.

`deploy_to_int` is not depend on `deploy_to_dev` which means events from `deploy_to_dev` and `deploy_to_int` can receive in any order.

### 3. complexPipelineWith4Steps
This manifests contains pipeline with 4 steps `deploy_to_dev`, `deploy_to_int`, `deploy_to_prod` and `deploy_to_stage`. They are in this order,
```
    root(PipelineTriggerEvent)
    /                   \
deploy_to_dev       deploy_to_int
    |                   /
deploy_to_prod         /
    \                 /
     \               /
      \             /
       \           /
        \         /
       deploy_to_stage
```
This pipeline should pass all the verification order in the DAG, step status and pipeline status.

### 4. humanError
This manifests contains pipeline with two linear steps `deploy_to_dev` and `deploy_to_int`. In the `tests` of `deploy_to_int` there is a typo in line 20. It is tends to fail because of this typo and send a `FailureEvent`.

Expected rules are also defined for this manifests.

### 5. multipleTestsForStep
This manifests contains pipeline with two linear steps `deploy_to_dev` and `deploy_to_int`. In the `tests` of `deploy_to_dev`, we have more than one `tests` with `before: true` and `before: false`. This pipeline should pass all the order in the DAG, step status and pipeline status verification.

### 6. testCompletionFailedDueToTypo
This manifests contains pipeline with two linear steps `deploy_to_dev` and `deploy_to_int`. In the `verifyendpoints.sh`, there is a typo in line 7 & 8. It is tends to fail at `TestCompletionEvent` of `deploy_to_dev`.

Expect rules are also defined for this manifest.

### 7. testCompletionProcessingFailed
This manifests contains pipeline with two linear steps `deploy_to_dev` and `deploy_to_int`. In the `verifyendpoints.sh`, we are returning `exit 1` to fail a test processing and raise a `TestCompletonEvent`. 

Expect rules are also defined for this manifest.

### 8. noDeployments
This manifests contains pipeline with two linear steps `deploy_to_dev` and `deploy_to_int`. In both the step, we have removed the deployment step. 
It should fail at `TestCompletionEvent`

Expect rules are also defined for this manifest. Expected step status should fail, `status: SUCCESS` should be `status: FAILURE`.

### 9. incorrectDependencies
This manifests contains pipeline with two linear steps `deploy_to_dev` and `deploy_to_int`. In the dependencies list of `deploy_to_int`, the step name is wrong and because of this, events of `deploy_to_int` will not received. 

### 10. clientCompletionFailed
This manifests contains pipeline with two linear steps `deploy_to_dev` and `deploy_to_int`. In the `argo_manifest/manifest.yaml`, we have removed `image` name. It is tends to fail at `ClientCompletionEvent`.

Expected rules are also defined for this manifest.

### 11. withRollBacks
This manifests contains pipeline with two linear steps `deploy_to_dev` and `deploy_to_int`. In step `deploy_to_dev`, `rollback_limit` is set to 1 and there is a bug in `verifyendpoints.sh` which will cause `TestCompletionEvent` failed and it will rollback and we will receive `TriggerStepEvent` of `deploy_to_dev` with failedStep populated after `PipelineCompletionEvent`.

Expected rules are also defined for this manifest.

