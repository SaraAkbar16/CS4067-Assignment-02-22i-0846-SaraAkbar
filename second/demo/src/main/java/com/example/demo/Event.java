package com.example.demo;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@Document(collection = "event_listings")
public class Event {
    @Id
    private Integer id;
    private String event_name;
    private String location;
    private String timing;
    private Integer ticket_price;

    // ✅ Constructors
    public Event() {
    }

    public Event(String event_name, String location, String timing, int ticket_price) {
        this.event_name = event_name;
        this.location = location;
        this.timing = timing;
        this.ticket_price = ticket_price;
    }

    // ✅ Getters & Setters
    public int getId() {
        return id;
    }

    public String getEvent_name() {
        return event_name;
    }

    public String getLocation() {
        return location;
    }

    public String getTiming() {
        return timing;
    }

    public int getTicket_price() {
        return ticket_price;
    }

    public void setId(int id) {
        this.id = id;
    }

    public void setEvent_name(String event_name) {
        this.event_name = event_name;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public void setTiming(String timing) {
        this.timing = timing;
    }

    public void setTicket_price(int ticket_price) {
        this.ticket_price = ticket_price;
    }
}
