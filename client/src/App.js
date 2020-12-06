import { BrowserRouter as Router, Route, Link, Switch } from 'react-router-dom';
import { Button } from '@material-ui/core';
import SignIn from './containers/SignIn';
import { makeStyles } from '@material-ui/core/styles';

function App() {
  return (
    <div>
      <Switch>
        <Route exact path="/" />
        <Route path="/sign-in" component={SignIn} />
      </Switch>
      <Button
        variant="contained"
        color="primary"
        to="/sign-in"
        component={Link}
      >
        会員登録
      </Button>
      <Button variant="contained" color="primary" to="/" component={Link}>
        ホーム
      </Button>
    </div>
  );
}

export default App;
