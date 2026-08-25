# FootIQ Database Design

## Overview

The FootIQ MVP database will store football teams, players and player statistics.

The first version will support:

- Searching for players
- Viewing player profiles
- Viewing player statistics
- Showing the player's current team

## Tables

### Teams

Stores information about football clubs.

| Field | Type | Description |
|---|---|---|
| id | INTEGER | Unique team ID |
| name | VARCHAR(100) | Team name |
| country | VARCHAR(100) | Country |
| league | VARCHAR(100) | League |

### Players

Stores information about football players.

| Field | Type | Description |
|---|---|---|
| id | INTEGER | Unique player ID |
| name | VARCHAR(100) | Player name |
| age | INTEGER | Player age |
| position | VARCHAR(50) | Playing position |
| nationality | VARCHAR(100) | Nationality |
| team_id | INTEGER | Player's team |

### Player Stats

Stores player performance statistics for each season.

| Field | Type | Description |
|---|---|---|
| id | INTEGER | Unique statistics ID |
| player_id | INTEGER | Player ID |
| season | VARCHAR(20) | Season |
| appearances | INTEGER | Appearances |
| minutes | INTEGER | Minutes played |
| goals | INTEGER | Goals |
| assists | INTEGER | Assists |
| shots | INTEGER | Shots |
| key_passes | INTEGER | Key passes |
| tackles | INTEGER | Tackles |
| interceptions | INTEGER | Interceptions |
| xg | DECIMAL(5,2) | Expected goals |
| xa | DECIMAL(5,2) | Expected assists |

## Relationships

A team can have many players.

A player belongs to one team.

A player can have multiple statistical records across different seasons.

```text
Team
  |
  | 1
  |
  | *
Player
  |
  | 1
  |
  | *
Player Stats