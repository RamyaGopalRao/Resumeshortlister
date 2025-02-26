# Resume Shortlister

Resume Shortlister is a Django application that allows users to upload resumes, add job listings, and shortlist candidates using OpenAI's resume parsing capabilities.

## Architecture

The high-level architecture of the Resume Shortlister application is as follows:

1. **Client Side (Frontend)**
    - Users interact with the web interface through a browser.
    - Users can upload resumes, add job listings, and view shortlisted candidates.

2. **Web Server (Django)**
    - Handles user requests and serves HTML templates.
    - Integrates with the OpenAI API to parse resumes.
    - Contains views for uploading resumes, adding job listings, and shortlisting candidates.
    - Uses models like `Resume`, `EmployeeExperience`, `Skills`, and `JobListing`.

3. **OpenAI API**
    - Processes the resumes uploaded by users.
    - Extracts relevant information such as work experience, skills, and education.
    - Sends the extracted data back to the Django application.

4. **Database (e.g., PostgreSQL)**
    - Stores resumes, job listings, parsed employee experiences, skills, and shortlisted candidates.
    - Allows querying and retrieving data for display on the frontend.

5. **Static Files**
    - CSS stylesheets for styling the frontend.
    - JavaScript files for dynamic interactions.

Here's how this architecture can be visualized:

+-------------------+       +-----------------+       +---------------+
|                   |       |                 |       |               |
|   Client (User)   +------>+   Django Views  +------>+    OpenAI API |
|   (Frontend)      |       |                 |       |               |
|                   |       |                 |       +---------------+
+-------------------+       +--------+--------+
                                    |
                                    v
                           +--------+--------+
                           |                 |
                           |    Database     |
                           |  (PostgreSQL)   |
                           |                 |
                           +-----------------+
