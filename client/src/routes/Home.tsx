import { getInfra } from "../api";
import styled from "styled-components";
import { useQuery } from "react-query";
import Header from "../components/Header";
import MenuBar from "../components/MenuBar";
import { Switch, Route } from "react-router-dom";
import Cost from "../screens/Cost";
import Infra from "../screens/Infra";

interface IInfra {
  tmp: null;
}

const Container = styled.div`
  display: flex;
  flex-direction: row;
  width: 100vw;
  overflow: hidden;
`;
const ContentBox = styled.div`
  padding-left: ${(props) => props.theme.menuWidth};
  width: 100%;
`;

const Home = () => {
  const { isLoading, data } = useQuery<any>("allInfra", getInfra);
  console.log(data);
  return (
    <>
      <Header />
      <Container>
        <MenuBar />
        <ContentBox>
          <Switch>
            <Route path={`/`} exact>
              <Infra />
            </Route>
            <Route path={`/cost`}>
              <Cost />
            </Route>
          </Switch>
        </ContentBox>
      </Container>
    </>
  );
};

export default Home;
