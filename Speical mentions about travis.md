## Issues with Travis

Our `.travis.yml` file doesn't allow us to build integration with our package. For the reason that, we have certain dependencies on apps that require configuration to slack API token. we tried multiple ways to fix it and used the recourse provided by the professor but we are still unable to run our `.travis.yml` file in Travis. Hence, the status is always failing. We have added a requirement.txt file with all the dependencies we have used such as `slackclient` and `urllib3`. We have included on `requirement.txt` on GitHub.
