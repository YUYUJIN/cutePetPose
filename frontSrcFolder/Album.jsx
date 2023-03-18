import React, { useState } from 'react';
import { Tabs } from 'antd';
import './Album.css';
import LogoComponent from './component/logoComponent';
import { checkBoxCat } from './Main';
import { dummy } from './movie';
import M from './m';
import { Analyze, Home } from './component/ButtonWithNavigation';

const { TabPane } = Tabs;

function Album() {
    const [activeKey, setActiveKey] = useState('dog');

    const onChange = (key) => {
        setActiveKey(key);
    };

    return (
        <div className='album'>
            <LogoComponent />
            <div className='albumTab'>
                <Tabs onChange={onChange} type="card" style={{fontFamily:'jua', letterSpacing:1}}>
                    {checkBoxCat.map((option, index) => (
                        <TabPane className='videoList' tab={option.label} key={option.value} >
                            <div className='mList'>
                                {dummy.results
                                    .slice((index * 9), (index * 9) + 9)
                                    .map((item, index) => (
                                        <M
                                            key={index}
                                            title={item.title}
                                            poster_path={item.poster_path}
                                            vote_average={item.vote_average}
                                        />
                                    ))
                                }
                            </div>
                        </TabPane>
                    ))}
                </Tabs>
                <div className='albumButtonList'>
                    <div className='buttonList'>
                        <Home />

                    </div>
                    <div className='buttonList'>
                        <Analyze />

                    </div>
                </div>
            </div>
        </div>
    );
}

export default Album;