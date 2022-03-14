package com.docker.scrum;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.domain.EntityScan;
import org.springframework.data.jpa.repository.config.EnableJpaRepositories;

@SpringBootApplication
@EntityScan("com.docker.scrum.model")
@EnableJpaRepositories("com.docker.scrum.repository")
public class ScrumApplication {

	public static void main(String[] args) {
		SpringApplication.run(ScrumApplication.class, args);
	}

}
