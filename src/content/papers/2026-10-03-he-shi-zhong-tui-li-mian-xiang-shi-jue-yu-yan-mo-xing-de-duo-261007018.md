---
title: 'When to Rethink: Learning Multi-Perspective Self-Verification for Vision-Language
  Models'
title_zh: 《何时重推理：面向视觉语言模型的多视角自验证学习方法》
authors:
- Ziquan Zhu
- Hanruo Zhu
- Si-Yuan Lu
- Morris Yu-Chao Huang
- Yicheng Lin
- Wei Han
- Tianlong Chen
- Mingyuan Wu
- Hanchao Yu
- Gaojie Jin
affiliations:
- University of Leicester
- Nanjing University of Posts and Telecommunications
- University of North Carolina at Chapel Hill
- Amazon
- Meta AI
arxiv_id: '2610.07018'
url: https://arxiv.org/abs/2610.07018
pdf_url: https://arxiv.org/pdf/2610.07018
published: '2026-10-03'
collected: '2026-10-13'
category: Reasoning
direction: 多模态大模型 · 自验证推理优化
tags:
- VLM
- Self-Verification
- Multimodal Reasoning
- Self-Correction
- Inference Optimization
one_liner: 提出多视角自验证MOTIVE框架，无需外部裁判即可提升VLM多模态推理的可靠性与效率
practical_value: '- 多模态商品理解/审核场景可复用多视角验证思路，避免单一prompt或规则的漏判误判，可分别从属性合规、文案真实性、图像匹配度多个维度校验商品信息可信度

  - Agent多轮推理决策可引入可靠性得分触发重推理逻辑，对比固定多轮推理范式可减少不必要的计算开销，尤其适合实时性要求高的电商导购、搜索query理解场景

  - 自验证模块训练时可直接以结果正确性为监督信号对齐可靠性得分，无需额外标注验证维度的标签，降低业务落地的标注成本'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
VLM在多模态推理任务中易生成似是而非的错误答案，现有自验证方案依赖单一准则或固定prompt，可靠性评估不稳定、覆盖不全，且无外部裁判时难以兼顾推理正确率与效率。
### 方法关键点
1. 系统性实验验证：验证器能力越强判断越可靠，且验证效果对prompt高度敏感，不存在跨任务通用的最优prompt
2. MOTIVE框架从互补视角对每个候选答案做评估，通过正确性对齐的多视角验证学习，输出与答案真实正确性高度相关的可靠性得分
3. 推理阶段用可靠性得分决策：高置信答案直接返回，低置信答案触发历史信息引导的重推理
### 关键结果
在多个多模态基准数据集、不同VLM backbone上性能均优于现有SOTA自验证、自校正基线，同时可减少不必要的推理轮次，无需外部裁判即可实现更高效可靠的多模态推理
