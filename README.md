# rancher-oauth
OAuth2 middleware proxy for Rancher stacks

Installs a OAuth2 proxy for a given stack using a rancher DNS hostname to map the upstream service. Useful for providing a oauth layer in between the application and the Traefik proxy for Rancher.

```
python up.py -s mystack -u myapplication.mystack -p 8080 www.example.com
```

Use an environment file to define `OAUTH_DOMAIN` and `OAUTH_CONFIG` for the 
