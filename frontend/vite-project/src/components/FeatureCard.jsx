import React from "react";
import styles from "../styles/LandingPage.module.css";

export const FeatureCard = ({ icon, title, description }) => {
  return (
    <div className={styles.featureCard}>
      <img
        loading="lazy"
        src={icon}
        alt={`${title} feature icon`}
        className={styles.featureIcon}
      />
      <div className={styles.cardContent}>
        <h3 className={styles.cardTitle}>{title}</h3>
        <p className={styles.cardDescription}>{description}</p>
      </div>
    </div>
  );
};
