import React, { Component } from 'react';
import axios from 'axios';

class MyComponent extends Component {
    state = {
      category: '',
    };
  
    componentDidMount() {
        axios.get('/api/data')
          .then(response => {
            const data = response.data;
            this.setState({ category: data.category });
          })
          .catch(error => {
            console.log(error);
          });
      }
  
    render() {
      return <div>{this.state.category}</div>;
    }
  }
  
  export default MyComponent;