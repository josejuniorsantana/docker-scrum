package com.docker.scrum.service;

import com.docker.scrum.model.Task;
import com.docker.scrum.model.TaskDTO;

import java.util.List;
import java.util.Optional;

public interface TaskService {

    List<Task> getAllTasks();

    Optional<Task> getTaskById(Long id);

    Optional<Task> getTaskByTitle(String title);

    Task saveNewTask(TaskDTO taskDTO);

    Task updateTask(Task oldTask, TaskDTO newTaskDTO);

    void deleteTask(Task task);
}
