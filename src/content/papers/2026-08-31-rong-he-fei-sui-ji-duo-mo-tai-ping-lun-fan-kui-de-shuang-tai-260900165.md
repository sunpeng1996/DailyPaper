---
title: Two-Sided State-Space Models for Sequential Recommendation with Non-Random
  Multimodal Review Feedback
title_zh: 融合非随机多模态评论反馈的双边状态空间序列推荐模型
authors:
- Ziwen Pan
- Zihan Liang
- Ruoxuan Xiong
affiliations:
- Emory University
arxiv_id: '2609.00165'
url: https://arxiv.org/abs/2609.00165
pdf_url: https://arxiv.org/pdf/2609.00165
published: '2026-08-31'
collected: '2026-09-02'
category: RecSys
direction: 序列推荐 · 多模态评论建模
tags:
- Sequential Recommendation
- Multimodal Review
- State Space Model
- User Item Dynamics
- MNAR
one_liner: 设计双边状态空间模型同时建模用户/商品动态，融合非随机多模态评论信号提升序列推荐效果
practical_value: '- 评论模态的有无本身是强信号：可将用户是否上传图片、评论长度是否偏离历史均值等模式作为特征加入现有推荐模型，无需复杂多模态内容理解即可获得增益

  - 商品侧动态状态可落地：给商品维护带正负反馈不对称衰减的状态向量，负反馈衰减更慢的设计符合用户决策逻辑，尤其适合家电、美妆等高评价权重的电商品类

  - 局部图消息传递优化用户偏好：以用户最近交互商品为锚点，传播关联商品反馈信息到用户状态，比全局GNN成本低，可直接嵌入现有序列推荐的用户建模模块

  - 多模态非随机缺失思路可复用：不要直接对缺失模态补0，而是将模态缺失作为独立embedding加入融合层，在广告、医疗等多模态缺失普遍的场景均可迁移'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有序列推荐普遍将评论视为被动静态信号，忽略两个核心问题：一是评论生成是非随机的，模态是否存在、表达模式偏离用户/商品历史的情况本身携带强信号；二是评论会动态改变商品声誉，且会向关联商品溢出，影响后续用户决策。双边平台的用户偏好和商品状态均持续演化，静态建模方式效果存在明显瓶颈。
### 方法关键点
- 多模态评论编码：除内容外，额外编码模态存在标识、当前评论与用户/商品历史表达的偏差特征，解决非随机模态缺失的信息浪费问题
- 用户状态演化：融合时间趋势特征，以用户最近交互商品为锚点，通过局部item graph做轻量消息传递，将关联商品反馈信息融入用户状态
- 商品状态演化：设计正负反馈不对称衰减的carryover记忆模块，负反馈半衰期（4.62个月）显著长于正反馈（2.77个月），符合用户对负面评价更敏感的行为规律
- 训练加入漂移、carryover、可靠性三类辅助损失约束状态演化合理性，主损失采用温度缩放的BPR pairwise损失
### 关键结果
在6个亚马逊品类数据集+Goodreads Fantasy图书数据集上对比BSARec、HM4SR等SOTA基线：6个亚马逊品类上Recall@20相对BSARec提升14.8%~18.8%，相对HM4SR平均提升11.7%；Goodreads上Recall@20相对HM4SR从0.5191提升至0.5847，涨幅12.6%；消融实验显示商品状态更新、局部消息传递、用户状态更新分别带来3.5%、2.79%、2.5%的Recall@20损失。
> 最值得记住的结论：双边平台推荐建模不能只做用户侧动态，商品侧的动态演化尤其是正负反馈的不对称影响，是易被忽略的高性价比增益点
