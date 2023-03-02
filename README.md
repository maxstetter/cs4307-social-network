# Social Network

## Max Stetter & Ben Jenks

This is our social network for CS4307 at Utah Tech University.

## Schema

* users

| user_id | name | thickness   | gender | age |
|---------|------|-------------|--------|-----|
| 1       | max  | not thick   | M      | 22  |
| 2       | ben  | super thick | M      | 20  |

* follows

| user_name | follow_name |
|-----------|-------------|
| max       | ben         |
| ben       | max         |

* posts

| post_id | author | content         | time                       | likes | dislikes |
|---------|--------|-----------------|----------------------------|-------|----------|
| 1       | max    | I hate valorant | 2023-03-01 14:26:04.282038 | 100   | 0        |
| 2       | ben    | I love valorant | 2023-03-01 19:36:27.391691 | 0     | 100      |

## Commands

In order to run our social network, start by running make_db.py
```
python3 make_db.py
```

### Create a User
This file creates a user with a unique name and id. If you try to do duplicate names, it will fail.

```
python3 create_user.py
```

### Follow Someone
This allows for one way follows. Given a user, who do you want to follow?

```
python3 add_follower.py
```

### Create a Post
Create a post given a user and the content you want to post.

```
python3 create_user.py
```

### Likes/Dislike Posts
Like or dislike posts. You can do this as much as you want to.

```
python3 dislike.py
python3 like.py
```

### Check Feed
See as many recent posts from your followers as you want. Results are in time order.

```
python3 check_feed.py
```

## Unique Queries

### How many people are thicky?
Gives you back all of the users that are thicky.

```
python3 thick.py
```

### Recently Active
Shows you people that have recently posted.

```
python3 recently_active.py
```

## Youtube link

