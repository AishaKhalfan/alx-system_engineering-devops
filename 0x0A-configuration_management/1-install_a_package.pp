# installing flask using pip3 in puppet
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
