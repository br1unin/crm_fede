    import React from 'react';
    import { useAuth } from '../context/AuthContext';

    const Profile: React.FC = () => {
    const { user } = useAuth();

    return (
        <div>
        <h1 className="text-2xl font-bold text-gray-900 mb-6">Mi Perfil</h1>
        <div className="bg-white rounded-lg shadow-md p-6">
            <div className="space-y-4">
            <div>
                <label className="block text-sm font-medium text-gray-700">Nombre</label>
                <p className="mt-1 text-sm text-gray-900">{user?.name}</p>
            </div>
            <div>
                <label className="block text-sm font-medium text-gray-700">Email</label>
                <p className="mt-1 text-sm text-gray-900">{user?.email}</p>
            </div>
            <div>
                <label className="block text-sm font-medium text-gray-700">Rol</label>
                <p className="mt-1 text-sm text-gray-900 capitalize">{user?.role}</p>
            </div>
            </div>
        </div>
        </div>
    );
    };

    // ✅ ESTA LÍNEA ES CRÍTICA - DEBE ESTAR AL FINAL
    export default Profile;