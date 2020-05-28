package com.example.myview.service;

import com.example.myview.entity.Block;
import com.example.myview.entity.Ipfs;
import org.springframework.data.domain.Page;
import com.example.myview.entity.User;

import java.math.BigInteger;
import java.util.Optional;

public interface UserService {
    Page<User> getUserList(int pageNum, int pageSize);

    Optional<User> findUserByBlockId(BigInteger blockId);

    Block findBlockByBlockId(BigInteger blockId);

    Ipfs findIpfsByBlockId(BigInteger blockId);
}
