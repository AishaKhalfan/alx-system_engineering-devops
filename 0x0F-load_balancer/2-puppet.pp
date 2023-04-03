# 2-puppet_custom_http_response_header.pp

# Install Nginx
class { '::nginx':
  ensure => installed,
}

# Define the custom HTTP header
$server_name = $::hostname
nginx::resource::server { 'default':
  listen => ['80', '443 ssl'],
  server_name => '_',
  ssl => true,
  ssl_certificate => '/etc/nginx/ssl/nginx.crt',
  ssl_certificate_key => '/etc/nginx/ssl/nginx.key',
  location => {
    '/' => {
      # Add the custom HTTP header
      add_header => [
        'X-Served-By "${server_name}"',
      ],
      # Serve a simple message
      content => 'Hello world!',
    },
  },
}

