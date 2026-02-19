#!/bin/bash
# Creates the application database on the first startup (empty volume).
# Only runs when /data/db has no data (WiredTiger, etc).
set -e
echo "[init-mongo.sh] Creating database back-end-stores-db..."
mongosh "mongodb://mongousr:mongopwd@localhost:27017/?authSource=admin" --eval 'db.getSiblingDB("back-end-stores-db").createCollection("_init"); db.getSiblingDB("back-end-stores-db")._init.insertOne({ initialized: true, at: new Date() });'
echo "[init-mongo.sh] Done."
