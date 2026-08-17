---
title: 'Intern-S2-Mobius: Foundation Model with Decoupled Knowledge and Reasoning'
title_zh: Intern-S2-Mobius：知识与推理解耦的基础模型
authors:
- Kai Chen
- Jifeng Ding
- Ning Ding
- Jiaye Ge
- Lixin Gu
- Yicheng Gu
- Qipeng Guo
- Ermo Hua
- Haian Huang
- Haozheng Hou
affiliations:
- Shanghai AI Laboratory
arxiv_id: '2608.14290'
url: https://arxiv.org/abs/2608.14290
pdf_url: https://arxiv.org/pdf/2608.14290
published: '2026-08-13'
collected: '2026-08-17'
category: LLM
direction: 大语言模型 · 知识推理解耦架构
tags:
- LLM
- Knowledge-Reasoning Decoupling
- Inference Acceleration
- MoE
- Architecture Design
one_liner: 提出知识与推理解耦的Mobius架构，同等推理能力下实现近4倍端到端推理加速
practical_value: '- 可复用知识推理解耦思路，将推荐/Agent系统中通用知识库（如商品属性、用户标签）与推理逻辑（匹配、排序逻辑）分离，降低迭代时的知识遗忘风险，减少重复推理计算

  - 借鉴动态隐式推理设计，在生成式推荐/Agent多轮推理场景中，将中间推理过程内化到连续向量空间迭代，避免输出冗长的中间CoT token，大幅降低生成延迟，提升用户体验

  - 大规模部署时可参考其知识存储与推理参数分离的硬件适配思路，将高频访问的推理参数驻留GPU显存，低频知识参数存储于SSD按需加载，降低大模型部署的显存成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前Transformer架构面临双重瓶颈：一方面缩放参数、数据、推理链的边际收益持续收窄，长CoT推理会产生大量冗余token，推理成本随链长非线性增长；另一方面降低注意力复杂度的优化往往牺牲模型能力，难以平衡效果与推理效率，现有架构知识与推理绑定的设计限制了数据效率、推理速度的进一步提升。

### 方法关键点
- 解耦知识存储与推理算子：将原Transformer层绑定的FFN（知识存储）抽离为全局共享的Memory向量库，所有层的Self-Attn（推理算子）可直接访问全量知识，间接实现双向残差连接，深层也能访问浅层对应的知识
- 动态隐式推理设计：将推理过程内化到连续隐向量迭代，无需逐token生成中间CoT即可完成多轮知识检索与推理优化，最后一次性输出高信息密度的token，可动态分配不同token的计算预算
- 大参数量下采用类MoE的块划分策略稀疏激活共享FFN，平衡存储规模与计算效率

### 关键实验
- 从零训练7B模型：仅用Transformer基线62.6%的训练数据即可达到同等MMLU得分，数据效率提升1.6倍
- 基于Qwen3.5-35B持续预训练的Intern-S2-Mobius：在MMLU Pro、GPQA Diamond等10个通用/科学任务上平均得分优于基线，端到端推理速度提升近4倍，同等任务下输出token长度平均缩短1.2~5倍

### 核心结论
知识与推理解耦的架构设计，比单纯优化注意力复杂度或缩放参数，更有可能突破当前大模型效果与效率的平衡瓶颈
