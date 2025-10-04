#!/usr/bin/env python
"""
Setup script for Dr. Paul Mwambu Portfolio Website
Run this script to set up the development environment
"""

import os
import sys
import subprocess
import shutil


def run_command(command, description):
    """Run a command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e.stderr}")
        return False


def check_requirements():
    """Check if required tools are installed"""
    print("🔍 Checking requirements...")
    
    # Check Python
    if shutil.which("python") is None:
        print("❌ Python is not installed or not in PATH")
        return False
    
    # Check Node.js
    if shutil.which("node") is None:
        print("❌ Node.js is not installed or not in PATH")
        return False
    
    # Check npm
    if shutil.which("npm") is None:
        print("❌ npm is not installed or not in PATH")
        return False
    
    print("✅ All requirements are met")
    return True


def setup_environment():
    """Set up the development environment"""
    print("🚀 Setting up Dr. Paul Mwambu Portfolio Website...")
    
    if not check_requirements():
        print("❌ Requirements check failed. Please install the required tools.")
        return False
    
    # Create virtual environment
    if not os.path.exists("venv"):
        if not run_command("python -m venv venv", "Creating virtual environment"):
            return False
    
    # Activate virtual environment and install Python dependencies
    if sys.platform == "win32":
        activate_cmd = "venv\\Scripts\\activate"
        pip_cmd = "venv\\Scripts\\pip"
    else:
        activate_cmd = "source venv/bin/activate"
        pip_cmd = "venv/bin/pip"
    
    if not run_command(f"{pip_cmd} install --upgrade pip", "Upgrading pip"):
        return False
    
    if not run_command(f"{pip_cmd} install -r requirements.txt", "Installing Python dependencies"):
        return False
    
    # Install Node.js dependencies
    if not run_command("npm install", "Installing Node.js dependencies"):
        return False
    
    # Build CSS
    if not run_command("npm run build-css-prod", "Building CSS"):
        return False
    
    # Create .env file if it doesn't exist
    if not os.path.exists(".env"):
        if os.path.exists("env.example"):
            shutil.copy("env.example", ".env")
            print("✅ Created .env file from env.example")
        else:
            print("⚠️  Please create a .env file with your configuration")
    
    # Run migrations
    if not run_command(f"{activate_cmd} && python manage.py migrate", "Running database migrations"):
        return False
    
    # Create superuser (optional)
    print("👤 Would you like to create a superuser? (y/n): ", end="")
    create_superuser = input().lower().strip()
    if create_superuser in ['y', 'yes']:
        run_command(f"{activate_cmd} && python manage.py createsuperuser", "Creating superuser")
    
    # Populate sample data (optional)
    print("📊 Would you like to populate the database with sample data? (y/n): ", end="")
    populate_data = input().lower().strip()
    if populate_data in ['y', 'yes']:
        run_command(f"{activate_cmd} && python manage.py populate_sample_data", "Populating sample data")
    
    print("\n🎉 Setup completed successfully!")
    print("\n📋 Next steps:")
    print("1. Activate the virtual environment:")
    if sys.platform == "win32":
        print("   venv\\Scripts\\activate")
    else:
        print("   source venv/bin/activate")
    print("2. Start the development server:")
    print("   python manage.py runserver")
    print("3. Open your browser and go to: http://localhost:8000")
    print("4. Access the admin panel at: http://localhost:8000/admin")
    
    return True


if __name__ == "__main__":
    setup_environment()
