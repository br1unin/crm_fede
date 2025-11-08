export interface User {
  id: number;
  email: string;
  name: string;
  role: 'admin' | 'employee';
  is_active: boolean;
  created_at: string;
}

export interface Client {
  id: number;
  name: string;
  company?: string;
  phone?: string;
  email?: string;
  address?: string;
  client_type: 'potential' | 'active';
  notes?: string;
  employee_id: number;
  created_at: string;
  employee?: User;
}

export interface Tractor {
  id: number;
  model: string;
  brand: string;
  year?: number;
  price?: number;
  status: 'available' | 'sold';
  description?: string;
  created_at: string;
}

export interface Sale {
  id: number;
  client_id: number;
  tractor_id: number;
  employee_id: number;
  sale_price: number;
  sale_date: string;
  notes?: string;
  client?: Client;
  tractor?: Tractor;
  employee?: User;
}

export interface LoginForm {
  email: string;
  password: string;
}

export interface AuthContextType {
  user: User | null;
  login: (email: string, password: string) => Promise<void>;
  logout: () => void;
  isAuthenticated: boolean;
}

// Agregar estas interfaces que faltaban
export interface RegisterForm {
  name: string;
  email: string;
  password: string;
  role: 'admin' | 'employee';
}

export interface ApiError {
  message: string;
  status: number;
}