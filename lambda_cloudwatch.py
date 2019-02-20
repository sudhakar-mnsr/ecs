if event["source"] != "aws.ecs":
    raise ValueError("This function only supports a source type of: aws.ecs")
print ("Here is the event:")
print(json.dumps(event))
