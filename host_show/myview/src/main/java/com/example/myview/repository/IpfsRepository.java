package com.example.myview.repository;

import com.example.myview.entity.Ipfs;
import org.springframework.data.jpa.repository.JpaRepository;

import java.math.BigInteger;

public interface IpfsRepository extends JpaRepository<Ipfs, BigInteger> {
    Ipfs findIpfsByBlockId(BigInteger blockId);
}
