---
title: 'DASH: Divergence-Adaptive Supervision Horizons for On-Policy Self-Distillation
  of Reasoning Models'
title_zh: DASH：面向推理模型同策略自蒸馏的散度自适应监督方法
authors:
- ZhiYan Hou
- Xinyu Tang
- Hongyan An
- Jianjin Zhang
- Weizhen Wang
- Yunyun Han
- Gengsheng Li
- Xiangzhao Hao
- Haiyun Guo
- Wenbin Hu
affiliations:
- 中国科学院自动化研究所
- EverMind
- Shanda Group
- 中国科学院大学
- 武汉大学
arxiv_id: '2608.06243'
url: https://arxiv.org/abs/2608.06243
pdf_url: https://arxiv.org/pdf/2608.06243
published: '2026-08-06'
collected: '2026-08-07'
category: Training
direction: LLM训练优化 · 同策略自蒸馏
tags:
- On-Policy Self-Distillation
- Knowledge Distillation
- LLM Training
- Reasoning LLM
- KL Divergence
one_liner: 提出散度自适应的同策略自蒸馏权重分配方法，无额外前向开销，推理准确率最高提升3.2个百分点
practical_value: '- 做LLM微调/自蒸馏时可直接复用DASH的加权逻辑：计算每个token与序列平均散度的gap生成自适应门控，反向聚合分配损失权重，无需额外前向开销，几乎无成本提升效果

  - 电商搜索/推荐的长序列生成（如商品卖点生成、多轮导购话术生成）蒸馏任务，可借鉴该序列感知的权重分配策略，给偏离教师分布更大的token分配更高权重，提升生成质量稳定性

  - Agent的工具调用/思考链蒸馏场景，可复用该方法替代均匀加权的蒸馏损失，适配思考链的时序依赖特性，用更低训练成本提升推理准确率'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
RLVR 用可验证的序列级奖励优化 LLM 推理能力，但奖励稀疏、信用分配难度大；现有 On-Policy Self-Distillation (OPSD) 虽然提供了稠密 token 级监督，但对所有位置的散度损失均匀加权，忽略了生成过程中师生分布偏差的时序演化特征——相同局部散度在不同偏差历史下对最终结果的影响差异极大，均匀加权无法适配这种时序差异。

### 方法关键点
- 以每个 token 的局部正向 KL 散度为基础，计算其与整个序列平均散度的 gap，生成自适应传播门（停止梯度回传）：低于平均散度的位置门控值更高，允许后续偏差信号传播；高于平均的位置门控更低，限制传播
- 采用反向多步聚合方式，从序列末尾向前递归计算每个 token 的聚合损失权重，最终损失为所有位置聚合值的平均，无需额外的师生前向传播，仅增加极少量的后向扫描计算
- 本地散度计算支持词汇表压缩，保留教师 Top100 token + 剩余合并尾项的配置即可保留98%以上的效果增益，大幅降低计算量

### 关键结果
在 Qwen3 1.7B/4B/8B 三个规模模型上验证，训练数据为 OpenThoughts-Math-30K，在 AIME2024、AIME2025、HMMT2025 三个数学推理基准上对比 SFT、GRPO、OPSD、PW-OPSD 等7个基线，DASH 在所有模型-基准组合上均取得最优，相比基础 OPSD 平均准确率分别提升3.2、1.4、1.6个百分点，无额外前向开销，额外后向计算占比<1%。

最值得记住的一句话：同策略自蒸馏的效果提升核心不在于加大监督强度，而在于根据偏差的时序演化动态分配权重，几乎无额外成本的序列感知加权就能带来显著收益。
