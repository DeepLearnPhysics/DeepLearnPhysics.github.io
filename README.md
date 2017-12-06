# DeepLearnPhysics.github.io
A repository for DeepLearnPhysics group top webpage for group descriptions.
The `master` branch holds static HTML files generated by [Pelican](http://docs.getpelican.com/en/stable/) with [uno theme](https://github.com/DeepLearnPhysics/pelican-uno).
The `develop` branch holds source code to generate the website.

### How to contribute
For aweome you to help development, follow the following steps
1. Join web-main github team
2. Install [Pelican](http://docs.getpelican.com/en/stable/) ... here's [quick start](http://docs.getpelican.com/en/stable/quickstart.html#).
3. Clone the repo: `git clone git@github.com:DeepLearnPhysics/DeepLearnPhysics.github.io`

You should be on the `develop` branch by default. To generate static website:

4. `make html`

To view the locally generated website (good idea before pushing!):

5. `make devserver` then access `localhost:8000` on your browser.

Finally, to make modification & test:

6. Make modifications you need, then `make html`. If you did step 5., you can check the change in the output in `localhost:8000`
7. Maybe good ide: change `SITEURL` in `pelicanconf.py` to `""` (empty string). This ensures generated static sites to use locally modified js/css under theme dir.

Note that `output` directory holds locally generated static HTML files. `output` directory is excluded from `develop` branch via `.gitignore` intentionally.
Ready to publish? Here are the steps.

8. Commit & push your change to `develop` branch. If you did step 7, `undo` it.
9. Make sure `develop` branch has no modifications by `git status`.
10. `git checkout master`, then `cp output/* ./` (this simply replaces the old page source with your new ones)
11. `git add .` && `git commit -m "updated"` && `git push`

Done!

---

### Copyright and license

It is under [the MIT license](/LICENSE).