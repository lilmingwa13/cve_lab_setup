FROM wordpress:6.2-apache

# Install Xdebug (for PHP 8.x adjust package if necessary)
RUN apt-get update && apt-get install -y --no-install-recommends \
        git unzip libzip-dev libpng-dev libonig-dev \
    curl \
    && pecl install xdebug \
    && docker-php-ext-enable xdebug \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

#
# THÊM DÒNG NÀY ĐỂ BẬT MOD_REWRITE VĨNH VIỄN
#
RUN a2enmod rewrite

# 2. CHO PHÉP Apache đọc .htaccess (BƯỚC QUAN TRỌNG NHẤT)
# Sửa file config Apache để đổi "AllowOverride None" thành "AllowOverride All"
RUN sed -i 's/AllowOverride None/AllowOverride All/g' /etc/apache2/apache2.conf


COPY ./xdebug.ini /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini
