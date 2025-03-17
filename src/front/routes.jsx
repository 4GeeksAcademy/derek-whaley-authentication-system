// Import necessary components and functions from react-router-dom.

import {
  createBrowserRouter,
  createRoutesFromElements,
  Route,
} from "react-router-dom";
import { Layout } from "./pages/Layout";
import { Home } from "./pages/Home";
import { Signup } from "./pages/Signup";
import { Login } from "./pages/Login";
import { Private } from "./pages/Private";

export const router = createBrowserRouter(
createRoutesFromElements(
  <Route path="/" element={<Layout />} errorElement={<h1 className="text-center">404 - Page Not Found</h1>}>
    <Route index element={<Home />} />
    <Route path="/signup" element={<Signup />} />
    <Route path="/login" element={<Login />} />
    <Route path="/private" element={<Private />} />
  </Route>
)
);

