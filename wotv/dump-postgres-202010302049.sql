--
-- PostgreSQL database dump
--

-- Dumped from database version 12.2 (Debian 12.2-2.pgdg90+1)
-- Dumped by pg_dump version 12.2

-- Started on 2020-10-30 20:49:13

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 3 (class 2615 OID 2200)
-- Name: public; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA public;


ALTER SCHEMA public OWNER TO postgres;

--
-- TOC entry 2881 (class 0 OID 0)
-- Dependencies: 3
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON SCHEMA public IS 'standard public schema';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 202 (class 1259 OID 16384)
-- Name: apis; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.apis (
    tables character varying
);


ALTER TABLE public.apis OWNER TO postgres;

--
-- TOC entry 203 (class 1259 OID 16390)
-- Name: characters; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.characters (
    name character varying NOT NULL,
    rank integer,
    link character varying
);


ALTER TABLE public.characters OWNER TO postgres;

--
-- TOC entry 2874 (class 0 OID 16384)
-- Dependencies: 202
-- Data for Name: apis; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.apis (tables) FROM stdin;
characters
\.


--
-- TOC entry 2875 (class 0 OID 16390)
-- Dependencies: 203
-- Data for Name: characters; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.characters (name, rank, link) FROM stdin;
Edson	44	/index
\.


--
-- TOC entry 2746 (class 1259 OID 16396)
-- Name: ix_characters_6ae999552a0d2dca; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_characters_6ae999552a0d2dca ON public.characters USING btree (name);


--
-- TOC entry 2747 (class 1259 OID 16397)
-- Name: ix_characters_e0c896cc4f59c8f5; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_characters_e0c896cc4f59c8f5 ON public.characters USING btree (name, rank);


-- Completed on 2020-10-30 20:49:26

--
-- PostgreSQL database dump complete
--

