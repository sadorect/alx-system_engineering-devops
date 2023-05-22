class nginx_install {
  package { 'nginx':
    ensure => installed,
  }

  file { '/var/www/html/index.html':
    ensure  => present,
    content => 'Hello World!',
    require => Package['nginx'],
  }

  file { '/etc/nginx/sites-available/default':
    ensure  => present,
    content => "server {
                  listen 80;
                  server_name _;
                  root /var/www/html;
                  location / {
                    return 301 https://www.youtube.com;
                  }
                }",
    require => Package['nginx'],
    notify  => Service['nginx'],
  }

  file { '/etc/nginx/sites-enabled/default':
    ensure => 'link',
    target => '/etc/nginx/sites-available/default',
    require => File['/etc/nginx/sites-available/default'],
  }

  service { 'nginx':
    ensure  => running,
    enable  => true,
    require => [Package['nginx'], File['/etc/nginx/sites-enabled/default']],
  }
}

include nginx_install
