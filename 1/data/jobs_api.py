import flask

from . import db_session
from . jobs import Jobs

blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs')
def get_jobs():
    session = db_session.create_session()
    jobs = session.query(Jobs).all()
    return flask.jsonify({'jobs': [item.to_dict(only=('id', 'job', 'team_leader', 'work_size', 'collaborators',
                                                      'start_date', 'end_date', 'is_finished'))
                                   for item in jobs]})


@blueprint.route('/api/jobs/<int:news_id>', methods=['GET'])
def get_one_jobs(news_id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).get(news_id)
    if not jobs:
        return flask.jsonify({'error': 'Not found'})
    return flask.jsonify(
        {
            'jobs': jobs.to_dict(only=('id', 'job', 'team_leader', 'work_size', 'collaborators',
                                       'start_date', 'end_date', 'is_finished'))
        }
    )


@blueprint.route('/api/jobs', methods=['POST'])
def create_jobs():
    if not flask.request.json:
        return flask.jsonify({'error': 'Empty request'})
    elif not all(key in flask.request.json for key in
                 ['job', 'team_leader', 'work_size', 'collaborators', 'is_finished']):
        return flask.jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    jobs = Jobs(
        job=flask.request.json['job'],
        team_leader=flask.request.json['team_leader'],
        work_size=flask.request.json['work_size'],
        collaborators=flask.request.json['collaborators'],
        is_finished=flask.request.json['is_finished'],
    )
    db_sess.add(jobs)
    db_sess.commit()
    return flask.jsonify({'success': 'OK'})


@blueprint.route('/api/jobs/<int:news_id>', methods=['DELETE'])
def delete_jobs(news_id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).get(news_id)
    if not jobs:
        return flask.jsonify({'error': 'Not found'})
    db_sess.delete(jobs)
    db_sess.commit()
    return flask.jsonify({'success': 'OK'})


@blueprint.route('/api/jobs/<int:jobs_id>', methods=['PUT'])
def change_jobs(jobs_id):
    if not flask.request.json:
        return flask.jsonify({'error': 'Empty request'})
    elif not all(key in flask.request.json for key in
                 ['job', 'team_leader', 'work_size', 'collaborators', 'is_finished']):
        return flask.jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).get(jobs_id)
    if not jobs:
        return flask.jsonify({'error': 'Not found'})
    jobs.job = flask.request.json['job']
    jobs.team_leader = flask.request.json['team_leader']
    jobs.work_size=flask.request.json['work_size']
    jobs.collaborators = flask.request.json['collaborators']
    jobs.is_finished = flask.request.json['is_finished']
    db_sess.commit()
    return flask.jsonify({'success': 'OK'})
