---
title: Morphing into Hybrid Attention Models
title_zh: FlashMorph：预训练Transformer转混合注意力模型的高效层选择方法
authors:
- Disen Lan
- Jianbin Zheng
- Yuxi Ren
- Xin Xia
- Xuanda Wang
- Xuefeng Xiao
- Xipeng Qiu
- Yu Cheng
affiliations:
- Fudan University
- ByteDance Seed
- The Chinese University of Hong Kong
arxiv_id: '2606.30562'
url: https://arxiv.org/abs/2606.30562
pdf_url: https://arxiv.org/pdf/2606.30562
published: '2026-06-29'
collected: '2026-06-30'
category: LLM
direction: LLM长上下文效率优化 · 混合注意力
tags:
- Hybrid Attention
- Linear Attention
- Long Context
- LLM Efficiency
- Layer Selection
one_liner: 将混合层选择建模为全局联合优化问题，提出高效可扩展的混合层选择方法
practical_value: '- 长上下文LLM服务（如RAG、Agent会话）降本改造时，混合注意力是高性价比方案，FlashMorph的层选择成本仅为原有方法的1/7，可直接复用
  pipeline 改造现有业务大模型

  - 合成长上下文passkey检索数据做层选择监督信号，比通用文本更能精准选出对召回关键的全注意力层，非常适配RAG类长上下文业务

  - 全局联合优化层门控的思路，解决了孤立评分忽略层间依赖的问题，可迁移到其他架构搜索类任务（如稀疏MoE的专家选择）'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：混合注意力通过保留少量全注意力层、替换其余层为线性注意力，可平衡长上下文LLM的性能与推理效率。将预训练Transformer转换为混合模型的核心挑战，是在全注意力层预算固定的前提下，选出保留全注意力的最优层集合。现有方法依赖固定放置规则或孤立层重要性评分，忽略了层间依赖、冗余与互补性，且层选择成本极高，难以适配大模型规模。

**方法关键点**：
- 将混合层选择建模为预算约束下的全局子集优化问题，把离散选择松弛为连续门控优化：给每个原全注意力层额外配一个通过隐对齐蒸馏得到的线性注意力分支，引入可学习的层间门控插值两个分支的输出
- 层选择阶段冻结所有原模型和线性分支权重，仅优化层门控，使用合成长上下文passkey检索数据做监督，加入线性化正则项鼓励尽可能用线性注意力，降低效率损失
- 优化完成后取门控值最高的TopK层保留全注意力，实例化混合模型后再做标准logits蒸馏和长上下文微调

**关键结果**：基于Qwen3-0.6B/1.7B的实验显示，在256K长上下文NIAH检索任务上，1.7B模型的NIAH-Single-3准确率达到73.2%，远超基线HALO的52.8%；层选择仅消耗20M token、2.1 GPU小时，成本比HALO低7.3倍，比KL-LS低510倍；推理阶段1.7B模型256K预填充速度提升2.81倍，512K解码速度提升2.07倍，可单卡处理原模型OOM的长序列。

最值得记住：仅优化少量层门控的全局联合选择，就能以极低的成本得到远优于启发式方法的混合注意力配置
