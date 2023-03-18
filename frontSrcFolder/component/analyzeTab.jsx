import { Tabs } from 'antd';
import { MyResponsiveLine, petData } from './graph';
import './analyzeTab.css';

const { TabPane } = Tabs;

const onChange = (key) => {
    console.log(key);
};

const App = () => (
    <div className='nivoContainer'>

    <Tabs onChange={onChange} type="card" style={{fontFamily:'jua',letterSpacing:1}}>
        {petData.map((option, index) => (
            <TabPane tab={option.label} key={option.keys}>
                <div className='tabNivo'>

                    <MyResponsiveLine data={option.data} />
                </div>
            </TabPane>
        ))}
    </Tabs>
        </div>
);

export default App;