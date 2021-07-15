from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Video(name = {name}, view = {views}, likes = {likes})"

# delete the step db.create_all() here to prevent overwriting the db

###names = {"John": {"age": 43, "gender": "male"}, ### Demo Data for Helloworld
###        "Sara":{"age": 42, "gender": "female"},
###        "Jane":{"age": 8, "gender": "female"},
###        "Lisa": {"age": 5, "gender": "female"}}

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
video_put_args.add_argument("views", type=int, help="Views of the video is required", required=True)
video_put_args.add_argument("likes", type=int, help="Likes of the video is required", required=True)

video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type=str, help="Name of the video")
video_update_args.add_argument("views", type=int, help="Views of the video")
video_update_args.add_argument("likes", type=int, help="Likes of the video")

resource_fields = {    ### imported fields and marshal_with
    'id': fields.Integer,
    'name': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer
}

### videos= {} ### removed b/c of db creation

###def abort_if_video_doesnt_exist(video_id): ### removed b/c of db creation
###    if video_id not in videos:
###        abort(404, message="Video ID: {} not valid...".format(video_id))

###def abort_if_video_exists(video_id): ### removed b/c of db creation
###    if video_id in videos:
###        abort(409, message="Video with that ID: {} already exists...".format(video_id))


###class HelloWorld(Resource):  ### demo class for starting Flask
###    def get(self, name):
###        return names[name]

###    def post(self):   ### demo for starting Flask
#        return {"data":"Posted"}

class Video(Resource):
    @marshal_with(resource_fields)
    def get(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="Video with ID {} does not exist...".format(video_id))
        return result
###        abort_if_video_doesnt_exist(video_id)   ### removed b/c of db creation
###        return videos[video_id]   ### removed b/c of db creation

    @marshal_with(resource_fields)
    def put(self, video_id):
        args = video_put_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if result:
            abort(409, message="Video ID {} taken...".format(video_id))
        video = VideoModel(id=video_id, name=args['name'], views=args['views'], likes=args['likes'])
        db.session.add(video)
        db.session.commit()
        return video, 201
###        abort_if_video_exists(video_id)   ### removed b/c of db creation
###        args = video_put_args.parse_args()
###        videos[video_id] = args
###        return videos[video_id], 201 #means created

    @marshal_with(resource_fields)
    def patch(self, video_id):
        args = video_update_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="Video ID {} does not exist...".format(video_id))

        if args['name']:
            result.name = args['name']
        if args['views']:
            result.views = args['views']
        if args['likes']:
            result.likes = args['likes']

        db.session.commit()           

        return result, 204

    @marshal_with(resource_fields)
    def delete(self, video_id):
        args = video_update_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="Video ID {} does not exist...".format(video_id))
        del args[video_id]
        return result, 501 #incomplete delete logic
###        abort_if_video_doesnt_exist(video_id)   ### removed b/c of db creation
###        del videos[video_id]
###        return '', 204


###api.add_resource(HelloWorld, "/helloworld/<string:name>")   ###demo resource for HelloWorld
api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)
    # Turn debug=True off for Prod