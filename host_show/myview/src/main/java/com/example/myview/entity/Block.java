package com.example.myview.entity;

import javax.persistence.*;
import java.io.Serializable;
import java.math.BigInteger;
import java.sql.Timestamp;

@Entity
@Table(name = "blog_block")
public class Block implements Serializable {
    private static final long serialVersionUID = 1L;

    @Id
    @GeneratedValue
    @Column(name = "block_id")
    private BigInteger blockId;
    @Column(name = "block_time", nullable = false)
    private Timestamp blockTime;
    @Column(name = "block_high", nullable = false)
    private String blockHigh;
    @Column(name = "block_hash", nullable = false)
    private String blockHash;
    @Column(name = "block_text", nullable = false)
    private String blockText;

    public Block() {
    }

    public Block(BigInteger blockId, Timestamp blockTime, String blockHigh, String blockHash, String blockText) {
        this.blockId = blockId;
        this.blockTime = blockTime;
        this.blockHigh = blockHigh;
        this.blockHash = blockHash;
        this.blockText = blockText;
    }

    public BigInteger getBlockId() {
        return blockId;
    }

    public void setBlockId(BigInteger blockId) {
        this.blockId = blockId;
    }

    public Timestamp getBlockTime() {
        return blockTime;
    }

    public void setBlockTime(Timestamp blockTime) {
        this.blockTime = blockTime;
    }

    public String getBlockHigh() {
        return blockHigh;
    }

    public void setBlockHigh(String blockHigh) {
        this.blockHigh = blockHigh;
    }

    public String getBlockHash() {
        return blockHash;
    }

    public void setBlockHash(String blockHash) {
        this.blockHash = blockHash;
    }

    public String getBlockText() {
        return blockText;
    }

    public void setBlockText(String blockText) {
        this.blockText = blockText;
    }

    @Override
    public String toString() {
        return "User{" +
                "blockId=" + blockId +
                ", blockTime='" + blockTime + '\'' +
                ", blockHigh='" + blockHigh + '\'' +
                ", blockHash='" + blockHash + '\'' +
                ", blockText='" + blockText + '\'' +
                '}';
    }
}
