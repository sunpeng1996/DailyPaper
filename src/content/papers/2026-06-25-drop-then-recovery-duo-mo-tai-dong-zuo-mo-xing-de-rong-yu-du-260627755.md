---
title: 'Drop-Then-Recovery: How Redundant Are Vision-Language-Action Models?'
title_zh: Drop-Then-Recovery：多模态动作模型的冗余度分析
authors:
- Guoheng Sun
- Kaixi Feng
- Shwai He
- Xiaochuan Gong
- Yexiao He
- Ziyao Wang
- Zheyu Shen
- Wanghao Ye
- Ramana Rao Kompella
- Gaowen Liu
affiliations:
- University of Maryland, College Park
- Cisco Research
arxiv_id: '2606.27755'
url: https://arxiv.org/abs/2606.27755
pdf_url: https://arxiv.org/pdf/2606.27755
published: '2026-06-25'
collected: '2026-07-01'
category: Multimodal
direction: 多模态大模型 · 结构冗余度分析
tags:
- VLA
- Model Redundancy
- Transformer Pruning
- Vision-Language
- Fine-tuning
one_liner: 提出DTR分析协议与GateProbe块排序方法，验证VLA模型语言主干存在极高冗余
practical_value: '- 可复用GateProbe单步敏感度排序方法，对推荐/Agent系统调用的大模型Transformer块做重要性打分，快速定位可裁剪块，降低推理时延与部署成本

  - 针对仅需处理短指令的垂类Agent（如电商客服、推荐query理解Agent），可参考VLA裁剪思路，大幅裁剪LLM主干冗余层，相同微调预算下甚至可提升任务效果

  - DTR「裁剪后微调验证必要性」的分析框架可复用，用于评估垂域大模型各组件（语言/多模态/输出头）的冗余度，优化模型容量分配'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
VLA模型从预训练VLM继承超大规模语言主干，容量远超机器人短指令处理需求，但不同组件的冗余度缺乏量化评估，闭环控制所需的最小模型结构边界不清晰。
### 方法关键点
- 提出Drop-Then-Recovery（DTR）分析协议：通过可控移除指定Transformer块后微调下游任务，验证被移除容量的必要性；
- 配套GateProbe单步虚拟门敏感度指标：基于块对下游动作损失的贡献度排序，保障裁剪选择的可靠性。
### 关键结果
跨多VLA架构、操纵基准、真实工业机器人场景验证得到非对称冗余特性：语言主干对标准机器人操纵任务冗余度极高，视觉/动作通路裁剪容忍度极低；在LIBERO基准上，移除一半LLM块后，相同微调预算下OpenVLA-OFT准确率从95.0%提升至98.3%，仅保留2个语言块即可恢复基线性能。
