# Execute a command using puppt
exec { 'killmenow':
  command => 'pkill killmenow',
  path    => ['/bin', '/usr/bin', '/usr/local/bin'],
  onlyif  => 'pgrep killmenow',
}

