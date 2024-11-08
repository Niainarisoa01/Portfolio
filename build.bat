@echo off
IF NOT EXIST static\css mkdir static\css
npx tailwindcss -i ./static/src/input.css -o ./static/css/output.css --minify 