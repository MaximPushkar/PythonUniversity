from main import *
import unittest
import os
import re
import xml.etree.ElementTree as ET

from test.test_wsgiref import run_amock


def create_names(teams, file_name):
    teams_el = ET.Element("teams")
    i = 0
    for team in teams:
        i += 1
        team_el = ET.Element("team")
        team_el.set("id", str(i))
        team_el.set("name", team)
        teams_el.append(team_el)

    etree = ET.ElementTree(teams_el)
    etree.write(file_name, encoding="utf-8", xml_declaration=True)


def create_matches(matches, file_name):
    matches_el = ET.Element("matches")
    i = 0
    for match in matches:
        i += 1
        match_el = ET.Element("team")
        match_el.set("team1", str(match[0]))
        match_el.set("team2", str(match[1]))
        match_el.set("balls1", str(match[2]))
        match_el.set("balls2", str(match[3]))
        matches_el.append(match_el)

    etree = ET.ElementTree(matches_el)  # Створюмо дерево вузлів
    etree.write(file_name, encoding="utf-8", xml_declaration=True)


def get_status(response):
    """ Повертає http статус відповіді: код і короткий опис"""
    return re.search(r"(?P<STATUS>\d{3} .+?)\n", response).group("STATUS").rstrip()


class TestMatchResults(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.mock_names = [
            "Team 1", "Team 2", "Team 3"
        ]
        cls.mock_matches = [
            [1, 2, 3, 0], [2, 3, 0, 1], [1, 3, 3, 0]
        ]

        cls.match_results = MatchResults("names.xml", "matches.xml")

    def setUp(self) -> None:
        create_names(self.mock_names, "names.xml")
        create_matches(self.mock_matches, "matches.xml")

    @classmethod
    def tearDownClass(cls) -> None:
        os.remove("names.xml")
        os.remove("matches.xml")

    def test_01_get_names(self):
        expected_result = [
            "Team 1", "Team 2", "Team 3"
        ]
        result = self.match_results.get_names()
        self.assertIsInstance(result, list)
        self.assertCountEqual(expected_result, result)
        self.assertListEqual(expected_result, result)

    def test_02_get_matches(self):
        expected_result = [
            [1, 2, 3, 0], [2, 3, 0, 1], [1, 3, 3, 0]
        ]
        result = self.match_results.get_matches()
        self.assertIsInstance(result, list)
        self.assertCountEqual(expected_result, result)
        self.assertListEqual(expected_result, result)

    def test_03_correct_path_status(self):
        request = b"GET / HTTP/1.1"
        out, err = run_amock(self.match_results, request)
        response = str(out, encoding="utf-8")
        status = get_status(response)
        self.assertEqual("200 OK", status)

    def test_04_incorrect_path_status(self):
        request = b"GET /lalala_path HTTP/1.1"
        out, err = run_amock(self.match_results, request)
        response = str(out, encoding="utf-8")
        status = get_status(response)
        self.assertEqual("404 NOT FOUND", status)

    def test_05_correct_path_without_data(self):
        request = (
            b"POST /operation_status HTTP/1.0\n"
            b"Content-Type: application/x-www-form-urlencoded\n\n"
            b"from=&to=&balls_1=3&balls_2=2"
        )
        out, err = run_amock(self.match_results, request)
        response = str(out, encoding="utf-8")
        self.assertEqual("303 SEE OTHER", get_status(response))
        match = re.search("Location: (?P<LOCATION>.+?)\n", response)
        self.assertFalse(match is None)
        location = match.group("LOCATION").rstrip()
        self.assertEqual(location, "/")


if __name__ == "__main__":
    unittest.main(verbosity=2)
