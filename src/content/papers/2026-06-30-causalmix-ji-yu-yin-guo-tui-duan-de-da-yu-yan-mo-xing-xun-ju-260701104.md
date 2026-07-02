---
title: 'CausalMix: Data Mixture as Causal Inference for Language Model Training'
title_zh: CausalMix：基于因果推断的大语言模型训练数据混合优化框架
authors:
- Zinan Tang
- Yukun Zhang
- Shaomian Zheng
- Zhuoshi Pan
- Qizhi Pei
- Dingnan Jin
- Jun Zhou
- Yujun Wang
- Biqing Huang
affiliations:
- Tsinghua University
- Ant Group
- Renmin University of China
arxiv_id: '2607.01104'
url: https://arxiv.org/abs/2607.01104
pdf_url: https://arxiv.org/pdf/2607.01104
published: '2026-06-30'
collected: '2026-07-02'
category: LLM
direction: 大语言模型SFT · 因果驱动数据混合
tags:
- Causal Inference
- Data Mixture
- Supervised Fine-Tuning
- CATE
- LLM Training
one_liner: 将LLM SFT数据混合优化转化为因果推断问题，跨模型跨数据池泛化性更强，性能优于现有基线
practical_value: '- 垂直领域SFT（如电商文案生成、客服Agent训练）可复用该框架，用小参数量模型做少量proxy实验，估计不同域数据的边际收益调混合比例，避免暴力网格搜索的高成本

  - 数据特征优先选择HES、Normalized Loss、Writing Style三个维度即可，过多特征会在小样本场景引发维度灾难，反而降低效果

  - 多技能Agent的SFT阶段可复用CATE解释器，量化不同技能数据的冲突（如常识记忆与逻辑推理的负向影响），合理平衡数据比例避免技能遗忘

  - DML正交化trick可迁移到其他超参数优化场景，先残差化混淆变量再估计目标效应，降低分布偏移对优化效果的影响'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM SFT阶段的数据混合优化方法大多依赖静态数据分布假设，数据池更新、模型规模扩容时需要重新全量实验，训练成本极高；同时以验证损失为核心优化目标的方法容易忽略不同数据域的边际收益，无法适配动态数据状态，下游任务表现不稳定。
### 方法关键点
- 因果建模：将数据域混合比例作为treatment，数据池的HES（复杂度）、Normalized Loss（难度）、Writing Style（质量）作为协变量，下游任务性能作为outcome，转化为连续treatment的CATE估计问题
- 正交估计：采用DML双机器学习对treatment和outcome做残差化，消除数据状态的混淆偏差，用CausalForestDML估计各域数据的边际收益
- 鲁棒策略输出：支持两种策略：① 基于边际收益的闭式解析直接输出混合比例；② 采样10w候选混合比例取Top100平均，降低推理噪声
### 关键实验
基于Tulu 3 SFT数据集（5个域）的512次Qwen2.5-0.5B proxy实验训练因果模型，对比RegMix、DoReMi、DMO等基线：800K数据规模下训练Qwen2.5-7B，平均得分62.28，比SOTA基线DMO高1.93个点；跨到未见过的LongCoT数据集、跨模型到Qwen3-4B，平均得分66.66，比基线最高值高1.92个点。
### 核心结论
没有通用的最优数据混合比例，只有当前数据状态下的最优边际收益组合。
