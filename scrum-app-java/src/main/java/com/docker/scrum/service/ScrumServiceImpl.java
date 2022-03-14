package com.docker.scrum.service;

import com.docker.scrum.model.Scrum;
import com.docker.scrum.model.ScrumDTO;
import com.docker.scrum.model.Task;
import com.docker.scrum.model.TaskDTO;
import com.docker.scrum.repository.ScrumRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

@Service
@RequiredArgsConstructor
public class ScrumServiceImpl implements ScrumService {

    private final ScrumRepository scrumRepository;

    @Override
    @Transactional
    public List<Scrum> getAllScrumBoards() {
        List<Scrum> scrumList = new ArrayList<>();
        scrumRepository.findAll().forEach(scrumList::add);
        return scrumList;
    }

    @Override
    @Transactional
    public Optional<Scrum> getScrumById(Long id) {
        return scrumRepository.findById(id);
    }

    @Override
    @Transactional
    public Optional<Scrum> getScrumByTitle(String title) {
        return scrumRepository.findByTitle(title);
    }

    @Override
    @Transactional
    public Scrum saveNewScrum(ScrumDTO scrumDTO) {
        scrumDTO.setTitle("j-"+scrumDTO.getTitle());
        return scrumRepository.save(convertDTOToScrum(scrumDTO));
    }

    @Override
    @Transactional
    public Scrum updateScrum(Scrum oldScrum, ScrumDTO newScrumDTO) {
        oldScrum.setTitle(newScrumDTO.getTitle());
        if(oldScrum.getTitle().substring(0,2) == "p-"){
            oldScrum.getTitle().replace("p-","j-");
        }
        else if (!(oldScrum.getTitle().substring(0,2) == "j-")){
            oldScrum.setTitle("j-" + oldScrum.getTitle());
        }

        return scrumRepository.save(oldScrum);
    }

    @Override
    @Transactional
    public void deleteScrum(Scrum scrum) {
        scrumRepository.delete(scrum);
    }

    @Override
    @Transactional
    public Scrum addNewTaskToScrum(Long scrumId, TaskDTO taskDTO) {
        Scrum scrum = scrumRepository.findById(scrumId).get();
        scrum.addTask(convertDTOToTask(taskDTO));
        return scrumRepository.save(scrum);
    }

    private Scrum convertDTOToScrum(ScrumDTO scrumDTO){
        Scrum scrum = new Scrum();
        scrum.setTitle(scrumDTO.getTitle());
        return scrum;
    }

    private Task convertDTOToTask(TaskDTO taskDTO) {
        Task task = new Task();
        task.setTitle(taskDTO.getTitle());
        task.setDescription(taskDTO.getDescription() + "\n - API Java");
        task.setColor(taskDTO.getColor());
        task.setStatus(taskDTO.getStatus());
        return task;
    }
}
