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
                src="https://cdn.builder.io/api/v1/image/assets/TEMP/35ff9fa1b6c7ee6c910193c0958f7311745ae270c66bb1fbe7d0dd07b1262118?placeholderIfAbsent=true&apiKey=817559b7301c4b3c964f75e98fcf293f"
                alt="Synapse logo"
                className={styles.logo}
              />
              <span className={styles.brandName}>Synapse</span>
            </div>
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
    </nav>
  );
};
