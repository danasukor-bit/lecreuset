const BC_KEY = process.env.BC_KEY;

const CORS = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Headers': 'Content-Type',
  'Access-Control-Allow-Methods': 'GET, OPTIONS',
  'Content-Type': 'application/json',
};

exports.handler = async function(event) {
  if (event.httpMethod === 'OPTIONS') {
    return { statusCode: 204, headers: CORS, body: '' };
  }

  const id = event.queryStringParameters && event.queryStringParameters.id;
  if (!id) {
    return { statusCode: 400, headers: CORS, body: JSON.stringify({ error: 'id obrigatório' }) };
  }

  try {
    const response = await fetch('https://api.blackcatpay.com.br/api/sales/' + encodeURIComponent(id), {
      headers: { 'X-API-Key': BC_KEY },
    });
    const data = await response.json();
    console.log('check-pix-status', id, '->', JSON.stringify(data).substring(0, 300));
    return { statusCode: 200, headers: CORS, body: JSON.stringify(data) };
  } catch(err) {
    return { statusCode: 500, headers: CORS, body: JSON.stringify({ error: err.message }) };
  }
};
