package com.example.myview.entity;

import javax.persistence.*;
import java.io.Serializable;
import java.math.BigInteger;

@Entity
@Table(name = "block_txt")
public class Ipfs implements Serializable{
    private static final long serialVersionUID = 1L;

    @Id
    @GeneratedValue
    @Column(name = "block_id")
    private BigInteger blockId;
    @Column(name = "block_ipfs", nullable = false)
    private String blockIpfs;

    public Ipfs() {
    }

    public Ipfs(BigInteger blockId, String blockIpfs, int state) {
        this.blockId = blockId;
        this.blockIpfs = blockIpfs;
    }

    public BigInteger getBlockId() {
        return blockId;
    }

    public void setBlockId(BigInteger blockId) {
        this.blockId = blockId;
    }

    public String getBlockIpfs() {
        return blockIpfs;
    }

    public void setBlockIpfs(String blockIpfs) {
        this.blockIpfs = blockIpfs;
    }

    @Override
    public String toString() {
        return "User{" +
                "blockId=" + blockId +
                ", blockIpfs='" + blockIpfs + '\'' +
                '}';
    }
}
