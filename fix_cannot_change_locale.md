# Troubleshooting

```sh
bash: warning: setlocale: LC_CTYPE: cannot change locale (UTF-8)
-bash: warning: setlocale: LC_CTYPE: cannot change locale (UTF-8)
```

You can see this message a lot on some AWS EC2 instances. Pop-up when using tab-completion in bash.

# Fix
Finally, this will fix

Add to `/etc/default/locale`

```
LC_ALL=en_US.UTF-8
LANG=en_US.UTF-8
```
