import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import {
  FiHome,
  FiUsers,
  FiTruck,
  FiShoppingCart,
  FiUser,
} from 'react-icons/fi';

const menuItems = [
  { path: '/', label: 'Dashboard', icon: <FiHome /> },
  { path: '/clientes', label: 'Clientes', icon: <FiUsers /> },
  { path: '/tractores', label: 'Tractores', icon: <FiTruck /> },
  { path: '/ventas', label: 'Ventas', icon: <FiShoppingCart /> },
  { path: '/perfil', label: 'Perfil', icon: <FiUser /> },
];

const Sidebar: React.FC = () => {
  const location = useLocation();

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
