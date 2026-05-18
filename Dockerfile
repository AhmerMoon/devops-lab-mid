# Nginx ka lightweight web server use kar rahe hain
FROM nginx:alpine

# Apni index.html file ko Nginx ke default folder me copy karna
COPY index.html /usr/share/nginx/html/index.html

# Port 80 open karna
EXPOSE 80