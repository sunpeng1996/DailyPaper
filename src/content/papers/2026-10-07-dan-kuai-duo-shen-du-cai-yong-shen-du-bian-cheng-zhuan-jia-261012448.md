---
title: 'One Block, Multiple Depths: Recurrent Vision Transformers with Depth-Programmed
  Experts'
title_zh: 单块多深度：采用深度编程专家的循环视觉Transformer
authors:
- Adrian Bulat
- Yassine Ouali
- Georgios Tzimiropoulos
affiliations:
- Samsung AI Cambridge
- Technical University of Iasi
- Queen Mary University of London
arxiv_id: '2610.12448'
url: https://arxiv.org/abs/2610.12448
pdf_url: https://arxiv.org/pdf/2610.12448
published: '2026-10-07'
collected: '2026-10-10'
category: Training
direction: Transformer架构优化 · MoE参数高效复用
tags:
- MoE
- Vision Transformer
- Parameter Efficiency
- Recurrent Transformer
- Knowledge Distillation
one_liner: 提出基于深度编程专家的循环ViT，参数量降70%仍匹配全深度ViT精度
practical_value: '- 推荐系统Transformer排序/召回模型可借鉴深度编程专家的权重合并思路，复用FFN参数，大幅降低大模型部署存储开销

  - 弹性深度训练思路可复用至多场景推荐适配：同一份checkpoint通过调整深度参数匹配不同算力的端侧、服务端部署需求

  - 做LLM4Rec的MoE优化时，优先选择权重空间合并方案，效果优于同计算预算下的token分发、输出混合方案'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
传统ViT堆叠多层独立Transformer块存在显著参数冗余，不同层表征相似度高，如何在保留深度依赖计算能力的前提下压缩参数量是核心痛点。
### 方法关键点
1. 提出reViT架构，用单个Transformer块循环执行替代全深度层栈，不同循环深度的FFN由共享专家库的凸组合生成，通过连续归一化深度坐标编程混合权重；
2. 采用权重空间合并的MoE方案，在单FFN计算预算下效果优于token分发、输出混合等同类MoE方案；
3. 支持弹性深度训练，同一份checkpoint可通过重采样坐标适配不同推理深度。
### 关键结果
- 从头训练的reViT-B/16参数量减少70%，精度匹配DeiT III；
- 8专家版本经DINOv2蒸馏后几乎保留教师全部线性探测精度，可迁移到分类、分割、深度预测任务。
