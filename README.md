# aura-insurance-engine
A lightweight vanilla Django API for managing multi-carrier insurance application workflows with tokenized form links and submission tracking.

## Steps to run locally

1. **Clone the repository**
   ```sh
   git clone <your-repo-url>
   cd aura-insurance-engine
   ```

2. **Create and activate a Python virtual environment**
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Create a `.env` file and add your Django `SECRET_KEY`**
   - Create a file named `.env` in the project root directory.
   - Add the following line (replace with your own secret key):
     ```
     SECRET_KEY=your-very-secret-key
     ```

5. **Apply database migrations**
   ```sh
   python manage.py migrate
   ```

6. **Seed the database with carriers**
   ```sh
   python manage.py seed_carriers
   ```

7. **Seed the database with coverage lines**
   ```sh
   python manage.py seed_coverage
   ```

8. **Seed the database with common insurance questions**
   ```sh
   python manage.py seed_questions
   ```

9. **Create a superuser to access the admin interface**
   ```sh
   python manage.py createsuperuser
   ```

10. **Run the development server**
    ```sh
    python manage.py runserver
    ```

Access the admin interface at [http://localhost:8000/admin/](http://localhost:8000/admin/)