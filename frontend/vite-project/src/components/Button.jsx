import React from "react";
import "../styles/Button.module.css";
import styles from "../styles/LandingPage.module.css";

export const Button = ({ children, variant = "primary", className = "" }) => {
  return (
    <button
      className={`${styles.button} ${styles[variant]} ${className}`}
      tabIndex={0}
    >
      {children}
    </button>
  );
};
