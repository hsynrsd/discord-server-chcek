import datetime

def get_creation_date_from_snowflake(snowflake_id: int) -> datetime.datetime:
    # Discord Epoch: 2015-01-01 00:00:00 UTC
    discord_epoch = 1420070400000
    timestamp = ((snowflake_id >> 22) + discord_epoch) / 1000
    return datetime.datetime.utcfromtimestamp(timestamp)

# Example usage
guild_id = "insert id here"
creation_date = get_creation_date_from_snowflake(guild_id)

print(f"ID {guild_id} was created on {creation_date} UTC")
