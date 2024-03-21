-- phpMyAdmin SQL Dump
-- version 4.7.1
-- https://www.phpmyadmin.net/
--
-- Host: sql11.freesqldatabase.com
-- Czas generowania: 10 Lut 2024, 00:49
-- Wersja serwera: 5.5.62-0ubuntu0.14.04.1
-- Wersja PHP: 7.0.33-0ubuntu0.16.04.16

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Baza danych: `sql11682263`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `firstname` varchar(255) NOT NULL,
  `lastname` varchar(255) NOT NULL,
  `login` varchar(255) NOT NULL,
  `password` varchar(128) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Zrzut danych tabeli `users`
--

INSERT INTO `users` (`id`, `firstname`, `lastname`, `login`, `password`) VALUES
(47, 'mJFI7U9uIxgBNwVyNYatcV/ZUM34YWSO977a4Z35E24=', '71KNMIN7l3o5LrJNd3Ajoi7URf73Z2ULCV3mzGQxPrs=', 'ZtWaF+a6MuXJo1ZTQeZyTere/p4jq8InYe3uLUtT/oo=', 'JDJiJDEyJGhlWkx6d0U5ZWZNWFJ5VFZGaFZFZnVvekw3NWRNRHAwME0xOHlMbHlFNnRPZUEva2JsM0th'),
(48, 'gkvKsKyDLSqi6ROXaDmJANnvvjIwLQRZb8IPoVkkr2M=', '2KkcwrqaWu/eMk3uCLiiNwwqSqxZKswscDBIU6c44mw=', 'Mi/nXdBwk0j3eOwoPyPqyUuYWkCiMpa1QOC+qPT86L0=', 'JDJiJDEyJGxJcnRsMDBlWjFaNmg1UXJOTUVyVmUyN1Vwd2gyZHRicmdLN2pSdUZhblgvZnhscy5kU2F1'),
(49, '+gu5Jt/+/7ifTv4kkjPuo/DwERxj3He65QmrtrlqK00=', 'TBrCqeyqrEKde4TLobq/He++lBlHuYmyfWV6Y4ljZZo=', 'vuKraatpl/wp2j3r7Cm7sp5obLDAxnp50dh+Dgs2pNY=', 'JDJiJDEyJHQ2dXRTeG5jaFhyRVZsMTRrT1BEZy5tdFVYeFZPdVplU1RCdktXclJ5c0t5OUptTS9WY0NT'),
(50, 'Ufs4SSuqlO4cR/zKuemuACpcte0Dq7Qo9T7XEdYWnH0=', 'cwCao7C9uGwpTKyfxYrZQAh2YJ2CAK1RfK4G0+nj7JU=', 'qZdEdVo8YShWNnmbUGRg4G7DCcPKjtJ9jugbojtdOwE=', 'JDJiJDEyJEdtQjk1MnFFMEh4bGNaQ2ZUVWt2Vk9DZWRtcEcyZEpzZFdPTEdtZjd0OW9HUUl3Li5oUkhX'),
(51, 'MRVxo+idT7RIUBsb+ZZrhi8CLRY8btV9lvncSMl1XYk=', '/G7V+XMmG3GiWeM0PhoKQ+rK96OLsqV6cF46uTgMuaM=', 'd+aG3gVL9BxhE05NSGNYjCxcfJTgfcmNe68iZzP5ztY=', 'JDJiJDEyJFd5Q1ZMSUNScU90a0VYNTJESnZJOS5vb1gyeC4wWEJ6R3pJYlQ3eHZtU2pEWGhZbzRqV0lh'),
(52, 'qFlc07U43xhLwoC/62yXPJi2AoP25voWJoyrpusqYv0=', 'Se7N4nZ8BUolBpOlHHK/Pg3u0gToE+y7xm6T5iafR4Q=', 'BD0045t9LMVqx5aJ4t7zn02ZD9bCV3OrrbC2xrwwXlE=', 'JDJiJDEyJC80RHFnV1VaUzg5d0R1NU1KYk5PSHUzZUdjY3hxbkRxeHZSUTh6ZDk4b2JqeFpwYmhhZGdL'),
(53, '5kz8oRMo1vs+3ksKXkotV+Sa5jZnVWX0amc3utX0dHM=', 'B7CUE0DAdaEEjaTzqGL8LDU8M0xl0lvLovShbMfkFC0=', 'wIfe6jeSzlgfws8BJXJq+VBOdGVjfOMegMhWMJJtzg8=', 'JDJiJDEyJHM0bENaVm5RMGUzbVluZUdtOUV1eGVOc1NWb1I1Z2pOM3dzTVVGNnJ1Q0FVNnRwL0J1Nkwy'),
(54, 'fz6EtpXYxIdW+mF5UO8gVgqLBmfYCGjqixN4xO5m0AQ=', 'AWttw3s2CzgdAui7rstH5VDqCmREZQhnvIu6OmURrG8=', 'seK2QcSFAqg2O0ppKyBxWkXlHX+uYjkesuCKNV/qeOU=', 'JDJiJDEyJDJDVTZDQnMvQlNMSTl4Ymc0N1E1cnV4UjB6cW1KNVVrSDU4NEZSLkVBSWRKS2ZVOHlrSVA2'),
(55, 'O9rzC98QDijM0ayqSgvWi1FB3y+ve8fLluhPVV/fMmw=', 'VDnbT4sqfOZ+9Eq8BzOHrKiKGroV9KjzdR7pXiu+JJQ=', '6WGN4vghdZHRgO2nUw72hIjMBhdyLyuKZQOu2dQozik=', 'JDJiJDEyJFp4ZmNvTU9SZENEZjZQLjRwbUdOOC5QUjZxdXhYU0N2VDRLa0tTMllVemJEZFNVU0VYMnFx'),
(56, 'hr1Ub0jtCGrI6SAuVIEioMabDRwx5ty/KApooJmoDiE=', '64cpoRaoDwp19tqSZgG4TVX4VbE429lJ5CDMTxKMWgc=', '8cY7RF0SSGjrF5cuYLhBi71WWrqw15Xeroz3ZbkJyVQ=', 'JDJiJDEyJGJnLlpoWFc0ZnliS2tXTWI1LlhPbWV2OXlwdmQ0Zldwd1JRQUVaV3lKcFprN05rVW1HTXR1');

--
-- Indeksy dla zrzutów tabel
--

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `login` (`login`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT dla tabeli `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=57;COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
