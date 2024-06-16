# social_media

### 1. Low-Level Design (LLD)

#### 1.1. Component Breakdown
- **Backend (Django):**
  - User Management
  - Authentication
  - Discussion Management
  - Comments and Likes Management
  - Search Functionality
  - Follower System
- **Frontend (React):**
  - User Interface for login/signup
  - User Profile
  - Feed for Discussions
  - Search UI
  - Post and Comment Management UI

#### 1.2. System Architecture Diagram
- **Frontend (React)**
  - Components
    - Login/Signup Component
    - User Profile Component
    - Discussion Feed Component
    - Post Component
    - Comment Component
    - Search Component

- **Backend (Django REST Framework)**
  - API Endpoints
    - User Endpoints (CRUD operations)
    - Discussion Endpoints (CRUD operations, search by text and tags)
    - Comment Endpoints (CRUD operations)
    - Like Endpoints (CRUD operations)
    - Authentication Endpoints (Login/Signup)
    - Follow Endpoints (Follow/Unfollow users)

#### 1.3. Database Schema
- **User**
  - id (Primary Key)
  - name
  - mobile (unique)
  - email (unique)
  - password
  - created_at
  - updated_at

- **Discussion**
  - id (Primary Key)
  - user (ForeignKey to User)
  - text
  - image (optional)
  - created_at
  - updated_at

- **Hashtag**
  - id (Primary Key)
  - name

- **DiscussionHashtag**
  - id (Primary Key)
  - discussion (ForeignKey to Discussion)
  - hashtag (ForeignKey to Hashtag)

- **Comment**
  - id (Primary Key)
  - user (ForeignKey to User)
  - discussion (ForeignKey to Discussion)
  - text
  - created_at
  - updated_at

- **Like**
  - id (Primary Key)
  - user (ForeignKey to User)
  - discussion (ForeignKey to Discussion)
  - comment (ForeignKey to Comment, optional)

- **Follow**
  - id (Primary Key)
  - follower (ForeignKey to User)
  - followee (ForeignKey to User)

#### 1.4. API Documentation
- **User Endpoints**
  - POST /api/users/ - Create User
  - PUT /api/users/{id}/ - Update User
  - DELETE /api/users/{id}/ - Delete User
  - GET /api/users/ - List Users
  - GET /api/users/search/?name={name} - Search User by Name

- **Discussion Endpoints**
  - POST /api/discussions/ - Create Discussion
  - PUT /api/discussions/{id}/ - Update Discussion
  - DELETE /api/discussions/{id}/ - Delete Discussion
  - GET /api/discussions/?tags={tags} - Get Discussions by Tags
  - GET /api/discussions/search/?text={text} - Get Discussions by Text

- **Comment Endpoints**
  - POST /api/comments/ - Create Comment
  - PUT /api/comments/{id}/ - Update Comment
  - DELETE /api/comments/{id}/ - Delete Comment

- **Like Endpoints**
  - POST /api/likes/ - Like a Post or Comment
  - DELETE /api/likes/{id}/ - Unlike a Post or Comment

- **Follow Endpoints**
  - POST /api/follows/ - Follow User
  - DELETE /api/follows/{id}/ - Unfollow User

### 2. Microservice Architecture
For simplicity and scalability, you can break the application into the following microservices:
- **User Service**
  - Handles user registration, authentication, and profile management.
- **Discussion Service**
  - Manages creating, updating, and deleting discussions.
- **Comment Service**
  - Manages comments on discussions.
- **Like Service**
  - Manages likes on posts and comments.
- **Follow Service**
  - Manages following and unfollowing of users.
- **Search Service**
  - Handles searching users and discussions.

### 3. Project Implementation

#### 3.1. Backend (Django)
1. **Setup Django Project and Apps**
   ```bash
   django-admin startproject social_media
   cd social_media
   django-admin startapp users
   django-admin startapp discussions
   django-admin startapp comments
   django-admin startapp likes
   django-admin startapp follows
   ```

#### 3.2. Frontend (React)
1. **Setup React Project**
   ```bash
   npx create-react-app social-media-client
   cd social-media-client
   ```

2. **Install Dependencies**
   - Use Axios for API calls.
   - React Router for navigation.
