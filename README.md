## Config Validator

### Description

This is a simple configuration validator that will determine if a value is missing between two enviroments.
For example comparing between `qa` and `staging`, `qa` would be considered the base enviornment and `staging` the deploy environment. Any values in `qa` that are not in `staging` would be reported.

### Requirements

* Python 3.6+

### Usage

`python configValidator.py {base_env} {deploy_env}`
 