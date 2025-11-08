import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider, useAuth } from './context/AuthContext';
import Login from './components/auth/Login';
import Dashboard from './pages/Dashboard';
import Clients from './pages/Clients';
import Tractors from './pages/Tractors';
import Sales from './pages/Sales';
import Profile from './pages/Profile';
import Header from './components/common/Header';
import Sidebar from './components/common/Sidebar';
import './App.css';

function AppContent() {
  const { isAuthenticated } = useAuth();

  if (!isAuthenticated) {
    return <Login />;
  }

  return (
    <div className="flex h-screen bg-gray-100">
      <Sidebar />
      <div className="flex-1 flex flex-col overflow-hidden">
        <Header />
        <main className="flex-1 overflow-x-hidden overflow-y-auto p-6">
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/clientes" element={<Clients />} />
            <Route path="/tractores" element={<Tractors />} />
            <Route path="/ventas" element={<Sales />} />
            <Route path="/perfil" element={<Profile />} />
            <Route path="*" element={<Navigate to="/" replace />} />
          </Routes>
        </main>
      </div>
    </div>
  );
}

// Componente principal
function App() {
  return (
    <Router>
      <AuthProvider>
        <AppContent />
      </AuthProvider>
    </Router>
  );
}

export default App;