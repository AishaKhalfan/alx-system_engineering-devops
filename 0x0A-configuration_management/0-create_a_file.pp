# create a file with specifications

file { '/tmp/school':
  ensure  => 'file',
  content => 'I love Puppet',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
}
