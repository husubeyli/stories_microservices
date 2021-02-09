from flask import request, jsonify, send_from_directory
from flasgger import swag_from
from http import HTTPStatus
from post_service.app import app
from marshmallow.exceptions import ValidationError
from post_service.schemas.schmas import (
    RecipeSchema, 
    CategorySchema,
    TagSchema,
    StorySchema,
)
from post_service.config.base import MEDIA_ROOT
from post_service.utils.common import save_file
from post_service.models import Recipe, Category, Tag, Story
from flask_jwt_extended import (
    
    get_jwt_identity,
    jwt_required
)


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(MEDIA_ROOT, filename)

#RECIPES
@app.route('/recipes/', methods=['GET', 'POST'])
@swag_from('docs/recipe/recipes_get.yml', methods=['GET'])
@swag_from('docs/recipe/recipes_post.yml', methods=['POST'])
@jwt_required
def recipes():
    if request.method == 'POST':
        try:
            data = request.json or request.form
            # print(data)
            image = request.files.get('image')
            serializer = RecipeSchema()
            recipe = serializer.load(data)
            recipe.owner_id = get_jwt_identity()
            print(recipe.owner_id)
            recipe.image = save_file(image)
            recipe.save()
            return RecipeSchema().jsonify(recipe), HTTPStatus.CREATED
        except ValidationError as err:
            return jsonify(err.messages), HTTPStatus.BAD_REQUEST
    recipes = Recipe.query.filter_by(is_published=True)
    return RecipeSchema(many=True).jsonify(recipes), HTTPStatus.OK


@app.route('/recipes/<int:recipe_id>/', methods=['GET', 'PUT', 'PATCH', 'DELETE'])
@swag_from('docs/recipe/recipe_get_id.yml', methods=['GET'])
@swag_from('docs/recipe/recipe_put_id.yml', methods=['PUT'])
@swag_from('docs/recipe/recipe_patch_id.yml', methods=['PATCH'])
@swag_from('docs/recipe/recipe_delete_id.yml', methods=['DELETE'])
@jwt_required
def recipe(recipe_id):
    recipe = Recipe.query.filter_by(id=recipe_id).first()
    if not recipe:
        return jsonify({'message': 'Not found'}), HTTPStatus.NOT_FOUND
    if request.method == 'DELETE':
        recipe.delete()
        return jsonify({}), HTTPStatus.NO_CONTENT
    if request.method == 'GET':
        return RecipeSchema().jsonify(recipe), HTTPStatus.OK
    try:
        data = request.json or request.form
        image = request.files.get('image')
        serializer = RecipeSchema()
        if request.method == 'PUT':
            recipe_serializer = serializer.load(data, instance=recipe)
        elif request.method == 'PATCH':
            recipe_serializer = serializer.load(data, instance=recipe, partial=True)
        recipe.owner_id = get_jwt_identity()
        if image:
            recipe.image = save_file(image)
        recipe_serializer.save()
        return RecipeSchema().jsonify(recipe), HTTPStatus.OK
    except ValidationError as err:
        return jsonify(err.messages), HTTPStatus.BAD_REQUEST


# CATEGORY
@app.route('/category/', methods=['GET', 'POST'])
@swag_from('docs/category/category_get.yml', methods=['GET'])
@swag_from('docs/category/category_post.yml', methods=['POST'])
def category():
    if request.method == 'POST':
        try:
            data = request.json or request.form
            image = request.files.get('image')
            serializer = CategorySchema()
            category = serializer.load(data)
            category.image = save_file(image)
            category.save()
            return CategorySchema().jsonify(category), HTTPStatus.CREATED
        except ValidationError as err:
            return jsonify(err.messages), HTTPStatus.BAD_REQUEST
    categories = Category.query.filter_by(is_published=True)
    return CategorySchema(many=True).jsonify(categories), HTTPStatus.OK


@app.route('/category/<int:category_id>/', methods=['GET', 'PUT', 'PATCH', 'DELETE'])
@swag_from('docs/category/category_get_id.yml', methods=['GET'])
@swag_from('docs/category/category_put_id.yml', methods=['PUT'])
@swag_from('docs/category/category_patch_id.yml', methods=['PATCH'])
@swag_from('docs/category/category_delete_id.yml', methods=['DELETE'])

def categories(category_id):
    category = Category.query.filter_by(id=category_id).first()
    if not category:
        return jsonify({'message': 'Not found'}), HTTPStatus.NOT_FOUND
    if request.method == 'DELETE':
        recipe.delete()
        return jsonify({}), HTTPStatus.NO_CONTENT
    if request.method == 'GET':
        return CategorySchema().jsonify(recipe), HTTPStatus.OK
    try:
        data = request.json or request.form
        image = request.files.get('image')
        serializer = CategorySchema()
        if request.method == 'PUT':
            category_serializer = serializer.load(data, instance=category)
        elif request.method == 'PATCH':
            category_serializer = serializer.load(data, instance=category, partial=True)
        if image:
            category.image = save_file(image)
        category_serializer.save()
        return CategorySchema().jsonify(category), HTTPStatus.OK
    except ValidationError as err:
        return jsonify(err.messages), HTTPStatus.BAD_REQUEST



# TAG
@app.route('/tag/', methods=['GET', 'POST'])
@swag_from('docs/tag/tag_get.yml', methods=['GET'])
@swag_from('docs/tag/tag_post.yml', methods=['POST'])
def tag():
    if request.method == 'POST':
        try:
            data = request.json or request.form
            serializer = TagSchema()
            tag = serializer.load(data)
            tag.save()
            return TagSchema().jsonify(tag), HTTPStatus.CREATED
        except ValidationError as err:
            return jsonify(err.messages), HTTPStatus.BAD_REQUEST
    tag = Tag.query.all()
    return TagSchema(many=True).jsonify(tag), HTTPStatus.OK


@app.route('/tag/<int:tag_id>/', methods=['GET', 'PUT', 'PATCH', 'DELETE'])
@swag_from('docs/tag/tag_get_id.yml', methods=['GET'])
@swag_from('docs/tag/tag_put_id.yml', methods=['PUT'])
@swag_from('docs/tag/tag_patch_id.yml', methods=['PATCH'])
@swag_from('docs/tag/tag_delete_id.yml', methods=['DELETE'])

def tags(tag_id):
    tag = Tag.query.filter_by(id=tag_id).first()
    if not category:
        return jsonify({'message': 'Not found'}), HTTPStatus.NOT_FOUND
    if request.method == 'DELETE':
        recipe.delete()
        return jsonify({}), HTTPStatus.NO_CONTENT
    if request.method == 'GET':
        return TagSchema().jsonify(tag), HTTPStatus.OK
    try:
        data = request.json or request.form
        serializer = TagSchema()
        if request.method == 'PUT':
            tag_serializer = serializer.load(data, instance=tag)
        elif request.method == 'PATCH':
            tag_serializer = serializer.load(data, instance=tag, partial=True)
        tag_serializer.save()
        return TagSchema().jsonify(tag), HTTPStatus.OK
    except ValidationError as err:
        return jsonify(err.messages), HTTPStatus.BAD_REQUEST



#STORIES
@app.route('/story/', methods=['GET', 'POST'])
@swag_from('docs/story/stories_get.yml', methods=['GET'])
@swag_from('docs/story/story_post.yml', methods=['POST'])
def story():
    if request.method == 'POST':
        try:
            data = request.json or request.form
            print(data)
            image = request.files.get('images')
            serializer = StorySchema()
            story = serializer.load(data)
            story.owner_id = 1
            story.image = save_file(image)
            story.save()
            return StorySchema().jsonify(story), HTTPStatus.CREATED
        except ValidationError as err:
            return jsonify(err.messages), HTTPStatus.BAD_REQUEST
    stories = Story.query.filter_by(is_published=True)
    return StorySchema(many=True).jsonify(stories), HTTPStatus.OK


@app.route('/story/<int:story_id>/', methods=['GET', 'PUT', 'PATCH', 'DELETE'])
@swag_from('docs/story/story_get_id.yml', methods=['GET'])
@swag_from('docs/story/story_put_id.yml', methods=['PUT'])
@swag_from('docs/story/story_patch_id.yml', methods=['PATCH'])
@swag_from('docs/story/story_delete_id.yml', methods=['DELETE'])

def stories(story_id):
    story = Story.query.filter_by(id=story_id).first()
    if not story:
        return jsonify({'message': 'Not found'}), HTTPStatus.NOT_FOUND
    if request.method == 'DELETE':
        story.delete()
        return jsonify(), HTTPStatus.NO_CONTENT
    if request.method == 'GET':
        return StorySchema().jsonify(story), HTTPStatus.OK
    try:
        data = request.json or request.form
        image = request.files.get('image')
        serializer = StorySchema()
        if request.method == 'PUT':
            story_serializer = serializer.load(data, instance=story)
        elif request.method == 'PATCH':
            story_serializer = serializer.load(data, instance=story, partial=True)
        story.owner_id = get_jwt_identity()
        if image:
            story.image = save_file(image)
        story_serializer.save()
        return StorySchema().jsonify(story), HTTPStatus.OK
    except ValidationError as err:
        return jsonify(err.messages), HTTPStatus.BAD_REQUEST