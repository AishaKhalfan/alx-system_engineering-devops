# Change the OS configuration so that it is possible to login with 
# the holberton user and open a file without any error message.
file { '/etc/security/limits.conf':
  ensure  => present,
  content => "holberton hard nofile 88888\nholberton soft nofile 88888\n",
}

exec { 'reload-limits-configuration':
  command => 'pam-auth-update --force',
  path    => '/usr/bin:/usr/sbin:/bin',
  refreshonly => true,
}

service { 'systemd-logind':
  ensure => running,
  enable => true,
  require => [File['/etc/security/limits.conf'], Exec['reload-limits-configuration']],
}
