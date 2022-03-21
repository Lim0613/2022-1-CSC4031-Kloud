import { BrowserRouter, Switch, Route } from "react-router-dom";
import Home from "./route/Home";
import Login from "./route/Login";
import { useRecoilValue } from "recoil";
import { isLoggedInAtom } from "./atoms";

const Router = () => {
  const isLoggedIn = useRecoilValue(isLoggedInAtom);
  return (
    <BrowserRouter>
      <Switch>
        <Route path="/" exact>
          {isLoggedIn ? <Home /> : <Login />}
        </Route>
      </Switch>
    </BrowserRouter>
  );
};

export default Router;