import React, { createContext, useContext, useState, useEffect } from 'react';
import type { ReactNode } from 'react';

// Definiciones de tipos locales
interface User {
  id: number;
  email: string;
  name: string;
  role: 'admin' | 'employee';
  is_active: boolean;
  created_at: string;
}

interface AuthContextType {
  user: User | null;
  login: (email: string, password: string) => Promise<void>;
  logout: () => void;
  isAuthenticated: boolean;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (context === undefined) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};

interface AuthProviderProps {
  children: ReactNode;
}

export const AuthProvider: React.FC<AuthProviderProps> = ({ children }) => {
  const [user, setUser] = useState<User | null>(null);
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  useEffect(() => {
    const token = localStorage.getItem('token');
    const userData = localStorage.getItem('user');
    if (token && userData) {
      try {
        const userObj: User = JSON.parse(userData);
        setUser(userObj);
        setIsAuthenticated(true);
      } catch (error) {
        console.error('Error parsing user data:', error);
        localStorage.removeItem('token');
        localStorage.removeItem('user');
      }
    }
  }, []);

  const login = async (email: string, password: string) => {
    try {
      console.log('Login attempt:', email, password);
      
      // Simulación de login
      const mockUser: User = {
        id: 1,
        email: email,
        name: email.split('@')[0],
        role: email.includes('admin') ? 'admin' : 'employee',
        is_active: true,
        created_at: new Date().toISOString()
      };

      setUser(mockUser);
      setIsAuthenticated(true);
      localStorage.setItem('token', 'mock-token');
      localStorage.setItem('user', JSON.stringify(mockUser));
    } catch (error) {
      console.error('Login error:', error);
      throw error;
    }
  };

  const logout = () => {
    setUser(null);
    setIsAuthenticated(false);
    localStorage.removeItem('token');
    localStorage.removeItem('user');
  };

  const value: AuthContextType = {
    user,
    login,
    logout,
    isAuthenticated
  };

  return (
    <AuthContext.Provider value={value}>
      {children}
    </AuthContext.Provider>
  );
};

// Exportar el tipo User para usarlo en otros componentes
export type { User };