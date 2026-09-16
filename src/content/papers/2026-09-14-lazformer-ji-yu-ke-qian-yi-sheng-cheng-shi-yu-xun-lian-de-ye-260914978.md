---
title: 'LazFormer: Scaling Transformers for Industrial Recommendation via Transferable
  Generative Pre-training'
title_zh: LazFormer：基于可迁移生成式预训练的工业级推荐Transformer
authors:
- Xiaodong Li
- Alin Fan
- Mingyang Li
- Yan Xiao
- Shichao Nie
- Junfeng Zhang
- Shaochuan Lin
- Zhanming Ou
- Tao Luo
- Xiaoyi Zeng
affiliations:
- Alibaba International Digital Commerce Group
arxiv_id: '2609.14978'
url: https://arxiv.org/abs/2609.14978
pdf_url: https://arxiv.org/pdf/2609.14978
published: '2026-09-14'
collected: '2026-09-16'
category: RecSys
direction: 生成式预训练 · 工业推荐排序优化
tags:
- Transformer
- Generative Pre-training
- CTR Prediction
- Ranking
- Long Sequence Modeling
one_liner: 提出工业级可扩展推荐Transformer框架LazFormer，解决预训练负迁移和稀疏参数过拟合问题，已落地阿里电商
practical_value: '- 预训练到排序的特征迁移可复用可迁移残差适配器设计：用零初始化的类LoRA残差分支注入加购、下单等排序专属特征，避免扰动预训练表征空间，缓解负迁移，效果优于直接拼接/前置投影方案

  - 多epoch训练稀疏参数过拟合问题可采用非对称训练策略：每轮epoch开始重置稀疏embedding到预训练状态，只累计更新密集Transformer参数，既能多轮训练充分吸收数据信息，又避免稀疏参数过拟合

  - 长序列排序效率优化可落地粗到细压缩+混合稀疏注意力+请求级范式：保留最近N条短序列做细粒度建模，更早的长序列按组聚合压缩，配合滑动窗口+全局token混合稀疏注意力，同请求多候选共享序列编码，可大幅降本且效果损失极小

  - 线上投入产出比验证：该方案在阿里国际电商首页推荐落地，仅牺牲12%的A10 GPU吞吐量，就拿到GMV+9.85%、IPV+5.21%的显著收益，商业价值明确'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有工业推荐Transformer多从零开始联合优化稀疏与密集参数，算力消耗大、收敛慢；预训练+排序范式存在两大核心痛点：一是预训练与排序的输入特征不一致，直接迁移密集参数易出现负迁移；二是排序阶段多epoch训练易导致十亿级稀疏参数过拟合，冻结稀疏参数又会限制其适配排序目标的能力。
### 方法关键点
- 生成式预训练：基于用户历史交互序列做自回归下一个item预测，联合学习稀疏embedding和密集Transformer参数，为下游排序提供初始化
- 可迁移残差适配器：参考LoRA设计，用零初始化低秩残差分支注入加购、下单等排序专属特征，初始状态无扰动，训练过程中逐步适配排序目标
- 请求感知排序：采用粗到细长序列压缩（保留最近1024条细粒度行为，更早行为按组聚合）、混合稀疏注意力、同请求多候选共享序列编码，大幅降低长序列建模开销
- 非对称多epoch训练：每轮epoch开始重置稀疏参数为预训练状态，密集参数继承上一轮训练结果，既充分吸收数据信号，又避免稀疏参数过拟合
### 关键结果
基于阿里国际电商16M用户、11B token预训练数据，11M用户、370M曝光排序数据实验：相比SOTA基线SORT，CTR AUC+0.74pt、GAUC+1.28pt，CVR AUC+0.55pt、GAUC+0.62pt；线上A/B测试实现IPV+5.21%、订单+3.38%、GMV+9.85%，仅损失12.1%的A10 GPU吞吐量。
### 核心记忆点
工业推荐场景引入生成式预训练时，优先保障稀疏和密集参数的可迁移性，兼顾效果增益和算力开销的设计才能拿到可落地的业务收益
