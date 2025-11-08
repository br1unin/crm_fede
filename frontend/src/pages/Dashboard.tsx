import React from 'react';
import { useAuth } from '../context/AuthContext';

const Dashboard: React.FC = () => {
  const { user } = useAuth();

  return (
    <div>
      <h1 className="text-2xl font-bold text-gray-900 mb-6">
        Dashboard
      </h1>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="bg-white p-6 rounded-lg shadow-md">
          <h3 className="text-lg font-semibold mb-2">Total Clientes</h3>
          <p className="text-3xl font-bold text-blue-600">0</p>
        </div>
        <div className="bg-white p-6 rounded-lg shadow-md">
          <h3 className="text-lg font-semibold mb-2">Tractores en Stock</h3>
          <p className="text-3xl font-bold text-green-600">0</p>
        </div>
        <div className="bg-white p-6 rounded-lg shadow-md">
          <h3 className="text-lg font-semibold mb-2">Ventas Totales</h3>
          <p className="text-3xl font-bold text-purple-600">0</p>
        </div>
      </div>
      <div className="mt-8 bg-white p-6 rounded-lg shadow-md">
        <h3 className="text-lg font-semibold mb-4">
          Bienvenido, {user?.name} ({user?.role})
        </h3>
        <p className="text-gray-600">
          Esta es la versión beta del CRM para tractores. Próximamente tendrás acceso a todas las funcionalidades.
        </p>
      </div>
    </div>
  );
};

export default Dashboard;