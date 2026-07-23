---
title: User-Centric Modeling of Transactional Sequences with Explainable State Space
  Models
title_zh: 基于可解释状态空间模型的用户交易序列个性化建模
authors:
- Ivan Palagin
affiliations:
- HSE University
arxiv_id: '2607.20228'
url: https://arxiv.org/abs/2607.20228
pdf_url: https://arxiv.org/pdf/2607.20228
published: '2026-07-22'
collected: '2026-07-23'
category: RecSys
direction: 用户行为序列建模 · Mamba+对比学习
tags:
- Mamba
- SSM
- CoLES
- Contrastive Learning
- User Embedding
- Explainability
one_liner: 将预训练CoLES用户嵌入通过两种策略注入Mamba，提升交易序列建模性能与收敛速度
practical_value: '- 可直接复用两种CoLES+Mamba融合策略：用户预训练嵌入初始化Mamba隐状态、作为前缀拼接输入序列，冷启动时缺嵌入自动退化为原生Mamba，兼容现有业务流程

  - Mamba处理数百/数千条长度的用户行为序列时，比Transformer复杂度低、比RNN长程记忆好，适合电商用户全生命周期行为建模场景

  - 2-3倍的收敛提速可直接降低大样本下的训练算力成本，尤其适配天级别更新的用户画像、推荐召回/排序模型场景

  - 可解释性工具（discretization-step maps、Integrated Gradients）可直接复用，用于定位高价值用户行为事件、解释模型决策逻辑，满足业务合规要求'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
用户行为/交易序列建模是推荐、风控、用户画像等业务的核心基础，现有RNN类编码器梯度消失、长程记忆能力弱，Transformer编码器O(L²)复杂度处理长序列成本极高；Mamba等SSM模型虽具备O(L)复杂度与优秀长程记忆能力，但缺乏用户全局先验信息，收敛慢、效果存在瓶颈。

### 方法关键点
- 预训练CoLES用户嵌入权重冻结，采用两种融合策略：1）经两层投影后作为Mamba第一层的初始隐状态h₀；2）投影为token后作为前缀拼接在输入序列头部
- 特征预处理：数值特征做log变换+z-score归一化，时间戳采用相邻间隔差编码，超参数通过Optuna自动寻优
- 天然兼容冷启动：无预训练CoLES嵌入时自动替换为零向量，模型退化为原生Mamba，无需额外适配逻辑

### 关键结果
实验在Age（银行年龄预测）、MBD（银行产品多标签预测）、Taobao（电商购买预测）三个公开数据集开展，对比原生Mamba、CoLES+线性分类器两个基线：
- 效果提升：Age数据集准确率较原生Mamba高3.2pp，MBD平均ROC-AUC高2.6pp，Taobao ROC-AUC高0.7pp
- 收敛效率：混合模型2-3个epoch达到最优效果，原生Mamba需6个epoch，收敛速度快2-3倍
- 可解释性：电商场景下模型自动过滤低意图浏览事件，高权重聚焦加购、购买等高价值行为

> 最值得记住：预训练全局用户嵌入作为先验注入序列模型，兼顾效果提升与收敛成本下降，是工业级长序列用户建模的高性价比方案。
