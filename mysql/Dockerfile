# Use the latest MySQL base image
FROM mysql:latest

# Copy custom my.cnf file to set bind address
COPY my.cnf /etc/mysql/conf.d/my.cnf

# Copy SQL initialization script to set up database and table
COPY database_students.sql /docker-entrypoint-initdb.d/
