# The Skin Guru
[View my live site here](https://)

The Skin Guru is an e-commerce platform designed for teens and young adults to explore and purchase skincare products. The website offers a comprehensive online shopping experience tailored to young skincare enthusiasts. Unregistered users can browse the entire store catalog, explore a variety of skincare products, read informative blog posts about skincare tips and trends, and view detailed product information. The site provides full access to product descriptions, pricing, purchasing and general site content without requiring account creation. Registered users gain additional benefits by creating a personal account. 

These users can:
* View and track their complete order history
* Save favorite products to a wishlist for future reference
* Write reviews under the products they have purchased
* Update their details from their personalised account dashboard.

The Skin Guru aims to be a user-friendly, educational, and accessible platform for young people looking to develop and maintain their skincare routines. By offering both guest browsing and enhanced registered user features, the site caters to different levels of user engagement and skincare knowledge.

____


## Contents
* [Project Goals](#project-goals)
* [User Stories](#user-stories)
* [Agile Development](#agile-development)
* [UX](#ux)
  * [Strategy](#strategy)
  *	[Scope](#scope)
  * [Structure](#structure)
  * [Skeleton](#skeleton)
    * [Wireframes](#wireframes)
  * [Surface](#surface)
* [Design](#design)
  * [Colour Scheme](#colour-scheme)
  * [Logo](#logo)
  * [Typography](#typography)
  * [Imagery](#imagery)
* [Database ERD](#database-erd)
* [Project Features](#project-features)
* [Future Features](#future-features)
* [Marketing](#marketing)
	* [Content Marketing](#content-marketing)
  * [SEO](#seo)
  * [Social Media](#social-media)
* [Technologies Used](#technologies-used)
  * [Languages](#languages)
  * [Frameworks, Libraries, Technologies and Programs used](#frameworks-libraries-technologies-and-programs-used)
* [Testing](#testing)
* [Deployment](#deployment)
  * [Forking the GitHub Repository](#forking-the-github-repository)
  * [Clone the GitHub Repository](#clone-the-github-repository)
  * [Django Project Setup](#django-project-setup)
  * [Database Creation](#database-creation)
  * [Cloudinary](#cloudinary)
  * [Deploying to Heroku](#Deploying-to-heroku)
* [Credits](#credits)
  * [Code References](#code-references)
  * [Content and Media References](#content-and-media-references)
* [Acknowledgements](#acknowledgements)  


____

### Project Goals

The goal of The Skin Guru project is to establish a vibrant and user-friendly online platform where teens and young adults can easily explore a wide variety of skincare products. The site encourages visitors to engage with its content, including informative blog posts about skincare routines and tips, while also providing a seamless shopping experience. All users can browse the store, read insightful articles, and complete their purchases without needing to create an account. However, registered users enjoy additional features that enhance their shopping experience. The Skin Guru is dedicated to making skincare accessible and enjoyable for all, fostering a community of informed and empowered young consumers.

____

### User Stories

**Epic - Home Page and Navigation**

As a **Site User**(all users):

* I can **view the site's home page** so that I can **understand what the site is for.** - **MUST HAVE**
* I can **use the navigation menu** so that I can **easily make my way around the site.**	- **MUST HAVE**
* I can **use the search bar** so that I can **search for a specific item.** - **MUST HAVE**
* I can **shop products by “Skin Type” or “Product Type”** so that I can **view all available products in that category.** - **MUST HAVE**
* I can **create an account easily from the navbar** so that I can **log in to the site.** - **MUST HAVE**
* I can **log in to my account easily from the navbar** so that I can **manage my account.** - **MUST HAVE**
* I can **click the Cart button in the navbar** so that I can **view the products in my cart.** - **MUST HAVE**


As a **Registered User:**

* I can **access my Wishlist from the navbar** so that I can **view the products in my wishlist.** - **COULD HAVE**

<br>
<br>

**Epic - Registration**

As a **Site User** (all users):

* I can **register an account** so that I can **manage my order history, add products to my wishlist, save my personal details for faster checkout, leave a review on products I’ve purchased, add comments to blogs.** - **MUST HAVE**


As a **Registered User:**

* I can **edit my personal details on my account** so that I can **keep them up to date.** - **MUST HAVE**

<br>
<br>

**Epic - Products**

As a **Site User** (all users):

* I can **sort the products displayed on each product page** so that I can **filter the products to improve my search criteria.** - **MUST HAVE**
* I can **click an individual product** so that I can **view its details.** - **MUST HAVE**
* I can **click a -/+ button on a products details page** so that I can **manage the quantity of the product I want to add to the cart.** - **MUST HAVE**
* I can **click “Add to cart” button on a products details page** so that I can **add to the product to the cart to purchase.** - **MUST HAVE**


As a **Site Admin:**

* I can **add a product to my site** so that I can **increase the range of products available on the site.** - **MUST HAVE**
* I can **edit existing products** so that I can **change the products description, price or image etc.**	- **MUST HAVE**
* I can **delete a product from my site** so that I can **remove it from sale.** - **MUST HAVE**

<br>
<br>

**Epic - Cart**

As a **Site User** (all users):

* I can **adjust quantities of products in my cart** so that I can **change the quantity of the product that I wish to purchase.** - **MUST HAVE**
* I can **click "remove" on a product in my cart** so that I can **remove a product from my cart before checkout.** - **MUST HAVE**

<br>
<br>

**Epic - Checkout**

As a **Site User** (all users):

* I can **go to checkout** so that I can **complete my purchase.** - **MUST HAVE**
* I can **view my order before checkout** so that I can **confirm my items for purchase.** - **MUST HAVE**
* I can **enter/update my delivery details** so that I can **provide the correct delivery and contact information.** - **MUST HAVE**
* I can **view my order summary details** so that I can **review my order after it is placed.** - **MUST HAVE**
* I can **receive an email after purchase** so that I can **have confirmation and record of my purchase.** - **MUST HAVE**


As a **Registered User:**

* I can **see my previously saved details already populated at checkout** so that I can **complete my purchases faster.** - **MUST HAVE**

<br>
<br>

**Epic - Blog Articles**

As a **Site User** (all users):

* I can **read blog articles** so that I can **stay up to date with the latest skincare information.** - **SHOULD HAVE**
* I can **view comments on articles** so that I can **see the conversation around the articles subject.** - **SHOULD HAVE**


As a **Registered User:**

* I can **add comments to articles** so that I can **join in the conversation.** - **SHOULD HAVE**
* I can **edit/update/delete my comments** so that I can **manage my comments on blog articles.** - **SHOULD HAVE**


As a **Site Admin:**

* I can **create, read, update, delete Blog Articles** so that I can **manage my content.** - **SHOULD HAVE**
* I can **approve/decline comments** so that I can **manage the comments section.** - **SHOULD HAVE**

<br>
<br>

**Epic - Contact Form**

As a **Site User** (all users):

* I can **fill out a contact form** so that I can **contact the business with any queries I may have.** - **COULD HAVE**


As a **Site Admin:**

* I can **store contact form submissions** so that I can **review them.** - **COULD HAVE**
* I can **mark contact form submissions as read** so that I can see **how many I still need to process.** - **COULD HAVE**

<br>
<br>

**Epic - Product Reviews**

As a **Site User** (all users):

* I can **view reviews on a product** so that I can **see other users feedback.** - **SHOULD HAVE**


As a **Registered User:**

* I can **create a review on a product I have purchased** so that I can **give feedback to the site owners and other users.** - **SHOULD HAVE**
* I can **edit/update/delete my review** so that I can **manage my reviews.** - **SHOULD HAVE**


As a **Site Admin:**

* I can **approve/decline reviews** so that I can **filter out negative reviews.** - **SHOULD HAVE**

<br>
<br>

**Epic - Wishlist**

As a **Registered User:**

* I can **click the 'Add to Wishlist' button** so that I can **keep a record of my favourite items.** - **COULD HAVE**
* I can **click the 'Wishlist’ heart icon** so that I can **see all the products in my Wishlist.** - **COULD HAVE**
* I can **click the 'Remove' button** so that I can **remove a product from my Wishlist.** - **COULD HAVE**
* I can **click the 'Add to cart' button** so that I can **add the product to my cart from in my Wishlist.** - **COULD HAVE**

<br>
<br>

**Epic - Newsletter**

As a **Site User** (all users):

* I can **enter my email into the newsletter form** so that I can **receive marketing emails about new products, promotions and skincare tips.** - **MUST HAVE**

<br>
<br>

**Epic - Emails**

As a **Site User** (all users):

* I can **receive an email after purchase** so that I can **view my order summary.** - **MUST HAVE**


As a **Registered User:**

* I can **receive a confirmation email upon registering an account** so that I can **verify my account.** - **MUST HAVE**

<br>

____

### Agile Development

<br>

____

### UX

#### Strategy

* **User Engagement:** The website will prioritize a user-friendly interface with simple navigation and clear CTAs encouraging users to explore products, read blog posts, and make purchases. Features such as quick access to product descriptions, easy-to-use search functionality, and a streamlined checkout process will enhance user interaction and increase conversion rates.

* **Brand Positioning:** The Skin Guru will be positioned as a go-to destination for young skincare enthusiasts, emphasizing its commitment to education and quality products. The website will showcase a curated selection of skincare items, complemented by informative content, creating an emotional connection with the target audience.


#### Scope

* **User Types:** The site will cater to two primary user groups: unregistered users who can browse products, read blog posts, and make purchases, and registered users who can save their information, view order history, and access personalized features.

* **Core Features:** Key functionalities will include a comprehensive product catalog with detailed descriptions and pricing, an intuitive search and filter system, an informative blog section, a simple account registration process, and a secure checkout system for both guest and registered users.


#### Structure

* **Information Hierarchy:** The site's information architecture will prioritize essential content. The homepage will feature direct links to popular product categories, latest blog posts, and login/register options, ensuring users can easily find what they need. As well as a newsletter sign up form to encourage users to keep informed of new launched, discounts and promotions, as well as receiving monthly skin tips.

* **Content Strategy:** Engaging blog article content will be developed that highlights product benefits, ingredients, and usage tips. The blog will feature skincare advice, trends, and educational content, building trust and encouraging product exploration.


#### Skeleton

##### Wireframes
Wireframes will be created for key pages including:
* **Homepage** (featuring bestsellers and latest blog posts)
* **Product catalog** (with filter and sort options)
* **Product detail page** (with comprehensive information and reviews)
* **Blog section** (with categorized articles)
* **User account dashboard** (showing order history and saved items)
* **Checkout process** (streamlined for both guest and registered users)


#### Surface

* **Visual Identity:** A fresh and vibrant color palette will be chosen to appeal to the young target audience. Typography will be selected for readability while reflecting a modern, trendy aesthetic that aligns with The Skin Guru's brand identity.

* **Responsive Design:** The website design will be fully responsive, ensuring optimal functionality across all devices - smartphones, tablets, and desktops. This is crucial for the target demographic who are likely to shop on mobile devices.

* **Accessibility Features:** Features like alt text for images, keyboard navigation options, and screen reader compatibility will be implemented to ensure inclusivity.

* **Feedback Mechanisms:** Visual feedback mechanisms in the form of confirmation messages for added products, successful purchases, and account actions will be implemented to enhance user experience and build trust.

<br>

____

### Design

#### Color Scheme
For The Skin Guru, the color palette was chosen to capture the essence of youthful energy and showcase brigh attractive colors:

* **Hot Pink** (#FFAEBC): Radiating vibrant energy, this bold shade embodies the spirited and confident nature of our young target audience.
* **Tiffany Blue** (#A0E7E5): A sophisticated yet playful hue that bridges elegance with youthful freshness. 
* **Mint** (#B4F8C8): A refreshing shade that evokes the clean, pure essence of skincare. It symbolizes the brand's focus on natural, gentle products that nurture young skin, creating a sense of calm and rejuvenation.
* **Soft Yellow** (#FBE7C6): Bringing warmth and optimism, this gentle tone represents the joy and positivity of effective skincare. It adds a cheerful, welcoming element that resonates with our young, enthusiastic audience.

![Screenshot of The Skin Guru colour palette](documentation/the-skin-guru-color-palette.png) 

<br>

#### Logo

I created my logo for The Skin Guru on [Logo.com](https://logo.com)

![Screenshot of The Skin Guru Logo](documentation/the-skin-guru-logo-no-bg.png) 

<br>

#### Typography

I chose the following typography for The Skin Guru on [Fontjoy.com](https://fontjoy.com/):
* **Chango** - as it’s a bold font to grab attention, but with a young and groovy vibe matching the font in my Logo.
* **Poppins** - for a modern vibe that keeps a clean aesthetic look to the site.

![Screenshot of The Skin Guru font pairing](documentation/the-skin-guru-font-pairing.png) 

<br>

#### Imagery

The Images for this project were sourced from [SkinShop.ie](https://skinshop.ie/)

<br>

____

### Database ERD

<br>

____

### Project Features

<br>

____
### Future Features

<br>

____

### Marketing

#### Content Marketing
#### SEO
#### Social Media

<br>

____

### Technologies Used
#### Languages
#### Frameworks, Libraries, Technologies and Programs used

<br>

____

### Testing

<br>

____

### Deployment
#### Forking the GitHub Repository
#### Clone the GitHub Repository
#### Django Project Setup
#### Database Creation
#### Cloudinary
#### Deploying to Heroku

<br>

____

### Credits
#### Code References
#### Content and Media References

<br>

____

###Acknowledgements

<br>

____