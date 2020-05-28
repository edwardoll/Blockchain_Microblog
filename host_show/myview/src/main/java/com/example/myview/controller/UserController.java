package com.example.myview.controller;

import com.example.myview.entity.Block;
import com.example.myview.entity.Ipfs;
import com.example.myview.entity.User;
import com.example.myview.service.UserService;

import org.springframework.ui.Model;
import org.springframework.data.domain.Page;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

import javax.annotation.Resource;
import java.math.BigInteger;
import java.util.Date;

@Controller
public class UserController {

    @Resource
    UserService userService;

    @RequestMapping("/")
    public String first() {
        return "redirect:/index";
    }

    @RequestMapping("/index")
    public String index(Model model) {
        int pageSize = 10;
        Page<User> users = userService.getUserList(0, pageSize);
        model.addAttribute("totalNumber", countNumber(users.getTotalPages(), pageSize));
        model.addAttribute("currentDate", new Date());
        return "index";
    }

    @RequestMapping("/list")
    public String list(Model model, @RequestParam(value = "pageNum", defaultValue = "0") int pageNum, @RequestParam(value = "pageSize", defaultValue = "10") int pageSize) {
        System.out.println("============================");
        Page<User> users = userService.getUserList(pageNum, pageSize);
        System.out.println("总页数" + users.getTotalPages());
        System.out.println("当前页是：" + pageNum);
        System.out.println("分页数据：");
        for (User user : users) {
            System.out.println(user.toString());
        }
        model.addAttribute("users", users);
        return "list";
    }

    @RequestMapping("/detail")
    public String detail(Model model, BigInteger id) {
        Block block = userService.findBlockByBlockId(id);
        Ipfs ipfs = userService.findIpfsByBlockId(id);
        model.addAttribute("BlockId", block.getBlockId());
        model.addAttribute("BlockTime", block.getBlockTime());
        model.addAttribute("BlockHigh", block.getBlockHigh());
        model.addAttribute("BlockHash", block.getBlockHash());
        model.addAttribute("BlockText", block.getBlockText());
        if(ipfs!=null)
            model.addAttribute("BlockIpfs", ipfs.getBlockIpfs());
        else
            model.addAttribute("BlockIpfs", "数据缺失，敬请期待！");
        return "detail";
    }

    @RequestMapping("/show")
    public String show(Model model, BigInteger id) {
        Block block = userService.findBlockByBlockId(id);
        System.out.println(block);
        if(block==null)
            return "wrong";
        else
            return detail(model, id);
    }

    public int countNumber(int total, int size) {
        int num = (total - 1) * size;
        Page<User> users = userService.getUserList(total - 1, size);
        for (User user : users) {
            num = num + 1;
        }
        return num;
    }
}
