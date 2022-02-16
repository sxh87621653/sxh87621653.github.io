package com.sxh.work.controller;

import com.sxh.work.entity.TelNote;
import com.sxh.work.service.TelNoteService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/tel")
public class TelNoteController {
    @Autowired
    private TelNoteService telNoteService;

    @PostMapping("create")
    public int createController(@RequestBody TelNote telNote){
       String telString=telNote.getRequestTel();
       telString=telString.substring(0, 3)+telString.substring(4, 8)+telString.substring(9, 13);
       telNote.setRequestTel(telString);
        if(telNoteService.create(telNote)>0)
        {
            return 1;
        }else {
            return 0;
        }
    }

    @GetMapping("findAll")
    public List<TelNote> findAllController(){return telNoteService.findAll();}


}
