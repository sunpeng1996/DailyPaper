---
title: 'STAR: Structured Tokenization and Target-Aware Interest Representation for
  PCVR Prediction'
title_zh: 面向点击后转化率预测的结构化分词与目标感知兴趣框架STAR
authors:
- Yimeng Xu
- Haorui Zhang
- Yingqi Song
- Ying Jiang
- Lan Ma
affiliations:
- Tsinghua University
- Peking University
arxiv_id: '2608.12986'
url: https://arxiv.org/abs/2608.12986
pdf_url: https://arxiv.org/pdf/2608.12986
published: '2026-08-13'
collected: '2026-08-14'
category: RecSys
direction: 推荐排序 · 点击后转化率(PCVR)预测
tags:
- PCVR
- CVR Prediction
- Target-Aware Modeling
- Contrastive Learning
- Feature Engineering
one_liner: 基于HyFormer优化特征处理与目标感知兴趣建模，PCVR预测AUC较官方基线提升1.65‰
practical_value: '- 高基数稀疏特征处理可复用「基数截断+频率重映射+序列哈希」方案，既能保留长尾信号又控制embedding表规模，适配工业级海量稀疏特征场景

  - 训练推理一致性可参考「序列化特征映射表、超参数到checkpoint侧文件」的方案，彻底解决特征分布偏移导致的线上离线效果不一致问题

  - 主损失之外可新增动态权重的InfoNCE对比学习辅助损失，对齐用户物品表征，实测能稳定提升排序AUC，额外计算开销极低

  - 区分真实0值与padding的缺失值处理技巧可直接复用，避免特征歧义，能带来千分级的AUC增益'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业级点击后转化率（PCVR）预测是电商/广告推荐排序的核心任务，现有HyFormer等统一序列-特征架构存在三类落地痛点：高基数稀疏特征因embedding表成本过高被直接丢弃，丢失大量长尾用户/物品信号；用户历史行为兴趣建模未充分关联候选物品，目标感知性不足；缺失值、padding零值混淆与特征分布偏移易引发训练推理不一致，导致优化不稳定。
### 方法关键点
- 结构化特征分词：对高基数稀疏特征采用基数截断+频率重映射+序列哈希方案，在控制embedding规模的前提下保留长尾信号；新增掩码区分真实零值与padding，补充绝对时间、序列长度、截断比例等元特征，按语义聚合为异构token输入
- 目标感知兴趣建模：基于DIN风格查询解码器，以候选物品特征为锚点生成序列查询，计算注意力加权的用户兴趣向量，通过残差连接更新查询表征
- 训练优化与一致性保障：新增动态权重的加权InfoNCE对比学习辅助损失，对齐用户-物品表征；序列化所有特征映射表、超参数到checkpoint侧文件，推理时直接加载对齐，彻底消除训练推理偏移
### 关键实验
在KDD Cup 2026腾讯UniRec 2000万条PCVR数据集上测试，相比官方基线，全优化模型验证AUC提升0.0149、测试AUC提升0.0166；ablation显示贡献最大的模块为时间特征（移除后测试AUC下降0.0020），其次是缺失值与padding区分处理（下降0.0013）、InfoNCE对比损失（下降0.0003）、DIN查询解码器（下降0.0002）。
**核心结论**：PCVR场景下，针对特征、建模、训练流程的定向优化收益远高于单纯扩大模型容量，且落地成本更低
