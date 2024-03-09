#!/usr/bin/env python3

from random import choice as rc
from faker import Faker

# Assuming db is already initialized with app in the application code
from app import app  # Import Flask app
from models import db, Owner, Pet  # Import db instance and models

fake = Faker()

with app.app_context():
    # Clear existing data
    Pet.query.delete()
    Owner.query.delete()

    # Create fake owners
    owners = [Owner(name=fake.name()) for _ in range(50)]
    db.session.add_all(owners)
    db.session.commit()  # Committing here to ensure owners have IDs assigned

    # Create fake pets with random owners
    species = ['Dog', 'Cat', 'Chicken', 'Hamster', 'Turtle']
    pets = [Pet(name=fake.first_name(), species=rc(species), owner_id=rc(owners).id) for _ in range(100)]
    db.session.add_all(pets)
    
    db.session.commit()


