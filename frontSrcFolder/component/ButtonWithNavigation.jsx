import { useNavigate } from 'react-router-dom';
import './ButtonWithNavigation.css'
import { Button} from 'antd';


function ButtonWithNavigation({ to, children }) {
  const navigate = useNavigate();
  
  const handleClick = () => {
    navigate(to);
  };
  
  return <Button type='primary' onClick={handleClick} style={{fontFamily:'jua',letterSpacing:1}}>{children}</Button>;
}

export function Home() {
  return (
    <div className='linkedButton'>
      <ButtonWithNavigation to="/">홈</ButtonWithNavigation>
    </div>
  );
}
export function Analyze() {
  return (
    <div className='linkedButton'>
      <ButtonWithNavigation to="/Analyze">분석</ButtonWithNavigation>
    </div>
  );
}

export function Album() {
  return (
    <div className='linkedButton'>
      <ButtonWithNavigation to="/Album">앨범</ButtonWithNavigation>
    </div>
  );
}