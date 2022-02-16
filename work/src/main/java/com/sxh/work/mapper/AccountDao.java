package com.sxh.work.mapper;

import java.util.List;

import com.sxh.work.entity.Account;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Select;


public interface AccountDao {

	  Account findByNameAndTel(Account account);
	  Account findById(Integer id);
	  int updatePic(Account account);
//
//	  @Select("select * from Account where userName like concat('%',#{userName},'%')")
//	  List<Account> findByUserName(String userName);
//
//	  @Insert("insert into Account(userId, userName, userTel) VALUES(#{userId}, #{userName}, #{userTel})")
//	  int insert(Account account);
//
//	  @Update("Update Account set userId = #{userId},userName= #{userName} Where id = #{userTel}")
//	  int update(Account account);
//
//	  @Delete("Delete from Account where userId = #{userId}")
//	  int delete(int id);

      List<Account> findAll();
//
//	  @Select("SELECT count(*) from Account")
//	  Integer findCount();

}
