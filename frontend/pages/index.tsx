import type { NextPage } from "next";
import Head from "next/head";
import Image from "next/image";
import Model from "../components/model";
import styles from "../styles/Home.module.css";

const Home: NextPage = () => {
  return (
    <div className={styles.container}>
      <Head>
        <title>AI Generated Branding</title>
        <meta
          name="description"
          content="Generate branding snippets for your product."
        />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <Model/>

    </div>
  );
};

export default Home;
