addEventListener('fetch', evento => {
	evento.respondWith(handleRequest(evento.request));
  });

  async function handleRequest(request) {
	let url = new URL(request.url);

	url.searchParams.set('width', '800');
	url.searchParams.set('height', '600');

	let modifiedRequest = new Request(url.toString(), {
	  method: request.method,
	  headers: request.headers
	});

	let cache = caches.default;
	let response = await cache.match(modifiedRequest);

	if (!response) {
	  response = await fetch(modifiedRequest);
	  let cacheHeaders = new Headers(response.headers);
	  cacheHeaders.set('Cache-Control', 'public, max-age=14400');
	  response = new Response(response.body, {
		status: response.status,
		statusText: response.statusText,
		headers: cacheHeaders
	  });
	  evento.waitUntil(cache.put(modifiedRequest, response.clone()));
	}

	return response;
  }
