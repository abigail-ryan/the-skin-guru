# Testing

This is the TESTING file for [The Skin guru](https://the-skin-guru-6ce126511380.herokuapp.com/)

Return to the [README.md](README.md) file.

## Contents

* [HTML Validation](#html-validation)
* [CSS Validation](#css-validation-using-w3c-validation)
* [JS Validation](#css-validation-using-w3c-validation)
* [Pep8 Validation](#pep8-validation)
* [Lighthouse scores using Chrome Dev Tools](#lighthouse-scores-using-chrome-dev-tools)
* [Device Testing and Browser Compability Testing](#device-testing-and-browser-compatibility-testing)
* [Manual Testing](#manual-testing)
    * [User Stories testing](#user-stories-testing)
    * [User Input testing](#user-stories-testing)
* [Bugs](#bugs)

<br>

____

#### HTML Validation

For testing my HTML for this project, I used the Validate by Direct Input option on W3C Markup Validation. 


![Screenshot of The Skin Guru - HTML Validation Home Page](documentation/home-page-html-validation.png) 

I checked all pages of the site in this way and the results are below:

<details>
<summary>All Pages HTML Validation</summary>
<br>

| HTML Page | Errors | Warnings | Screenshot |
| ---- | ------ | -------- | -------- | 
| Home | None | None | As above |
| All products | None | None | ![Screenshot of The Skin Guru - HTML Validation all products page](documentation/all-products-page-html-validation.png) |
| Product details | None | None | ![Screenshot of The Skin Guru - HTML Validation product detaikls page](documentation/product-details-page-html-validation.png) |
| All Articles | None | None | ![Screenshot of The Skin Guru - HTML Validation All Articles page](documentation/all-products-page-html-validation.png) |
| Article Details | None | None | ![Screenshot of The Skin Guru - HTML Validation Article Details page](documentation/article-details-page-html-validation.png) |
| My Profile | None | None | ![Screenshot of The Skin Guru - HTML Validation my profile page](documentation/my-profile-page-html-validation.png) |
| My Wishlist | None | None | ![Screenshot of The Skin Guru - HTML Validation my wishlist page](documentation/my-wishlist-with-Item-html-validation.png) |
| Cart | None | None | ![Screenshot of The Skin Guru - HTML Validation cart page](documentation/cart-page-with-item-html-validation.png) |
| Checkout | None | None | ![Screenshot of The Skin Guru - HTML Validation checkout page](documentation/checkout-page-html-validation.png) |
| Checkout Success | None | None | ![Screenshot of The Skin Guru - HTML Validation checkout success page](documentation/checkout-success-page-html-validation.png) |
| Contact | None | None | ![Screenshot of The Skin Guru - HTML Validation contact page](documentation/contact-page-html-validation.png) |
| Delivery Info | None | None | ![Screenshot of The Skin Guru - HTML Validation delivery info page](documentation/delivery-info-page-html-validation.png) |
| Sign in | 1 | None | ![Screenshot of The Skin Guru - HTML Validation sign in page](documentation/sign-in-html-validation.png) |
| Sign up | 2 | None | ![Screenshot of The Skin Guru - HTML Validation sign up page](documentation/sign-up-html-validation.png) |
| 404 | None | None | ![Screenshot of The Skin Guru - HTML Validation 404 page](documentation/404-error-page-html-validation.png) |
| 500 | None | None | ![Screenshot of The Skin Guru - HTML Validation 500 page](documentation/500-server-error-page-html-validation.png) |

The Sign In & Sign Up pages both showed small errors, however as these templates are made up of includes, blocktrans and redirect blocks, I was unable to find there these issues were coming from.

</details>

<br>

____

### CSS Validation

My direct input CSS Validation checks returned no errors. There were warnings present on the deployed url input, howvere these relate to mailchimp and boostrap and do not have any effect on my code.

![Screenshot of The Skin Guru - CSS Validation deployed url](documentation/the-skinguru-deployed-url-css-val.png) 

![Screenshot of The Skin Guru - CSS Validation warnings](documentation/theskinguru-url-css-vallidation.png) 

<details>
<summary>All CSS Validation</summary>
<br>

| CSS Doc | Errors | Warnings | Screenshot |
| ---- | ------ | -------- | -------- | 
| base.css | None | None | ![Screenshot of The Skin Guru - CSS Validation base.css](documentation/base-css-validation.png) |
| checkout.css | None | None | ![Screenshot of The Skin Guru - CSS Validation checkout.css](documentation/checkout-csss-validation.png) |
| posts.css | None | None | ![Screenshot of The Skin Guru - CSS Validation posts.css](documentation/posts-css-validation.png) |
| profile.css | None | None | ![Screenshot of The Skin Guru - CSS Validation profile.css](documentation/profile-css-validation.png) |

</details>

<br>

____

### JS Validation

I checked my JavaScript code using JSHint, and input a variation of the following lines into the top of the input box to correctly test the code without throwing errors.
/* jshint esversion: 6, jquery: true, browser: true */ /* global Stripe, bootstrap */
 

<details>
<summary>All CSS Validation</summary>
<br>

| JS File | Errors | Warnings | Screenshot |
| ---- | ------ | -------- | -------- | 
| comments.js | None | None | ![Screenshot of The Skin Guru - CSS Validation comments.js](documentation/comments-js-validation.png) |
| countryfield.js | None | None | ![Screenshot of The Skin Guru - CSS Validation countryfield.js](documentation/countryfields-js-validation.png) |
| reviews.js | None | None | ![Screenshot of The Skin Guru - CSS Validation reviews.js](documentation/reviews-js-validatioon.png) |
| stripe_elements.js | None | None | ![Screenshot of The Skin Guru - CSS Validation stripe_elements.js](documentation/stripe_elements-js-validation.png) |

</details>

<br>

____

#### Pep8 Validation

CI Python Linter was used to validate the Python files. Some minor line lenght isuues, missing lines, and trailing white space errors were raised and fixed in all .py files before final deployment.

![Screenshot of The Skin Guru - PEP8 Validation - minor errors](documentation/pep8-minor-errors.png) 

<details>
<summary>All Python Validation</summary>
<br>

| Python App | File  | Errors | Screenshot |
| ---- | ------ | -------- | -------- | 
| Articles App | admin.py | None | ![Screenshot of The Skin Guru - Pep8 Validation admin.py](documentation/articles-admin-py.png) |
|  | apps.py | None | ![Screenshot of The Skin Guru - Pep8 Validation apps.py](documentation/articles-apps-py.png) |
|  | forms.py | None | ![Screenshot of The Skin Guru - Pep8 Validation forms.py](documentation/articles-forms-py.png) |
|  | models.py | None | ![Screenshot of The Skin Guru - Pep8 Validation models.py](documentation/articles-models-py.png) |
|  | urls.py | None | ![Screenshot of The Skin Guru - Pep8 Validation urls.py](documentation/articles-urls-py.png) |
|  | views.py | None | ![Screenshot of The Skin Guru - Pep8 Validation views.py](documentation/articles-views-py.png) |
| ---- | ------ | -------- | -------- | 
| Cart App | apps.py | None | ![Screenshot of The Skin Guru - Pep8 Validation apps.py](documentation/cart-apps-py.png) |
|  | contexts.py | None | ![Screenshot of The Skin Guru - Pep8 Validation contexts.py](documentation/cart-contexts-py.png) |
|  | urls.py | None | ![Screenshot of The Skin Guru - Pep8 Validation urls.py](documentation/cart-urls-py.png) |
|  | views.py | None | ![Screenshot of The Skin Guru - Pep8 Validation views.py](documentation/cart-views-py.png) |
| ---- | ------ | -------- | -------- | 
| Checkout App | admin.py | None | ![Screenshot of The Skin Guru - Pep8 Validation admin.py](documentation/checkout-admin-py.png) |
|  | apps.py | None | ![Screenshot of The Skin Guru - Pep8 Validation apps.py](documentation/checkout-apps-py.png) |
|  | forms.py | None | ![Screenshot of The Skin Guru - Pep8 Validation fomrs.py](documentation/checkout-forms-py.png) |
|  | models.py | None | ![Screenshot of The Skin Guru - Pep8 Validation models.py](documentation/checkout-models-py.png) |
|  | signals.py | None | ![Screenshot of The Skin Guru - Pep8 Validation signals.py](documentation/checkout-signals-py.png) |
|  | urls.py | None | ![Screenshot of The Skin Guru - Pep8 Validation urls.py](documentation/checkout-urls-py.png) |
|  | views.py | None | ![Screenshot of The Skin Guru - Pep8 Validation views.py](documentation/checkout-views-py.png) |
|  | wehbook_handler.py | None | ![Screenshot of The Skin Guru - Pep8 Validation webhook_handler.py](documentation/checkout-webhook-handler-py.png) |
|  | webhook.py | None | ![Screenshot of The Skin Guru - Pep8 Validation webhook.py](documentation/checkout-webhook-py.png) |
| ---- | ------ | -------- | -------- | 
| Contact App | admin.py | None | ![Screenshot of The Skin Guru - Pep8 Validation admin.py](documentation/contact-admin-py.png) |
|  | apps.py | None | ![Screenshot of The Skin Guru - Pep8 Validation apps.py](documentation/contact-apps-py.png) |
|  | forms.py | None | ![Screenshot of The Skin Guru - Pep8 Validation forms.py](documentation/contact-forms-py.png) |
|  | modles.py | None | ![Screenshot of The Skin Guru - Pep8 Validation modles.py](documentation/contact-models-py.png) |
|  | urls.py | None | ![Screenshot of The Skin Guru - Pep8 Validation urls.py](documentation/contact-urls-py.png) |
|  | views.py | None | ![Screenshot of The Skin Guru - Pep8 Validation views.py](documentation/contact-views-py.png) |
| ---- | ------ | -------- | -------- | 
| Home App | apps.py | None | ![Screenshot of The Skin Guru - Pep8 Validation apps.py](documentation/home-apps-py.png) |
|  | urls.py | None | ![Screenshot of The Skin Guru - Pep8 Validation urls.py](documentation/home-urls-py.png) |
|  | views.py | None | ![Screenshot of The Skin Guru - Pep8 Validation views.py](documentation/home-views-py.png) |
| ---- | ------ | -------- | -------- | 
| Products App | admin.py | None | ![Screenshot of The Skin Guru - Pep8 Validation admin.py](documentation/products-admin-py.png) |
|  | apps.py | None | ![Screenshot of The Skin Guru - Pep8 Validation apps.py](documentation/products-apps-py.png) |
|  | forms.py | None | ![Screenshot of The Skin Guru - Pep8 Validation fomrs.py](documentation/products-forms-py.png) |
|  | modles.py | None | ![Screenshot of The Skin Guru - Pep8 Validation mmodles.py](documentation/products-models-py.png) |
|  | urls.py | None | ![Screenshot of The Skin Guru - Pep8 Validation urls.py](documentation/products-urls-py.png) |
|  | views.py | None | ![Screenshot of The Skin Guru - Pep8 Validation views.py](documentation/products-views-py.png) |
| ---- | ------ | -------- | -------- | 
| Profiles App | apps.py | None | ![Screenshot of The Skin Guru - Pep8 Validation apps.py](documentation/profiles-apps-py.png) |
|  | fomrs.py | None | ![Screenshot of The Skin Guru - Pep8 Validation forms.py](documentation/profiles-forms-py.png) |
|  | models.py | None | ![Screenshot of The Skin Guru - Pep8 Validation models.py](documentation/profiles-models-py.png) |
|  | urls.py | None | ![Screenshot of The Skin Guru - Pep8 Validation urls.py](documentation/profiles-urls-py.png) |
|  | views.py | None | ![Screenshot of The Skin Guru - Pep8 Validation views.py](documentation/profiles-views-py.png) |
| ---- | ------ | -------- | -------- | 
| Wishlist | admin.py | None | ![Screenshot of The Skin Guru - Pep8 Validation admin.py](documentation/wishlist-admin-py.png) |
|  | apps.py | None | ![Screenshot of The Skin Guru - Pep8 Validation apps.py](documentation/wishlist-apps-py.png) |
|  | contexts.py | None | ![Screenshot of The Skin Guru - Pep8 Validation contexts.py](documentation/wishlist-contexts-py.png) |
|  | modles.py | None | ![Screenshot of The Skin Guru - Pep8 Validation models.py](documentation/wishlist-models-py.png) |
|  | signals.py | None | ![Screenshot of The Skin Guru - Pep8 Validation signals.py](documentation/wishlist-signals-py.png) |
|  | urls.py | None | ![Screenshot of The Skin Guru - Pep8 Validation urls.py](documentation/wishlist-urls-py.png) |
|  | views.py | None | ![Screenshot of The Skin Guru - Pep8 Validation views.py](documentation/wishlist-views-py.png) |
| ---- | ------ | -------- | -------- | 
| The Skin Guru Project | urls.py | None | ![Screenshot of The Skin Guru - Pep8 Validation urls.py](documentation/theskinguru-urls-py.png) |
|  | views.py | None | ![Screenshot of The Skin Guru - Pep8 Validation views.py](documentation/theskinguru-views-py.png) |

</details>

<br>