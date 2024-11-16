Deno.serve(
    { hostname: "localhost", port: 8080 },
    (request) => {
      const url = new URL(request.url);
      const filepath = decodeURIComponent(url.pathname);
    },
  );  