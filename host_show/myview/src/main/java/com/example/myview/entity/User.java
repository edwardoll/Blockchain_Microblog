package com.example.myview.entity;

import javax.persistence.*;
import java.io.Serializable;
import java.math.BigInteger;

@Entity
@Table(name = "blog_mail")
public class User implements Serializable {
    private static final long serialVersionUID = 1L;

    @Id
    @GeneratedValue
    @Column(name = "block_id")
    private BigInteger blockId;
    @Column(name = "text_id", nullable = false)
    private String textId;
    @Column(name = "text_hash", nullable = false)
    private String textHash;
    @Column(nullable = false)
    private String text;

    public User() {
    }

    public User(BigInteger blockId, String textId, String textHash, String text) {
        this.blockId = blockId;
        this.textId = textId;
        this.textHash = textHash;
        this.text = text;
    }

    public BigInteger getBlockId() {
        return blockId;
    }

    public void setBlockId(BigInteger blockId) {
        this.blockId = blockId;
    }

    public String getTextId() {
        return textId;
    }

    public void setTextId(String textId) {
        this.textId = textId;
    }

    public String getTextHash() {
        return textHash;
    }

    public void setTextHash(String textHash) {
        this.textHash = textHash;
    }

    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    @Override
    public String toString() {
        return "User{" +
                "blockId=" + blockId +
                ", textId='" + textId + '\'' +
                ", textHash='" + textHash + '\'' +
                ", text='" + text + '\'' +
                '}';
    }
}
