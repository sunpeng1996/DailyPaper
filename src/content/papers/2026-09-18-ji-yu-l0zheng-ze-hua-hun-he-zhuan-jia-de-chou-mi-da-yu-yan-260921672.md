---
title: Accelerating Dense LLMs via L0-regularized Mixture-of-Experts
title_zh: 基于L0正则化混合专家的稠密大语言模型推理加速方法
authors:
- Zhenyu Zhang
- Jiudong Yang
- Zhaowen Tao
- Meng Chen
affiliations:
- YZW
- FuTu AI
- Wise AI
arxiv_id: '2609.21672'
url: https://arxiv.org/abs/2609.21672
pdf_url: https://arxiv.org/pdf/2609.21672
published: '2026-09-18'
collected: '2026-09-21'
category: LLM
direction: LLM推理优化 · L0正则化MoE
tags:
- MoE
- L0-regularization
- LLM Inference
- Dynamic Batching
- Corpus Curation
one_liner: 用仅30B token训练将稠密LLM转为L0正则化MoE，实现最高2.5倍无性能损失的推理加速
practical_value: '- 业务场景中部署LLM做文案生成、query理解、Agent推理时，可采用L0-MoE方案替代量化/剪枝，在几乎不损失效果的前提下获得2倍以上推理速度提升，降低推理成本

  - 构建垂直领域MoE专家时，可复用CCM聚类混淆矩阵的语料筛选方法，仅用小量级领域语料即可完成专家训练，不需要大规模预训练语料

  - MoE训练阶段可直接复用动态批调度策略，先易后难安排训练语料，能显著提升路由的专家选择准确率，减少训练波动

  - 对于现有稠密LLM的低成本升级，可直接冻结非MLP参数仅训练FFN层的L0掩码，训练成本低，适配业务快速迭代需求'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM推理加速方案中，量化、剪枝、蒸馏普遍伴随明显性能损失，传统MoE模型则需要万亿级token预训练语料与极高计算资源，中小团队与业务场景难以低成本落地无损失的LLM加速。

### 方法关键点
- 语料筛选：提出聚类混淆矩阵（CCM）采样方法，基于BGE-M3语义向量与K-means聚类，从全量语料中筛选30B token的多领域子集，覆盖专家训练所需的语义场景
- 专家构建：基于稠密LLM预训练权重，冻结非MLP参数，用L0正则化约束FFN层维度选择，为每个语义领域训练专属专家，自动保留对性能影响最大的隐层维度
- 训练优化：采用动态批调度策略，先用语义区分度低的语料训练路由的基础选择能力，再逐步引入高区分度语料优化token级路由效果，同时加入负载均衡损失与Z-Loss约束专家分配均匀性

### 关键实验
在RedPajama语料上训练，基于Llama-3-8B、Mistral-7B、Qwen2-7B三个开源稠密LLM验证，对比GPTQ量化、LLM Shearing剪枝、RKD+CoT蒸馏等基线：L0-MoE在MMLU、GSM8K、HumanEval、BBH四个基准上性能与原稠密模型持平甚至略有提升（Mistral-7B版本平均涨点1%），最高实现2.5x推理加速，优于量化/剪枝方案的1.8-2.6x加速（后者伴随2-9%的性能损失）。

### 核心结论
仅用30B小语料即可将现有稠密LLM低成本转换为MoE，实现无性能损失的2倍以上推理加速，适配业务场景的低成本LLM部署需求。
