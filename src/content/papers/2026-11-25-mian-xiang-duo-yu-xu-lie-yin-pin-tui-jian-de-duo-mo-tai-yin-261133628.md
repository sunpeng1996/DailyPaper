---
title: Multi-Modal Causal Disentanglement for Multi-Domain Sequential Audio Recommendation
title_zh: 面向多域序列音频推荐的多模态因果解耦框架CAMAR
authors:
- Yu Ren
- Pengcheng Li
- Weijun Xu
- Hengzhong Zhou
- Shufeng Ye
- Qiang Xiao
- Dongjing Wang
- Chuanjiang Luo
- Yong Li
affiliations:
- Hangzhou Dianzi University
- NetEase Cloud Music
arxiv_id: '2611.33628'
url: https://arxiv.org/abs/2611.33628
pdf_url: https://arxiv.org/pdf/2611.33628
published: '2026-11-25'
collected: '2026-11-26'
category: RecSys
direction: 多域序列推荐 · 因果解耦 多模态语义ID
tags:
- Multi-Domain Recommendation
- Sequential Recommendation
- Causal Disentanglement
- Multi-modal Embedding
- Semantic ID
- Cold Start
one_liner: 提出因果解耦多域推荐框架CAMAR，结合多模态语义ID缓解负迁移与跨域冷启动
practical_value: '- 多域联合训练负迁移问题可直接复用「域不变+域特化表征拆分」方案，叠加正交约束+域对抗训练切断虚假因果路径，仅允许通用偏好跨域交互

  - 跨域语义对齐可采用RQ-VAE将多模态特征编码为跨域共享语义ID，无需用户行为共现即可关联不同域的相似内容，适配内容类电商、音视频场景

  - 跨域冷启动可加轻量成对域转移MLP（TransNet），用stop-gradient隔离源域和目标域梯度，小参数开销即可补全冷启动域的用户表征

  - 多域训练可采用三阶段调度：先训单域召回损失稳定基础效果，再加正交约束，最后开启对抗和迁移损失，避免训练波动'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前多域序列推荐存在两大落地痛点：一是高流量域主导共享参数空间，导致低流量域出现负迁移、效果受损；二是传统ID类协同信号依赖跨域活跃用户，语义关联但行为重叠少的域无法有效对齐，跨域冷启动问题突出。

### 方法关键点
- 基于结构因果图将用户偏好拆解为域不变通用偏好与域特化场景偏好，通过正交约束、域对抗训练、跨域交互路径限制三大机制切断负迁移的虚假因果路径，仅允许域不变分量参与跨域信息融合
- 用RQ-VAE将文本、视觉、音频三类预训练特征编码为跨域共享的可训练语义ID，无需用户行为共现即可对齐不同域的物品语义
- 轻量TransNet网络通过成对小MLP补全用户未活跃域的表征，加入stop-gradient避免梯度干扰，缓解跨域冷启动
- 采用三阶段训练策略保证收敛稳定性：先优化召回损失，再加正交约束，最后开启对抗训练和迁移网络损失

### 关键结果
在网易云音乐3域工业数据集（3.56M用户，覆盖歌曲、歌单、播客）和Amazon公开数据集上对比9个SOTA基线，离线效果全面领先：播客域Hit@5提升29.7%，歌单域Hit@5提升11.5%，歌曲域Hit@5提升5.9%；在线A/B测试获全域正向收益：歌曲播放时长+1.0%，歌单点赞率+3.0%，播客播放时长+1.6%。

**最值得记住的一句话**：多域联合优化的核心是隔离域特化噪声、对齐通用语义信号，因果解耦+多模态语义ID是缓解负迁移和冷启动的高性价比组合方案
