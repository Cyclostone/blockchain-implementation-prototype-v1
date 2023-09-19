import React from "react";
import ReactDOM from "react-dom";
import { Router, Switch, Route } from "react-router-dom";
import { createBrowserHistory } from "history";
import "./index.css";
import App from "./components/App";
import Blockchain from "./components/Blockchain";
import ConductTransaction from "./components/ConductTransaction";

ReactDOM.render(
  <Router history={createBrowserHistory()}>
    <Switch>
      <Route path="/" exact={true} component={App} />
      <Route path="/blockchain" component={Blockchain} />
      <Route path="/conduct-transaction" component={ConductTransaction} />
    </Switch>
  </Router>,
  document.getElementById("root")
);
