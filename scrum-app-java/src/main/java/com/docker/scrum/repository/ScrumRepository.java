package com.docker.scrum.repository;

import com.docker.scrum.model.Scrum;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import java.util.Optional;

@Repository
public interface ScrumRepository extends CrudRepository<Scrum, Long> {

    Optional<Scrum> findByTitle(String title);
}
