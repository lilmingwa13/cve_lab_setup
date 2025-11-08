FROM wordpress:6.4-apache

# Install Xdebug (for PHP 8.x adjust package if necessary)
RUN apt-get update && apt-get install -y --no-install-recommends \
        git unzip libzip-dev libpng-dev libonig-dev \
    && pecl install xdebug \
    && docker-php-ext-enable xdebug \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY ./xdebug.ini /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini
