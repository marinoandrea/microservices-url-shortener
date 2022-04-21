const proxy  = require('http-proxy-middleware');

module.exports = function (app) {
    app.use('/userservice',
        proxy.createProxyMiddleware( { 
            target: 'http://localhost:5001',
            changeOrigin: true,
            pathRewrite: { '^/userservice': '' }
        })
    
    ),
    app.use('/urlshortener',
        proxy.createProxyMiddleware( {
            target: 'http://localhost:5000',
            changeOrigin: true,
            pathRewrite: { '^/urlshortener': '' }
    }));
}