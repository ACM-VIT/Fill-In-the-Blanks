<h1 align="center"><a href="https://organize.mlh.io/participants/events/4390-kickstarting-hacktoberfest-with-acm-vit">Kicking Off Hacktoberfest with ACM-VIT!</a></h1>
<p align="center">
<img src="https://raw.githubusercontent.com/Malika01/hacktoberfest-readme/master/Final.png">
</p>

<h2 align="center"> Fill in the Blanks </h2>

<p align="center"> 
You’ve lost random parts of your images. You need some mechanism to make your image set presentable again. Use your skill in Machine Learning to achieve this.
</p>

<p>
  <a href="https://acmvit.in/" target="_blank">
    <img alt="made-by-acm" src="https://img.shields.io/badge/MADE%20BY-ACM%20VIT-blue?style=for-the-badge" />
  </a>
    <!-- Uncomment the below line to add the license badge. Make sure the right license badge is reflected. -->
    <!-- <img alt="license" src="https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge" /> -->
    <!-- forks/stars/tech stack in the form of badges from https://shields.io/ -->
</p>

---
## Submitting a Pull Request

 * Fork the repository by clicking the fork button on top right corner of the page
 * Clone the target repository. To clone, click on the clone button and copy the https address. Then run 
 <pre><code>git clone [HTTPS-ADDRESS]</code></pre>
* Go to the cloned directory by running 
<pre><code>cd [NAME-OF-REPO]</code></pre>
* Create a new branch. Use 
<pre><code> git checkout -b [YOUR-BRANCH-NAME]</code></pre>
* Make your changes to the code. Add changes to your branch by using 
<pre><code>git add .</code></pre>
* Commit the chanes by executing
<pre><code>git commit -m "your msg"</code></pre>
* Push to remote. To do this, run 
<pre><code>git push origin [YOUR-BRANCH-NAME]</code></pre>
* Create a pull request. Go to the target repository and click on the "Compare & pull request" button. **Make sure your PR description mentions which issues you're solving.**
<img src="https://drive.google.com/u/1/uc?id=1f9JKAR-kRvCRGxIs_SAvegaYDPx53T9G&export=download"></img>
* Wait for your request to be accepted. 

---
## Guidelines for Pull Request

<!-- general guidelines here -->
  * Avoid pull requests that :
      * are automated or scripted
      * that are plagarized from someone else's branch
  * Do not spam
  * Project maintainer's decision on validity of PR is final.

  For additional guidelines, refer to [participation rules](https://hacktoberfest.digitalocean.com/details#rules)

---
## What counts as a PR?
Check out our [issues](https://github.com/ACM-VIT/Fill-In-the-Blanks/issues) and try to solve them !
  
---
## Interacting with Issues

  * There are helper issues that detail all you have to do to complete the project.
      * Read the helper issues and work on the corresponding code in your fork of the repo.
      * If you have some doubt regarding the 'help' given, comment below the issue.
      * If you have some doubt not related to any 'helper issue/s' open, Open up a new issue, select doubt and fill in the template.
  * If you want to provide some extra help to fellow participants, open up a new helper issue. Don't include any solution/code!
  * Do not spam

---
## Overview

### Idea
Fill in the Blanks, but with Images!

### Explanation
The aim is to build a deep learning model, that takes as input an image with a missing rectangular portion and a boolean mask indicating its location, and imagines the missing content. The basic set of packages can be found in requirements.txt and can be installed using the pip command from usage section. The suggested dataset consists of images of various indoor scenes. Use the provided code to create the blanks in the images.

---
## Dataset
[Indoor Scenes [2.4GB tar]](http://groups.csail.mit.edu/vision/LabelMe/NewImages/indoorCVPR_09.tar)

### You may use the provided funtion to create the blanks
```python
import random_rect
new_img, bool_mask = random_rect(img, area)
```
Where <code>img</code>, <code>new_img</code> and <code>bool_mask</code> are NumPy or TensorFlow arrays,
<code>area</code> is a valid fraction in [0, 1].



---
## Usage
<!-- How To, Features, Installation etc. as subheadings in this section. example-->
Packages to be used are TensorFlow for creating and training the model, NumPy for handling arrays, MatPlotLib for image output.
Run the following command to install all the required packages for this project
<pre>pip install requirements.txt</pre>

Lets get started!
```console
git remote add
git fetch
git merge
```

---
## Authors


**Authors:**
[Rohan Nolan Lasrado](https://github.com/lasradorohan/), 
[Atharva Gundawar](https://github.com/Atharva-Gundawar)
<br>
**Contributors:** <!-- Generate contributors list using this link - https://contributors-img.web.app/preview -->
<a href="https://github.com/ACM-VIT/Fill-In-the-Blanks/graphs/contributors">
  <img src="https://contributors-img.web.app/image?repo=ACM-VIT/Fill-In-the-Blanks" />
</a>
