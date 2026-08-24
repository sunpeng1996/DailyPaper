---
title: Asymmetric Capacity Allocation in Self-Refinement Pipelines
title_zh: 自优化流水线的非对称算力分配策略
authors:
- Zhuoyi Yang
- Ian G. Harris
- Salar Hashemitaheri
- Cassie Huang
- Yuangang Li
- Hyunwoo Oh
- Paul Dourish
- Tony Givargis
- Mohsen Imani
- Li Zhang
affiliations:
- University of California, Irvine
- Drexel University
arxiv_id: '2608.21345'
url: https://arxiv.org/abs/2608.21345
pdf_url: https://arxiv.org/pdf/2608.21345
published: '2026-08-21'
collected: '2026-08-24'
category: Agent
direction: Agent自优化流水线算力分配优化
tags:
- Self-Refinement
- LLM Agent
- Inference Optimization
- Model Allocation
- Cost Efficiency
one_liner: 通过跨模型多基准实验验证自优化三阶段对模型大小敏感度差异，指导低成本多阶段LLM系统设计
practical_value: '- 搭建带自优化的LLM Agent（如商品文案生成、推荐理由生成、客服应答系统）时，优先把高算力预算分配给初始生成器和最终优化器，纠错阶段用小模型即可，可在几乎无损效果下降低30%+推理成本

  - 自优化流水线不要用比generator小2个参数级以上的refiner，否则会出现「越改越差」的问题，甚至不如不做优化

  - 哪怕用最小规格的critic（如0.6B参数的小模型），也比完全去掉纠错阶段的效果更好，不需要为了省成本跳过critic环节

  - 该结论跨Qwen3、Gemma3两个主流开源模型家族通用，不需要针对业务所用模型重新验证，可直接套用'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前LLM自优化（生成-纠错-优化）流水线普遍采用同规格模型跑全流程，或凭经验分配各阶段模型，无系统研究三阶段对模型容量的需求差异，导致大量算力浪费。而自优化是LLM Agent、多阶段内容生成系统的核心组件，亟需可落地的低成本优化方案。
### 方法关键点
- 采用控制变量实验设计：固定其中两阶段的模型大小，仅调节第三阶段的参数规格，隔离每个阶段对模型大小的敏感度
- 覆盖2类主流开源模型家族（Qwen3共6种参数规格、Gemma3共4种参数规格），5类跨领域基准任务（规划、摘要、逻辑推理、代码优化、文本生成）
- 设置无critic基线，验证critic模块的实际增益
### 关键结果
- 效果对refiner和generator的敏感度是critic的3~10倍：refiner性能波动范围最高达50个百分点，generator最高达37.5个百分点，critic最高仅9个百分点
- 最小规格critic（如Qwen3 0.6B）相比无critic基线，平均提升3.7~11个百分点的效果，仅比最大规格critic低1~3个百分点
- 规格过小的refiner会导致12/30的实验场景效果不如初始生成结果，最差降幅达20个百分点
> 最值得记住的结论：自优化流水线算力分配要「重生成、重优化、轻纠错」，不要给critic分配过多算力
