# open files
exec {'fix_name':
  path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  command => "sed -i 's/15/1000/g' /etc/default/nginx && service nginx restart"
}
