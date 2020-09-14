require('@babel/register');
const path = require('path');

module.exports = {
    // 読み込むjsxファイルの名前と読み込み場所の設定
    entry: {
        favolyric_index:     path.resolve(__dirname, "src/favolyric/index.jsx"),
    },
    // 出力するjsファイルの場所と名前の設定
    output: {
        path: path.resolve(__dirname, "../static/js/") ,
        filename: "[name].js",
    },
    module: {
        rules: [
            {
                test: /\.jsx$/,
                exclude: /node_modules/,
                loader: 'babel-loader'
            }
        ]
    },
    resolve: {
        extensions: [".js","jsx"],
    }
}
