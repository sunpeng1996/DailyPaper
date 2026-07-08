---
title: 'SCOReD: Student-Aware CoT Optimization for Recommendation Distillation'
title_zh: 面向推荐蒸馏的学生感知思维链优化框架SCOReD
authors:
- Haz Sameen Shahgir
- Yufei Li
- Frank Shyu
- Luke Simon
- Sandeep Pandey
- Xi Liu
- Yue Dong
affiliations:
- University of California Riverside
- Meta AI
arxiv_id: '2607.05734'
url: https://arxiv.org/abs/2607.05734
pdf_url: https://arxiv.org/pdf/2607.05734
published: '2026-07-07'
collected: '2026-07-08'
category: GenRec
direction: 生成式推荐 · CoT蒸馏优化
tags:
- CoT Distillation
- Generative Recommendation
- Knowledge Distillation
- LLM4Rec
- Reranking
one_liner: 提出学生感知的推荐CoT蒸馏优化框架，兼顾效果提升与推理长度压缩
practical_value: '- 做生成式推荐CoT蒸馏时，优先对大模型原始推理轨迹做推荐专属分段（历史/偏好/候选/排序/验证/最终结果），剪去冗余的无意义验证步骤，可同时提升SFT效果、降低推理延迟

  - CoT压缩需适配目标学生模型，可复用学生模型</think>token注意力权重评估分段重要性的方法，比通用LLM摘要压缩的输出格式错误率降低46%，不会出现压缩后性能暴跌的问题

  - 压缩操作选择的奖励函数可直接复用该工作的设计：综合学生生成正确答案的概率、编辑后长度、学生侧分段困惑度三个维度，平衡效果、效率、学生适配性

  - 若小模型生成式推荐SFT阶段已经通过高质量蒸馏数据逼近大老师效果，后续RLHF、自蒸馏等优化很难拿到额外增益，资源可优先投向前端数据治理'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前生成式推荐依赖大模型的CoT推理轨迹蒸馏来让小模型获得推理能力，但推荐场景下大模型的CoT存在大量冗余：平均每条轨迹重复验证答案3.2次，79%的验证步骤完全不改变最终排序。直接用原始轨迹做SFT会让小模型学会冗余推理，延迟高、效果差；通用CoT压缩方法未适配推荐场景特性和学生模型分布，会导致性能下降、输出格式错误率飙升。
### 方法关键点
1. 轨迹分段：将大模型原始CoT拆分为6类推荐专属分段：购买历史分析、用户偏好建模、候选分析、中间排序、验证、最终排序
2. 重要性打分：用待训练学生模型的</think>结束符对每个分段的平均注意力权重，将分段分为高/中/低三档，对应不同的操作集合（高：保留/重写；中：重写/融合；低：融合/裁剪）
3. 奖励选操作：基于「学生生成正确答案的对数概率 - 长度惩罚 - 学生侧分段困惑度惩罚」的奖励函数选最优操作，保证压缩后的轨迹适配学生分布
### 关键结果
基于Amazon Beauty数据集实验，老师模型为Gemma-4-26B，学生为0.6B Qwen3：
- 相比原始SFT，NDCG提升1.56%、Recall@5提升1.9%，推理长度降低27.3%，输出解析错误率从2.82%降至1.52%
- 优化后的0.6B小模型效果超过35B Qwen-3.6，接近26B老师模型水平
- 后续叠加DAPO强化学习、OPSD自蒸馏均无明显增益，SFT阶段的蒸馏数据优化已经挖尽小模型潜力

最值得记住的一句话：推荐场景的CoT压缩不能只追求长度最短，必须适配学生模型的分布，才能同时实现效果提升和推理加速。
