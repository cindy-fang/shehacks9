import React from "react";
import { NavBar } from "./components/NavBar";
import { Footer } from "./components/Footer";
import { FeatureCard } from "./components/FeatureCard";
import { Button } from "./components/Button";
import styles from "./styles/LandingPage.module.css";

const features = [
  {
    icon: "https://cdn.builder.io/api/v1/image/assets/TEMP/d19f84865584083db7cbc635b66e8422fba58eeaa0336a071cc1a4c90724da0b?placeholderIfAbsent=true&apiKey=817559b7301c4b3c964f75e98fcf293f",
    title: "NLP to CLI Translation",
    description:
      "Bridge the gap between your ideas and the command line with AI-powered commands. Synapse seamlessly integrates your requirements, simplifying workflows and making the terminal accessible for all levels—from beginners to seasoned developers.",
  },
  {
    icon: "https://cdn.builder.io/api/v1/image/assets/TEMP/1f4b1f87d11cc9a09909c466d8a5c62e836aa6266819ff958a1992801b842373?placeholderIfAbsent=true&apiKey=817559b7301c4b3c964f75e98fcf293f",
    title: "Editable Commands",
    description:
      "Edit AI-prompted CLI commands before executing them for ultimate control. Synapse gives you the flexibility to tweak commands to fit your needs, making every action precise and tailored.",
  },
  {
    icon: "https://cdn.builder.io/api/v1/image/assets/TEMP/5b3c64b404bd10768793af6597ef19785aa5aa2b7ca1ec2ae8cee7f828a984d4?placeholderIfAbsent=true&apiKey=817559b7301c4b3c964f75e98fcf293f",
    title: "Command History and Insights",
    description:
      "Track past commands and learn from your most-used workflows with in-depth insights that translate complex actions into accessible knowledge.",
  },
  {
    icon: "https://cdn.builder.io/api/v1/image/assets/TEMP/c0393ae6da863937883d521ffca43e5b8997daeb35daa9d03def257380753f52?placeholderIfAbsent=true&apiKey=817559b7301c4b3c964f75e98fcf293f",
    title: "Smart OS Detection and Enhanced UX",
    description:
      "Enjoy a terminal tailored for ease and compatibility with Synapse's smart OS detection and familiar keyboard functionalities for natural interactions.",
  },
  {
    icon: "https://cdn.builder.io/api/v1/image/assets/TEMP/ac6892a7d341abaa57fea52a75e362c56602d82dbdebfef036a48f878725a8a9?placeholderIfAbsent=true&apiKey=817559b7301c4b3c964f75e98fcf293f",
    title: "Safety Net for Commands",
    description:
      "Prevent catastrophic mistakes with built-in safeguards. Synapse reviews risky commands, confirms actions with you, and ensures that your workflow stays error-free and efficient.",
  },
  {
    icon: "https://cdn.builder.io/api/v1/image/assets/TEMP/5caac5cc1a5bc6f4b29fe529d2e85518ae50862a73964a0034ed2482f51ff8a9?placeholderIfAbsent=true&apiKey=817559b7301c4b3c964f75e98fcf293f",
    title: "Project Setup Automations",
    description:
      "Set up your projects in seconds with a single command. Whether you're working on a MERN stack or another established tech framework, Synapse handles all dependencies and configurations automatically, saving you time and effort.",
  },
];

export default function App() {
  return (
    <div className={styles.landingPage}>
      <NavBar />

      <main className={styles.mainContent}>
        <section className="hero">
          {/* <img
            loading="lazy"
            src="https://cdn.builder.io/api/v1/image/assets/TEMP/6556a9b4a25c11052ee857881a911afcd7426b62e78ed5b2308eb8497fa5a740?placeholderIfAbsent=true&apiKey=817559b7301c4b3c964f75e98fcf293f"
            alt=""
            className={styles.heroBackground}
          /> */}
          <div className="heroContent">
            <h1 className="heroTitle">Your connection to a smarter CLI</h1>
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

        <section className="features">
          <h2 className={styles.featuresTitle}>Features</h2>
          <p className={styles.featuresDescription}>
            Learn how Synapse connects your commands to smarter execution. We're
            making the command line intuitive for all!
          </p>

          <div className={styles.featureGrid}>
            {features.map((feature, index) => (
              <FeatureCard
                key={index}
                icon={feature.icon}
                title={feature.title}
                description={feature.description}
              />
            ))}
          </div>
        </section>

        <section className="cta">
          <div className="ctaContainer">
            <h2 className="ctaTitle">
              From thought to execution, powered by Synapse.
            </h2>
            <p className={styles.ctaDescription}>
              Master the command line with Synapse, your AI-powered CLI
              assistant. Turn natural language into precise CLI commands,
              prevent costly mistakes, and streamline workflows with smart
              features like project setup, command generation, and an intuitive
              interface for users of any OS.
            </p>
            <Button variant="outline">Try Synapse today</Button>
          </div>
        </section>
      </main>

      <Footer />
    </div>
  );
}
