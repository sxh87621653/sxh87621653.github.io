package com.sxh.work.mapper;

import com.sxh.work.entity.TelNote;

import java.awt.*;
import java.util.List;

public interface TelNoteDao {
     int create(TelNote telNote);
     List<TelNote> findAll();
}
