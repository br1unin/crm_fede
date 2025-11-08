import React from 'react';
import { Link, useLocation } from 'react-router-dom';

const Sidebar: React.FC = () => {
  const location = useLocation();

  const menuItems = [
    { path: '/', label: 'Dashboard', icon: '📊' },
    { path: '/clientes', label: 'Clientes', icon: '👥' },
    { path: '/tractores', label: 'Tractores', icon: '🚜' },
    { path: '/ventas', label: 'Ventas', icon: '💰' },
    { path: '/perfil', label: 'Perfil', icon: '👤' },
  ];

  return (
    <div className="w-64 bg-gray-800 text-white">
      <nav className="mt-8">
        {menuItems.map((item) => (
          <Link
            key={item.path}
            to={item.path}
            className={`flex items-center px-6 py-3 text-sm font-medium ${
              location.pathname === item.path
                ? 'bg-gray-900 text-white'
                : 'text-gray-300 hover:bg-gray-700'
            }`}
          >
            <span className="mr-3 text-lg">{item.icon}</span>
            {item.label}
          </Link>
        ))}
      </nav>
    </div>
  );
};

export default Sidebar;