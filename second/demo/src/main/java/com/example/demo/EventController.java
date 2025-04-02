package com.example.demo;

import org.springframework.web.bind.annotation.*;

/* 
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import java.util.List;
*/
@CrossOrigin(origins = "*")
@RestController
@RequestMapping("/api/events")
public class EventController {

    /*
     * @Autowired
     * private EventRepository eventRepository;
     * 
     * @GetMapping
     * public ResponseEntity<List<Event>> getAllEvents() {
     * List<Event> events = eventRepository.findAll();
     * System.out.println("Fetched Events from DB: " + events); // Debugging Log
     * return events.isEmpty() ? ResponseEntity.noContent().build() :
     * ResponseEntity.ok(events);
     * }
     * 
     * @GetMapping("/")
     * public String home() {
     * return "Welcome to the Event Service!";
     * }
     */

    @GetMapping
    public String getEvents() {
        return "Events list";
    }

    @GetMapping("/")
    public String home() {
        return "Welcome to the API!";
    }
}
