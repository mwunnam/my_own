#!/usr/bin/python3

class FileStorage():
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        ''' Returns the dictionary objects '''
        return self.__objects

    def new(self, obj):
        '''
        Adds a new object to __objects
        But does it in a way in a special way
        key = <obj class name>.id
        value = obj

        '''
        if obj is not None:
            key = f'{obj.__class__.__name___}.{obj.id}'
            self.__objects[key] = obj

    @classmethod
    def create(cls, **kwargs):
        '''
        create an instance from a with dictionary of attributes
        '''
        return cls(**kwargs)

    def save(self):
        ''' Serialize objects to the JSON file '''
        json_objects = {}
        for key, obj in self.__objects.items():
            json_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(json_objects, file)


    def reload(self):
        ''' Deserialize the JSON file to __objects only if the JSON file
            exist
        '''
        try:
            with open(self.__file_path, 'r') as file:
                json_objects = json.load(file)
                for key, value in json_objects.items():
                    cls_name = key.split('.')[0]
                    if cls_name in globals():
                        cls = globals()[cls_name]
                        self.__objects[key] = cls.create(**value)

        except FileNotFoundError:
            return f'File not Found'
