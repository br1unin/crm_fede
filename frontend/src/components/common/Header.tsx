import React from 'react';
import { useAuth } from '../../context/AuthContext';

const Header: React.FC = () => {
  const { user, logout } = useAuth();

  return (
    <header className="bg-white shadow-sm border-b border-gray-200">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-16">
          <div className="flex items-center">
            <h1 className="text-xl font-semibold text-gray-900">
              🚜 CRM Tractores
            </h1>
          </div>
          <div className="flex items-center space-x-4">
            <span className="text-sm text-gray-700">
              Hola, {user?.name}
            </span>
            <button
              onClick={logout}
              className="bg-gray-500 hover:bg-gray-600 text-white px-4 py-2 rounded-md text-sm"
            >
              Cerrar sesión
            </button>
          </div>
        </div>
      </div>
    </header>
  );
};

export default Header;