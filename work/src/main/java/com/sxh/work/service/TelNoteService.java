package com.sxh.work.service;

import com.sxh.work.entity.TelNote;
import com.sxh.work.mapper.TelNoteDao;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class TelNoteService {
    @Autowired
    private TelNoteDao telNoteDao;

    public int create(TelNote telNote) {
        return telNoteDao.create(telNote);
    }

    public List<TelNote> findAll()
    {
        return telNoteDao.findAll();
    }


}
