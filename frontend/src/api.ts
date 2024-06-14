import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000';

export const createTask = async (taskTitle: string, taskDescription: string) => {
  try {
    const response = await axios.post(`${API_URL}/tasks/`, {
      task_title: taskTitle,
      task_description: taskDescription
    });

    return response.data;
  } catch (error) {
    if (error.response && error.response.data && error.response.data.detail) {
      throw new Error(error.response.data.detail);
    } else {
      throw new Error('Erro ao criar a tarefa');
    }
  }
};
