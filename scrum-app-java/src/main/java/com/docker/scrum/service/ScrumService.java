package com.docker.scrum.service;

import com.docker.scrum.model.Scrum;
import com.docker.scrum.model.ScrumDTO;
import com.docker.scrum.model.TaskDTO;

import java.util.List;
import java.util.Optional;

public interface ScrumService {

    List<Scrum> getAllScrumBoards();

    Optional<Scrum> getScrumById(Long id);

    Optional<Scrum> getScrumByTitle(String title);

    Scrum saveNewScrum(ScrumDTO scrumDTO);

    Scrum updateScrum(Scrum oldScrum, ScrumDTO newScrumDTO);

    void deleteScrum(Scrum scrum);

    Scrum addNewTaskToScrum(Long scrumId, TaskDTO taskDTO);
}
