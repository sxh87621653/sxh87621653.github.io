package com.sxh.work.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.sxh.work.entity.Account;
import com.sxh.work.mapper.AccountDao;

@Service
public class AccountService {
	@Autowired
	private AccountDao accountMapper;

	  public Account findByNameAndTel(Account account) {return accountMapper.findByNameAndTel(account);}

	  public Account findById(int userId){return accountMapper.findById(userId);}
	  
	  public int updatePic(Account account) {return accountMapper.updatePic(account);}
//
//	  public List<Account> findByUserName(String name){return accountDao.findByUserName(name);}
//
//	  public int insert(Account userModel) {
//	    return accountDao.insert(userModel);
//	  }
//
//	  public int update(Account userModel) {
//	    return accountDao.update(userModel);
//	  }
//
//	  public int delete(int id) { return accountDao.delete(id);}

	  public List<Account> findAll() {return accountMapper.findAll();}


//	  public int findCount() {return accountDao.findCount();}

}
