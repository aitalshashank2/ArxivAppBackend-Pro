# Endpoints

## Backend

### Endpoints and Model Info

- **User** - /user/ - Logging in
	- Name and other details from Google OAuth Server

- **Paper**: GET - /paper/?q="query" | ViewSet - /paper/
	- arxiv\_url
	- arxiv\_comment
	- authors
	- links
	- published
	- title

- **Blog** : ViewSet - /blogs/
	- Title
	- Body
	- Author : Foreignkey
	- Date
	- Upvotes : ForeignKey

- Authentication: OAuth2.0

- Admin
