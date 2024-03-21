# ~~CloThings~~ - A cool clothing store

This is a simple clothing store website made to teach the basics of web development.

## Technologies

- **HTML/HTMX** *(with Jinja2 templating)*
- **FastAPI** *(backend)*
- **In-memory "dictionary" database** *(no real database)*

## Features

- **PAGES**
  - [ ] Home page *(Description of the store)*
  - [ ] List of the products
  - [ ] Checkout the cart

- **FUNCTIONALITIES**
  - [ ] Navigation bar
  - [ ] Add products to the cart
  - [ ] Remove products from the cart

## Installation

```bash
# Optional: Create a virtual environment
python3 -m venv env
source env/bin/activate

# Install the dependencies
pip install fastapi[all]
pip install uvicorn
```

## Running the server

```bash
# Run the server
# --reload flag is optional and enables hot reloading if any files are changed
uvicorn main:app --reload --reload-include static/ --reload-include templates/
```

## TODO

- [ ] Finish cleanly the project.
- [ ] Make sure the project is well documented.
- [ ] Do not use advanced concepts.
- [ ] Split the project into multiple steps.
  - **Step 1 :** Start the backend *(Understand the basics of a web server, routing, and templating)*
  - **Step 2 :** Add multiple pages *(Understand the basics of navigation)*
  - **Step 3 :** Pass data to the templates *(Understand the basics of data management)*
  - **Step 4 :** Create the database *(ie: Outfits and pass them to the templates)*
  - **Step 5 :** API *(Understand the basics of APIs)*
  - **Step 6 :** Add to cart *(Understand the basics of state management with HTMX and the backend)*
  - **Step 7 :** Delete from cart
  - **Step 8 :** Checkout *(A fake payment system)*

## Future improvements

Those are improvements that can be made to the project to make it more complex and interesting. They are not necessary for the project to be complete.

- [ ] Publish the website
- [ ] Product categories
  - [ ] Add a filter to the products list page
  - [ ] Combine filters *(ie: Filter by category and price)*
- [ ] Add a login system
- [ ] Add a real database *(For data persistance)*
- [ ] Product recommendation
- [ ] Product reviews and ratings
