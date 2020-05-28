package com.example.myview.repository;

import com.example.myview.entity.Block;
import org.springframework.data.jpa.repository.JpaRepository;

import java.math.BigInteger;

public interface BlockRepository extends JpaRepository<Block, BigInteger> {
    Block findBlockByBlockId(BigInteger blockId);
}