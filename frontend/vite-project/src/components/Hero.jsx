import React from "react";
import styles from "../styles/LandingPage.module.css";

export const Footer = () => {
  return (
    <section className={styles.hero}>
      <div className={styles.heroContent}>
        <h1 className={styles.heroTitle}>Your connection to a smarter CLI</h1>
        <p className={styles.heroDescription}>
          A CLI assistant turning natural language into commands.
          <br />
          Simplifying the terminal, one command at a time.
        </p>
        <Button>Download</Button>

        <div className={styles.partnerLogos}>
          <img
            loading="lazy"
            src="https://cdn.builder.io/api/v1/image/assets/TEMP/484763d8c5b50f6fa51e4daa93cd9c1e332dff5cb3f2b52917ebbfc514a1089d?placeholderIfAbsent=true&apiKey=817559b7301c4b3c964f75e98fcf293f"
            alt="Partner logo 1"
            className={styles.partnerLogo}
          />
          <img
            loading="lazy"
            src="https://cdn.builder.io/api/v1/image/assets/TEMP/4e1950ea7dce6f6077a57c6280e0b8a847887f1d4f00b3b935af8c3afbbb8904?placeholderIfAbsent=true&apiKey=817559b7301c4b3c964f75e98fcf293f"
            alt="Partner logo 2"
            className={styles.partnerLogo}
          />
          <img
            loading="lazy"
            src="https://cdn.builder.io/api/v1/image/assets/TEMP/aa4c304ed5c43dcc813a8e7947c9ec9e51e8eca1ef7279e099c1718a013323ca?placeholderIfAbsent=true&apiKey=817559b7301c4b3c964f75e98fcf293f"
            alt="Partner logo 3"
            className={styles.partnerLogo}
          />
        </div>
      </div>
    </section>
  );
};
