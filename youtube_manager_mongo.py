from pymongo import MongoClient
from bson import ObjectId

client = MongoClient('mongodb+srv://susanta:susanta@cluster0.ihmme.mongodb.net/')

db = client['ytmanager']
video_collection = db['videos']

def list_videos():
    for video in video_collection.find():
        print(f'ID: {video["_id"]}, Name: {video["name"]}, Duration: {video["duration"]}')

def add_video(name, duration):
    if name and duration:
        video_collection.insert_one({"name": name, 'duration': duration})
    else:
        print("Name and duration cannot be empty.")

def update_video(video_ID, new_name, new_duration):
    if new_name and new_duration:
        try:
            video_collection.update_one(
                {'_id': ObjectId(video_ID)}, 
                {'$set': {'name': new_name, 'duration': new_duration}}
            )
        except Exception as e:
            print(f"Error updating video: {e}")
    else:
        print("New name and duration cannot be empty.")

def delete_video(video_ID):
    try:
        video_collection.delete_one({'_id': ObjectId(video_ID)})
    except Exception as e:
        print(f"Error deleting video: {e}")

def main():
    while True:
        print('\nYoutube Manager App')
        print('1. List all videos')
        print('2. Add new video')
        print('3. Update a video')
        print('4. Delete a video')
        print('5. Exit')
        choice = input('Enter your choice: ')

        if choice == '1':
            list_videos()

        elif choice == '2':
            name = input("Enter video name: ")
            duration = input("Enter the duration: ")
            add_video(name, duration)

        elif choice == '3':
            video_ID = input('Enter the video ID to update: ')
            name = input("Enter new video name: ")
            duration = input("Enter new duration: ")
            update_video(video_ID, name, duration) 
            
        elif choice == '4':
            video_ID = input('Enter the video ID to delete: ')
            delete_video(video_ID)

        elif choice == '5':
            break

        else:
            print("Enter a valid input")

if __name__ == "__main__":
    main()