package com.example.myview.repository;

import com.example.myview.entity.User;

import org.springframework.data.jpa.repository.JpaRepository;

import java.math.BigInteger;
import java.util.Optional;

public interface UserRepository extends JpaRepository<User, BigInteger> {
    Optional<User> findUserByBlockId(BigInteger blockId);
}
