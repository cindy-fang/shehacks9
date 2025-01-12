import React from "react";
import styles from "../styles/LandingPage.module.css";

export const Footer = () => {
  return (
    <footer className={styles.footer}>
      <div className={styles.container}>
        <div className={styles.logoContainer}>
          <p className={styles.copyright}>
            © 2025 Synapse. Built with love by developers, for developers 🤍
          </p>
          <img
            loading="lazy"
            src="https://cdn.builder.io/api/v1/image/assets/TEMP/6b32479b-93c0-4845-bab4-9d036897d49d?placeholderIfAbsent=true&apiKey=817559b7301c4b3c964f75e98fcf293f"
            alt="Synapse logo"
            className={styles.footerLogo}
          />
        </div>
      </div>
    </footer>
  );
};
