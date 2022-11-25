import React from 'react';
import '../../../img/logo.svg'
import '../../../img/search.svg'
const PosHeader = () => {
return (
    <header className="header">
        <div className="header__logo">
            <img src="../../../img/logo.svg" alt="" />
        </div>
        <div className="header__buscador">
            <img src="../../../img/search.svg" alt="" />
        <input
            type="text"
            className="header__input"
            placeholder="Busca un término"
        />
        </div>
        <div className="header__usuario">
            <img 
            src="https://randomuser.me/api/portraits/men/90.jpg" alt="" />
            <span>Luis Ventura</span>
        </div>
    </header>
    );
};
export default PosHeader;