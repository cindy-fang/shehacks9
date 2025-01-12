import React from "react";
import { Button } from "./Button";
import styles from "../styles/LandingPage.module.css";

export const NavBar = () => {
  return (
    <nav className={styles.navbar}>
      <div className={styles.navbarContainer}>
        <div className={styles.navbarContent}>
          <div className={styles.brandContainer}>
            <div className={styles.logoWrapper}>
              <img
                loading="lazy"
                src="https://cdn.builder.io/api/v1/image/assets/TEMP/6b32479b-93c0-4845-bab4-9d036897d49d?placeholderIfAbsent=true&apiKey=817559b7301c4b3c964f75e98fcf293f"
                alt="Synapse logo"
                className={styles.navLogo}
              />
            </div>

            <div className={styles.navMenu}>
              <a href="#demo" className={styles.navLink} tabIndex={0}>
                Demo
              </a>
              <a href="#features" className={styles.navLink} tabIndex={0}>
                Features
              </a>
              <Button variant="secondary">Download</Button>
            </div>
          </div>
        </div>
      </div>
    </nav>
  );
};
