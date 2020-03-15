const webpack = require('webpack');
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const OpenBrowserWebpackPlugin = require('open-browser-webpack-plugin');
const packagePath = relPath => path.resolve(__dirname, relPath);
const TsConfigPathsPlugin = require('awesome-typescript-loader').TsConfigPathsPlugin;

module.exports = {
    entry: ['./src/index'],
    mode: 'development',
    output: {
        path: packagePath('dist'),
        publicPath: '/',
        filename: '[name].js',
    },

    // Enable sourcemaps for debugging webpack's output.
    devtool: 'source-map',
    plugins: [
        new OpenBrowserWebpackPlugin(),
        new webpack.NamedModulesPlugin(),
        new HtmlWebpackPlugin({
            title: 'WellDone',
            template: packagePath('./src/index.html'),
        }),
    ],
    resolve: {
        // Add '.ts' and '.tsx' as resolvable extensions.
        extensions: ['.ts', '.tsx', '.js', '.json', '.css'],
        modules: [
            packagePath('node_modules'),
        ],
        plugins: [
            new TsConfigPathsPlugin()
        ]
    },
    module: {
        rules: [
            {
                test: /\.css$/,
                use: [
                    {
                        loader: 'style-loader',
                        options: {
                          esModule: true,
                        }
                    },
                    {
                        loader: 'css-modules-typescript-loader',
                    },
                    {
                        loader: 'css-loader',
                        options: {
                          modules: true,
                        },
                    },
                ],
            },
            { enforce: 'pre', test: /\.js$/, loader: 'source-map-loader' },
            {
                test: /\.tsx?$/,
                loader: 'awesome-typescript-loader',
                query: {
                    useTranspileModule: true,
                    useBabel: true,
                    useCache: true,
                    cacheDirectory: '.cache',
                    reportFiles: ['src/**/*.{ts,tsx}'],
                },
            },
            {
              test: /\.(png|jpg|gif)$/,
              use: [
                {
                  loader: 'file-loader',
                  options: {},
                },
              ],
            },
        ],
    },
    devServer: {
        contentBase: packagePath('dist'),
        compress: true,
        port: 8080,
        hot: true,
        stats: 'errors-only',
    },
};
