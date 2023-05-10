class strace_is_your_friend {

  package { 'libapache2-mod-php7.0':
    ensure => installed,
  }

  service { 'apache2':
    ensure => running,
    enable => true,
  }

}
