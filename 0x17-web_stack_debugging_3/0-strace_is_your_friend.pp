# Fix the server
exec {'fix_typo':
  path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php"
}
