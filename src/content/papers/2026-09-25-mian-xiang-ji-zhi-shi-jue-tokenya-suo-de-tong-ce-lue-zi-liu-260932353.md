---
title: 'Fewer Tokens, More Self-Teaching: On-Policy Self-Distillation for Extreme
  Visual Token Reduction'
title_zh: 面向极致视觉Token压缩的同策略自蒸馏训练框架LT-OPD
authors:
- Junxian Li
- Ruixuan Yang
- Tianao Zhang
- Tiange Xu
- Weisheng Dong
- Yulun Zhang
affiliations:
- Shanghai Jiao Tong University
- Xi’an Jiaotong University
- University of Cambridge
- Xidian University
arxiv_id: '2609.32353'
url: https://arxiv.org/abs/2609.32353
pdf_url: https://arxiv.org/pdf/2609.32353
published: '2026-09-25'
collected: '2026-09-29'
category: Multimodal
direction: 多模态大模型 · 视觉Token压缩效率优化
tags:
- MLLM
- Visual Token Reduction
- On-policy Distillation
- Self-distillation
- Curriculum Learning
one_liner: 通过同策略自蒸馏和渐进式预算课程，大幅提升极致视觉Token压缩下的MLLM性能
practical_value: '- 电商多模态导购/内容审核场景可直接复用LT-OPD训练流程，仅保留5%视觉Token即可降低85% KV cache开销，不损失推理延迟的同时保留80%+模型能力，适配端侧/高并发部署需求

  - 同策略自蒸馏思路可迁移到生成式推荐模型压缩场景：用全参数大模型做冻结教师，压缩小模型在自身生成的轨迹上做分布对齐，解决训练/推理分布mismatch问题

  - 渐进式预算课程学习的训练Trick可直接复用，极端压缩场景下先从高Token预算训练逐步降到目标预算，避免初始阶段生成轨迹质量过低导致训练崩溃'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有视觉Token压缩方法在极致低保留率（如5%）下性能衰减严重，传统蒸馏方案基于固定训练前缀对齐分布，和压缩模型推理时实际遇到的自身生成轨迹分布存在 mismatch，蒸馏增益有限，无法支撑MLLM在端侧、高并发场景（如电商多模态导购、内容审核）的低成本部署。

### 方法关键点
- 提出LT-OPD训练框架：冻结全Token MLLM作为教师，低Token压缩学生模型先自行生成回答轨迹，教师在学生生成的前缀上提供下一词分布监督，用JSD散度对齐两者分布，从根源解决训练-推理分布不匹配问题
- 引入渐进式预算课程学习：训练初期采用较高的Token保留率（如25%），通过cosine衰减逐步降到目标保留率（如5%），避免初始阶段学生生成轨迹质量过低导致训练崩溃
- 构建14K多来源混合训练集LT-14K，覆盖感知、OCR、推理等多类视觉问答任务，提升压缩模型泛化性

### 关键实验
在9个多模态基准上测试，Qwen3.5-4B在5%视觉Token保留率下，平均性能保留率从基线的68.6%提升至82.3%，超过所有训练免、训练类基线，同时降低KV cache开销85.2%、prefill FLOPs 85.4%，无额外推理开销；增益可跨架构迁移到Qwen3.5-9B、GLM-4.6V-9B、LLaVA-OV-1.5-4B等模型，性能优于GRPO、DAPO等通用RL优化方法。

### 核心结论
极致压缩场景下，仅优化Token选择策略的收益远低于将Token选择和适配压缩模型实际生成分布的训练策略结合的收益。
