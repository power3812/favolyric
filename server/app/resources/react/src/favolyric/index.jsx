// 必要なものをインポートする．
import React from 'react'
import ReactDOM from 'react-dom'

// Reactコンポーネントを作る．
class Favolyric extends React.Component {
    constructor() {
        super();
    }

    // レンダリングされる部分を実装する．
    render() {
        return (
            <h1> Hello, React!! </h1>
        );
    }
}

// Htmlと紐付けを行う．ここでは，`home`というidがつけられたタグとHomeコンポーネントを紐付けるよう設定している
ReactDOM.render(
    <Favolyric />,
    document.getElementById('favolyric')
);
