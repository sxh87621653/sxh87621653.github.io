package com.sxh.work.controller;
import java.util.List;

import com.alibaba.druid.sql.visitor.functions.Substring;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import com.sxh.work.entity.Account;
import com.sxh.work.service.AccountService;


@RestController
/*处理前端请求，发送和接受json格式参数*/
@RequestMapping("/user")
public class AccountController {

  @Autowired
  /*自动装配*/
  private AccountService accountService;

  @PostMapping("findByNameAndTel")
  public Account findByNameAndTelController(@RequestBody Account account) {	  return accountService.findByNameAndTel(account); }

  @GetMapping("findById")
  public Account findByIdController(int userId){
    Account account =accountService.findById(userId);
    String tel= account.getUserTel();
    account.setUserTel(tel.substring(0,3)+"-"+tel.substring(3,7)+"-"+tel.substring(7,11));
    return account;
  }
  
  @PostMapping("updatePic")
  public int updatePic(@RequestBody Account account) {return accountService.updatePic(account);}
//
//  @GetMapping("findByName")
//  public List findByUserNameController(String name) { return accountService.findByUserName(name); }
//
//  @PostMapping("insert")
//  public int insertController(@RequestBody Account userModel) { return accountService.insert(userModel); }
//
//  @PostMapping("update")
//  public int updateController(@RequestBody Account userModel) { return accountService.update(userModel); }
//
//  @GetMapping("deleteById")
//  public int deleteByIdController(int id) { return accountService.delete(id); }

  @GetMapping("findAll")
  public List findAllController() {
    return accountService.findAll();
  }

//  @GetMapping("findCount")
//  public int findCountController() {return accountService.findCount();}

}