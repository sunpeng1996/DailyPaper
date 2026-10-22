---
title: 'Beyond the Sequentiality Bottleneck: A Hybrid Diffusion-Autoregressive Framework
  for Efficient Multimodal Reasoning'
title_zh: 突破序列性瓶颈：混合扩散-自回归多模态推理框架
authors:
- Wei Cai
- Jian Zhao
- Yuchen Yuan
- Xuelong Li
affiliations:
- Peking University
- Institute of Artificial Intelligence (TeleAI), China Telecom
arxiv_id: '2610.28584'
url: https://arxiv.org/abs/2610.28584
pdf_url: https://arxiv.org/pdf/2610.28584
published: '2026-10-20'
collected: '2026-10-22'
category: Reasoning
direction: 大模型推理 · 扩散-自回归混合架构
tags:
- Diffusion Language Model
- Autoregressive Model
- Multimodal Reasoning
- Planner-Executor
- Chain-of-Thought
- Hybrid LLM
one_liner: 提出融合扩散模型并行规划与自回归模型精确执行的CoRAL框架，突破多模态推理的序列性瓶颈
practical_value: '- 混合架构可直接迁移到电商Agent推理链路：用轻量DLM并行生成多组候选CoT路径（如优惠凑单逻辑、多商品组合推荐方案），再用ARM做优选和最终话术生成，兼顾推理效率与输出准确性

  - RDC奖励引导的扩散训练方法可复用：针对推荐/广告场景的业务目标（如点击率、转化率）设计reward函数，融入扩散模型去噪训练，让生成的候选内容更贴合业务需求

  - 多模态理解任务可复用拆分思路：商品图理解、用户多模态需求解析等复杂任务拆分为「并行探索候选解+串行精排生成」两阶段，既突破纯自回归的序列瓶颈，又避免纯扩散的语义漂移问题'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
自回归模型（ARM）推理时存在「序列性瓶颈」，长Chain-of-Thought生成成本随长度线性上升，且易出现误差累积；扩散语言模型（DLM）支持并行生成、探索空间效率高，但语义连贯性差、生成质量整体不及ARM，二者能力高度互补，现有方案未充分融合二者优势解决多模态推理的效率与质量平衡问题。
### 方法关键点
- 非对称规划-执行（APE）架构：DLM作为Planner，通过并行去噪一次性生成K条多样化推理轨迹；ARM作为Executor，仅需1次前向pass即可完成所有候选轨迹的评估选优，再基于最优轨迹合成高保真最终答案
- RDC（Reward-Guided Denoising for CoT）训练目标：将结果导向的奖励信号融入扩散模型的去噪损失，由传统的分布拟合优化转向目标导向的推理轨迹生成，损失由基础扩散损失+奖励加权的轨迹对数似然损失两部分组成，提升Planner生成轨迹的正确性
- 双模式信息交互：Planner生成的轨迹可直接以文本形式输入Executor，也可通过轻量投影层将Planner隐状态映射到Executor嵌入空间，减少文本序列化带来的信息损失
### 关键结果
在CapMAS、CapArena、DetailCaps-4870等多模态理解基准，以及Trip-Planning、GPQA等复杂推理基准上测试：1. Trip-Planning任务准确率达0.31，是最优ARM基线Qwen2.5-VL-7B的2.58倍，throughput达0.42，领先所有基线；2. GPQA任务准确率0.39、throughput 0.58，均为SOTA；3. CapMAS的CLAIR、Coverage、Factuality指标分别达86.75、58.36、83.59，全面超过Qwen2.5-VL、GLM-4v等顶级ARM。
> 最值得记住的一句话：DLM擅长并行探索候选解空间，ARM擅长因果校验与高保真输出，二者的非对称混合架构是突破大模型推理序列性瓶颈的高性价比路径
