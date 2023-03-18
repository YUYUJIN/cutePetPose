import React, { useState, Component } from 'react';
import axios from 'axios';
import { Select, Button, Form } from 'antd';

const { Option } = Select;



export default function SelectAutoWidth() {
    const [selectedValue, setSelectedValue] = useState(null);

    const handleSubmit = (values) => {
        if (selectedValue === 'cat') {
            // '/animals가 보낼 곳'
            axios
                .post('/api', { category: 'cat' }, { baseURL: 'http://112.214.96.160:5000' })
                .then((response) => console.log(response.data))
                .catch((error) => console.error(error));
        } else if (selectedValue === 'dog') {
            axios
                .post('/api', { category: 'dog' }, { baseURL: 'http://112.214.96.160:5000' })
                .then((response) => console.log(response.data))
                .catch((error) => console.error(error));
        } else {
            alert('동물을 선택해주세요.');
        }
    };

    const handleSelectChange = (value) => {
        setSelectedValue(value);
    };

    return (
        <div className='selectPet'>
            <Form onFinish={handleSubmit} style={{alignItems: 'center' }} layout="inline">

                <Form.Item style={{ fontFamily: 'jua' }}>
                        <Select
                            value={selectedValue}
                            defaultValue="골라"
                            style={{ width: 90, fontFamily: 'jua', overflow: 'hidden', alignItems: 'center', verticalAlign:'middle' }}
                            onChange={handleSelectChange}
                            options={[
                                { value: 'cat', label: <span style={{ fontFamily: 'jua' }}>고양이</span> },
                                { value: 'dog', label: <span style={{ fontFamily: 'jua' }}>강아지</span> },
                            ]}
                            // dropdownStyle={{fontFamily:'jua'}}
                        />
                        {/* <Select value={selectedValue} onChange={handleSelectChange} style={{ minWidth: 90, letterSpacing: 1, fontFamily: 'jua' }}>
                            <Option value="강아지" style={{ fontFamily: 'jua', letterSpacing: 1 }}>강아지</Option>
                            <Option value="고양이" style={{ fontFamily: 'jua', letterSpacing: 1 }}>고양이</Option>
                        </Select> */}
                </Form.Item>
                <Form.Item>
                    <Button type="primary" htmlType="submit" style={{ fontFamily: 'jua', letterSpacing: 1 }}>선택</Button>
                </Form.Item>
            </Form>
        </div>
    );
}