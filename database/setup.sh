docker volume create goodreads-data-volume
docker run --name=goodreads-mysql-container -p3306:3306 -v goodreads-data-volume:/var/lib/mysql --env db.env -d mysql:5.7.31 --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci
