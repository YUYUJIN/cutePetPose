import React from 'react';
import './Analyze.css';
import LogoComponent from './component/logoComponent';
import { Album, Home } from './component/ButtonWithNavigation';
import 'bootstrap/dist/css/bootstrap.min.css';
import MyTabs from './component/analyzeTab.jsx'

// const navigateLinkAnalyze = useNavigate();
// const analyzeNavigateToAlbum = () => {
//   navigateLinkAnalyze('/Album');
// };
function Analyze() {
  return (
    <div className="analyze">
      <LogoComponent />
      <div className='graph'>
        <MyTabs />
        <div className='linkedButtonList'>
          <div className='gList'>
            {/* <MyResponsiveLine className='graphNivo' data={petData[2].data} /> */}
            <div className='buttonList'>
              <Home />

            </div>
            <div className='buttonList'>
              <Album />

            </div>

          </div>
        </div>
      </div>
    </div>
  );
}


export default Analyze;
