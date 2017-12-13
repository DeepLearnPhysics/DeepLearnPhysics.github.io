# DeepLearnPhysics.github.io
A repository for DeepLearnPhysics group [top](https://deeplearnphysics.org) webpage for group descriptions.
The `master` branch holds static HTML files generated by [Pelican](http://docs.getpelican.com/en/stable/) with [uno theme](https://github.com/DeepLearnPhysics/pelican-uno).
The `develop` branch holds source code to generate the website.

## Requirement
You need python packages:
* `pelican >= 3.5.0`
* `markdown >= 2.6.9`

## How to contribute (develop)
For aweome you to help development, follow the following steps. I split into three steps: **installation**, **compilation**, **development**, and **publish**.

### Installation
1. Join [web-blog](https://github.com/orgs/DeepLearnPhysics/teams/web-main) github team
2. Clone the repo: `git clone git@github.com:DeepLearnPhysics/DeepLearnPhysics.github.io`.
3. Make sure you are on the `develop` branch by `git branch`
### Compilation
By compilation we mean to generate static HTMLs. This is fairly simple:
1.  `make html`

### Development
Our development work is a process of modify-compile-check. The **first to-do** is:
1. Open `pelicanconf.py` and **uncomment** the line `#SITEURL = ''`. This generates HTMLs to be viewed locally.
2. `make devserver` then access `localhost:8000` on your browser. This runs a virtual pelican web server on your machine and allows you to browse the updated website contents all on your laptop.
3. Make modifications you wish to make. `contents` directory is where you make a _blog post_.
4. `make html` will update your local static website.

### Publish
After you finish your development work, if you want to publish your change on our website, you have to push your changes.
1. Open `pelicanconf.py` and **comment out** the line `SITEURL = ''`. This generates HTMLs to be viewed on the shared remote server.
2. `make html` and if you are running a local virtual server, `make stopserver`.
3. Commit your changes to the develop branch.
4. `git checkout master` ... the master branch holds static website contents.
5. `cp -r output/* ./`
6. `git add .`
7. `git commit -m "your message"`
8. `git push`

Done!

---

### Copyright and license

It is under [the MIT license](/LICENSE).
