import React, { useState } from 'react';
import { Tab, Nav } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import './Album.css'
import LogoComponent from './component/logoComponent';
import { checkBoxCat } from './Main';
import { dummy } from './movie';
import M from './m';
import { Analyze, Home } from './component/ButtonWithNavigation'
function Album() {
    const [key, setKey] = useState('dog');

    return (

        <div className='album'>
            <LogoComponent />
            <div className='albumTab'>

                <Tab.Container activeKey={key} onSelect={setKey}>
                    {/* <div className='tabMenu'>
                        <Nav variant="pills" >
                            {checkBoxCat.map((option) => (
                                <Nav.Item className='tabElements'>
                                    <Nav.Link eventKey={option.value} >{option.label}</Nav.Link>
                                </Nav.Item>

                            ))}
                        </Nav>
                    </div> */}
                    <div className='videoList'>
                        <Tab.Content >
                            {checkBoxCat.map((option, index) => (
                                <Tab.Pane key={index} eventKey={option.value} >
                                    <div className='mList'>
                                        {dummy.results
                                            .slice((index * 10), (index * 10) + 10)
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
                                </Tab.Pane>
                            ))}
                            <Tab.Pane eventKey="cat">
                                <h1>Cat Content</h1>
                            </Tab.Pane>
                        </Tab.Content>
                    </div>
                </Tab.Container>
                <div className='albumButtonList'>
                    <Home />
                    <Analyze />
                </div>
            </div>

        </div>
    );
}

export default Album;