package com.example.demo;

import org.bson.Document;
import org.springframework.core.convert.converter.Converter;
import org.springframework.lang.NonNull;
import org.springframework.stereotype.Component;

@Component
public class EventReadConverter implements Converter<Document, Event> {
    @Override
    public Event convert(@NonNull Document source) {
        Event event = new Event();
        event.setId(source.getInteger("_id"));
        event.setEvent_name(source.getString("event_name"));
        event.setLocation(source.getString("location"));
        event.setTiming(source.getString("timing"));
        event.setTicket_price(source.getInteger("ticket_price"));
        return event;
    }
}
