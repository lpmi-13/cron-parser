# Cron Parser

Our team has a lot of different AWS resources that use crons, and sometimes it's nice to make sure that things which stress our system don't happen at the same time (ie, batch jobs that involve a lot of database reads/writes).

We're planning to introduce a dashboard in our self-service system to display all the various scheduled tasks we have so teams can easily see if they're planning one to run at the same time as another resource-intensive job. We also plan to eventually check these clashes in CI, but that will be a future project.

At the moment, the only thing we run on schedules are lambdas and ECS services, but we can use this same approach for any future resources that we'd also like to run on a schedule.

## Running the tests

We chose to use the basic `unittest` module, since it doesn't require any dependencies.

```
python -m unittest
```

## Running the script locally

This has no dependencies outside the standard library, so any installation of python3 should be good to go!

```
python input_validation.py '10 */2 5 * 3,4 /usr/local/bin/boom.sh'
```

## Current execution context

We currently offer this as a simple python script for the teams to run and check their crons, but eventually, we'd like to put it in a lambda that runs on service deployment and updates a datastore (most likely DynamoDB) so we can query it for our self-service dashboard frontend. We might also run this once daily just to compensate for any transient issues with running on deployment, but the ideal scenario would be a run only during deployments, which scales much more easily.

## Linting

The project uses the `black` formatter, and eventually will probably run it on a pre-commit hook with lefthook.
