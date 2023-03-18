import './Main.css';
import React, { useState, useEffect } from 'react';
import LogoComponent from './component/logoComponent';
import { Analyze, Album } from './component/ButtonWithNavigation'
import SelectAutoWidth from './component/catDogDropdown';
import {Button} from 'antd';

const catDog = [
    { value: 'dog', label: '강아지' },
    { value: 'cat', label: '고양이' }
];
const pet_state = { value: 'state', label: '현재 상태' }
export const checkBoxCat = [
    { value: 'cat1', label: 'cat 행동 1' },
    { value: 'cat2', label: 'cat 행동 2' },
    { value: 'cat3', label: 'cat 행동 3' }
];
export const checkBoxDog = [
    { value: 'option1', label: 'dog 행동 1' },
    { value: 'option2', label: 'dog 행동 2' },
    { value: 'option3', label: 'dog 행동 3' }
];
function Main() {
    const [selectedOption, setSelectedOption] = useState('');
    // const [checkedValues, setCheckedValues] = useState([]);
    // const [lastChecked, setLastChecked] = useState(null);

    // function handleSelectChange(event) {
    //     setSelectedValue(event.target.value);
    // }
    // const handleCheckboxChange = (e) => {
    //     const { value, checked } = e.target;
    //     if (checked) {
    //         setCheckedValues((prev) => ({ ...prev, [value]: true }));
    //     } else {
    //         if (lastChecked === value) {
    //             setLastChecked(null);
    //         }

    //         setCheckedValues((prev) => {
    //             const { [value]: deletedValue, ...rest } = prev;
    //             return rest;
    //         });
    //     }
    // };
    // const [isButtonDisabled, setIsButtonDisabled] = useState(true); // 선택 여부

    const [isOn, setIsOn] = useState(false);
    // const [selectedValue, setSelectedValue] = useState(null);

    // // 강아지를 보냈을 때 dog, 고양이를 보냈을 때 cat으로 post
    // function handleSubmit(event) {
    //     event.preventDefault();
    //     if (selectedValue === '고양이') {
    //         //'/animals가 보낼 곳'
    //         axios.post('/api', { 'category': 'cat' }, { baseURL: 'http://112.214.96.160:5000' })

    //             .then(response => console.log(response.data))
    //             .catch(error => console.error(error));
    //     } else if (selectedValue === '강아지') {
    //         axios.post('/api', { 'category': 'dog' }, { baseURL: 'http://112.214.96.160:5000' })
    //             .then(response => console.log(response.data))
    //             .catch(error => console.error(error));
    //     }
    //     else {
    //         alert('동물을 선택해주세요.');
    //     }
    // }

    // function handleSelectChange(event) {
    //     setSelectedValue(event.target.value);
    // }


    const handleClick = () => {
        setIsOn(!isOn);
    }
    // const navigateLink = useNavigate();
    // const navigateToAnalyze = () => {
    //     navigateLink('/Analyze');
    //   };
    // const navigateToAlbum = () => {
    //     navigateLink('/Album');
    //   };


    return (
        <div className='videoView'>
            <LogoComponent />
            <div className='videoWindow'>
                <div className='imgBox'>
                    {isOn && <img className='imgView' src='http://112.214.96.160:5000/video' alt="" />}
                </div>
                <div className='buttonClass'>
                    <div className='leftContents'>
                        <SelectAutoWidth/>
                        <span className='buttonList'>{pet_state.label}</span>
                    </div>
                    <div className='actionBtn'>
                        <div className='buttonList'>
                            <Button type='primary' onClick={handleClick} style={{fontFamily:'jua',letterSpacing:1}}>{isOn ? '캠끄기' : '캠켜기'}</Button>
                        </div>
                    </div>

                    <div className='buttonList'>
                        <Analyze />
                    </div>
                    <div className='buttonList'>
                        <Album />
                    </div>
                    {/* <div className='buttonList'>
                        <select value={selectedOption} onChange={(e) => setSelectedOption(e.target.value)}>
                            <option value=''>동물 선택</option>
                            {catDog.map((option) => (
                                <option key={option.value} value={option.value}>
                                    {option.label}
                                </option>
                            ))}
                        </select>
                        {selectedOption === 'dog' && (
                            <div>
                                {checkBoxDog.map((option) => (
                                    <label key={option.value}>
                                        <input
                                            type="checkbox"
                                            value={option.value}
                                            checked={checkedValues[option.value] || false}
                                            onChange={handleCheckboxChange}
                                        />
                                        {option.label}
                                    </label>
                                ))}
                            </div>
                        )} */}
                    {/* {selectedOption === 'cat' && (
                        <div>
                            {checkBoxCat.map((option) => (
                                <label key={option.value}>
                                    <input
                                        type="checkbox"
                                        value={option.value}
                                        checked={checkedValues[option.value] || false}
                                        onChange={handleCheckboxChange}
                                    />
                                    {option.label}
                                </label>
                            ))}
                        </div>
                    )}

                    </div> */}
                </div>
            </div>
        </div >
    );
}

export default Main;
