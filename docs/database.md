# FootIQ Database Design

## MVP

The first version of FootIQ will allow users to:

- Search for football players
- View player profiles
- View player statistics
- View the player's team

## Entities

### Team

| Field | Type | Description |
|---|---|---|
| id | INTEGER | Unique team ID |
| name | VARCHAR | Team name |
| country | VARCHAR | Team's country |
| league | VARCHAR | Team's league |

### Player

| Field | Type | Description |
|---|---|---|
| id | INTEGER | Unique player ID |
| name | VARCHAR | Player's name |
| age | INTEGER | Player's age |
| position | VARCHAR | Player's position |
| nationality | VARCHAR | Player's nationality |
| team_id | INTEGER | Player's team |

### PlayerStats

| Field | Type | Description |
|---|---|---|
| id | INTEGER | Unique statistics ID |
| player_id | INTEGER | Player |
| appearances | INTEGER | Number of appearances |
| minutes | INTEGER | Minutes played |
| goals | INTEGER | Goals scored |
| assists | INTEGER | Assists |
| shots | INTEGER | Shots |
| key_passes | INTEGER | Key passes |
| tackles | INTEGER | Tackles |
| interceptions | INTEGER | Interceptions |
| xg | DECIMAL | Expected goals |
| xa | DECIMAL | Expected assists |

## Relationships

A team can have many players.

A player belongs to one team.

A player has one set of statistics in the MVP.

```text
Team
 │
 │ 1
 │
 │
 │ *
Player
 │
 │ 1
 │
 │
 │ 1
PlayerStats