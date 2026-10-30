---
title: 'IntReal: A Real-World Dataset and Benchmark for Multimodal Interleaved Generation'
title_zh: IntReal：面向多模态交错生成的真实世界数据集与评测基准
authors:
- Shaohan Yu
- Jie Qin
- Wende Tan
- Haiwen Diao
- Limeng Qiao
- Yueming Lyu
- Chenyang Si
affiliations:
- PRLab, Nanjing University
- Meituan
- Imperial College London
- S-Lab, Nanyang Technological University
arxiv_id: '2610.38425'
url: https://arxiv.org/abs/2610.38425
pdf_url: https://arxiv.org/pdf/2610.38425
published: '2026-10-27'
collected: '2026-10-30'
category: Multimodal
direction: 多模态交错生成 · 数据集与评测基准
tags:
- Multimodal Generation
- Dataset
- Benchmark
- UMM
- Evaluation
one_liner: 开源10万级多模态交错生成数据集与7维度细粒度自动化评测套件
practical_value: '- 可复用7维度细粒度多模态生成评测框架，用于电商种草文案+配图的生成效果自动评估，替代部分人工标注

  - 可参考IntReal数据集的跨模态内容对齐标注逻辑，优化电商场景图文混排生成的训练数据构造流程

  - 复用「单模态训练可提升交错生成效果」结论，图文混排任务可先分别优化文生文、文生图模块，降低端到端训练成本'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
当前多模态交错生成（图文混排生成）领域缺乏高质量标注训练数据与细粒度评测体系，制约统一多模态模型（UMM）的能力迭代。
### 方法关键点
1. 构建IntReal-100K数据集，包含10万条真实世界图文交错样本、超53万张图片，覆盖攻略、知识、教程、故事4大类；
2. 推出7维度细粒度评测套件，覆盖文本丰富度/逻辑性、图片美观度/多样性、数量合规性、上下文保真度、主体一致性，支持模型能力粗到细诊断。
### 关键结果数字
评测指标间冗余度极低（最大两两斯皮尔曼相关系数≤0.42），与人评一致性达83.3%，不同专家评测器一致性>0.9；基准测试证明单模态训练可有效提升交错生成效果，无需全阶段联合图文训练。
