package com.example.myview.service.impl;

import com.example.myview.entity.Block;
import com.example.myview.entity.Ipfs;
import com.example.myview.entity.User;
import com.example.myview.repository.BlockRepository;
import com.example.myview.repository.IpfsRepository;
import com.example.myview.repository.UserRepository;
import com.example.myview.service.UserService;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Sort;
import org.springframework.stereotype.Service;

import java.math.BigInteger;
import java.util.Optional;

@Service
public class UserServiceImpl implements UserService {
    @Autowired
    private UserRepository userRepository;

    @Autowired
    private BlockRepository blockRepository;

    @Autowired
    private IpfsRepository ipfsRepository;

    @Override
    public Page<User> getUserList(int pageNum, int pageSize) {
        Sort sort = Sort.by(Sort.Direction.ASC, "blockId");
        Pageable pageable = PageRequest.of(pageNum, pageSize, sort);
        Page<User> users = userRepository.findAll(pageable);
        return users;
    }

    @Override
    public Optional<User> findUserByBlockId(BigInteger blockId) {
        return userRepository.findUserByBlockId(blockId);
    }

    @Override
    public Block findBlockByBlockId(BigInteger blockId) {
        return blockRepository.findBlockByBlockId(blockId);
    }

    @Override
    public Ipfs findIpfsByBlockId(BigInteger blockId) {
        return ipfsRepository.findIpfsByBlockId(blockId);
    }

}
