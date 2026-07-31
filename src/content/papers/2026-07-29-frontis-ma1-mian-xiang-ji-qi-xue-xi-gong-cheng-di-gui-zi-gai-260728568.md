---
title: 'Frontis-MA1: Training an AI4AI Model towards Recursive Self-Improvement in
  Machine Learning Engineering'
title_zh: Frontis-MA1：面向机器学习工程递归自改进的AI4AI模型训练
authors:
- Junlin Yang
- Che Jiang
- Yu Fu
- Tianwei Luo
- Can Ren
- Weizhi Wang
- Kaikai Zhao
- Hongyi Liu
- Yuxin Zuo
- Yuru Wang
affiliations:
- Frontis.AI
- Tsinghua University
- Horizon Research
arxiv_id: '2607.28568'
url: https://arxiv.org/abs/2607.28568
pdf_url: https://arxiv.org/pdf/2607.28568
published: '2026-07-29'
collected: '2026-07-31'
category: Agent
direction: Agent 元进化与递归自改进
tags:
- AI4AI
- Recursive Self-Improvement
- Meta-Evolution Agent
- MLE
- Execution Grounded Training
one_liner: 提出全栈OpenMLE系统与元进化Agent Frontis-MA1，低算力下达到前沿闭源模型MLE性能
practical_value: '- 可复用Draft/Improve/Debug/Crossover四个原子操作的设计范式，优化推荐系统调优、广告策略迭代类Agent的工作流，减少无意义的探索

  - 执行反馈驱动的SFT+RL训练方法可迁移到电商/广告的A/B测试闭环，将实验结果直接转化为模型迭代的监督信号，提升策略迭代效率

  - OpenMLE-Evo的三因素（质量/进度/新颖性）父节点选择策略，可直接用于推荐召回多目标排序、实验流量分配，平衡现有最优解和新方向探索

  - 沙箱隔离、异步反馈处理的执行环境方案可复用在电商大模型生产管线中，降低业务迭代的试错成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有AI4AI研究缺乏统一全栈框架支撑可验证的递归自改进（RSI）落地，机器学习工程（MLE）作为AI4AI的具象测试场景，需要同时覆盖可执行任务环境、执行反馈驱动训练、长程进化搜索的完整体系，才能让Agent实现持续自我迭代，避免依赖单纯的模型参数扩容。
### 方法关键点
- 全栈OpenMLE系统分为三层：OpenMLE-Gym提供5758个经过质量过滤的多模态可执行MLE任务与沙箱执行环境，输出标准化结构化反馈；OpenMLE-ERL基于执行反馈做SFT+RL训练，对齐Draft/Improve/Debug/Crossover四个可复用的原子进化算子，作为训练和推理的统一接口；OpenMLE-Evo基于结构化经验做长程搜索，通过质量/进度/新颖性三因素加权选择父节点，按需合成算子适配的上下文记忆，减少无效探索
- 训练元进化Agent Frontis-MA1：训练数据与评估基准完全去重，形成学习-进化的闭环，避免数据泄露
### 关键实验结果
- 基准测试用MLE-Bench Lite，单任务仅分配12小时RTX4090（12GB显存）算力：Frontis-MA1-35B搭配OpenMLE-Evo比基座Qwen3.6-35B的Medal Average从39.39%提升到60.61%，搭配OpenMLE-Evo-Max进一步提升到71.21%，超过GPT-5.5+Codex，接近GPT-5.6 Sol与2.8T参数的Kimi K3
- 跨域迁移到NatureBench Lite：固定框架替换为训练后模型，Match-SOTA从50%提升到70%；固定模型替换为OpenMLE-Evo框架，Match-SOTA从20%提升到50%
### 核心结论
递归自改进的核心是让Agent的训练和推理共享同一套可执行的进化算子，形成学习和搜索的闭环，可在低算力预算下达到超越大参数闭源模型的效果。
