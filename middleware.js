export const config = {
  matcher: '/(.*)',
};

export default function middleware(request) {
  const authorizationHeader = request.headers.get('authorization');
  
  if (authorizationHeader) {
    const basicAuth = authorizationHeader.split(' ')[1];
    
    // btoa/atob are supported in Edge runtimes
    const [user, password] = atob(basicAuth).split(':');
    
    // Auth Check
    if (user === 'funter_netturbo' && password === 'n3tturb0_!qaz') {
      // Allow access by doing nothing
      return; 
    }
  }

  // If not authenticated, challenge the request
  return new Response('Acesso negado. Por favor, faca login com as credenciais da NetTurbo.', {
    status: 401,
    headers: {
      'WWW-Authenticate': 'Basic realm="Dash Funter Privado"',
    },
  });
}
