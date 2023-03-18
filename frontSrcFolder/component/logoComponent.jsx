import './logoComponent.css'
import { Link } from 'react-router-dom';
import logo from 'C:/Users/tmdqj/Desktop/pet_project/pet/src/images/logo.png'
function logoComponent() {
    return ( 
        <div className='logoContainer'>
            <Link to="/"><img className='logoImg' src={logo} alt="main_logo" /></Link>
        </div>
     );
}

export default logoComponent;