---
title: 'MPIE-Bench: Benchmarking Anatomically Plausible Multi-Person Interaction Editing'
title_zh: MPIE-Bench：面向解剖学合理的多人交互编辑基准
authors:
- Jiajia Lin
- Mingxuan Du
- Tuowen Zhou
- Benfeng Xu
- Hongtao Xie
affiliations:
- University of Science and Technology of China
- Metastone Technology, Beijing, China
arxiv_id: '2607.27616'
url: https://arxiv.org/abs/2607.27616
pdf_url: https://arxiv.org/pdf/2607.27616
published: '2026-07-29'
collected: '2026-08-01'
category: Eval
direction: 多模态生成评估 · 多人交互编辑
tags:
- Evaluation Benchmark
- Text-to-Image Editing
- Multimodal Generation
- 3D Human Mesh
- VLM-as-a-Judge
one_liner: 提出含2500样本的多人交互编辑基准与几何评估指标，比VLM评审更贴合人类判断
practical_value: '- 电商营销/广告素材生成的多人物交互场景评估，可复用基于3D人体网格的解剖合理性、交互贴合度两个维度的指标，替代易过饱和的VLM
  checklist评审

  - 生成多人出镜的广告/商品展示图时，可接入预训练多人网格重建模块做生成后质检，过滤肢体融合、穿模等不符合常识的低质素材

  - 业务侧构建自定义生成内容评估基准时，可参考其从真实视频挖掘样本、按交互类型/接触密度分层标注的思路'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有文生图/个性化编辑模型生成多人接触类交互场景时，普遍存在肢体融合、额外肢体、身体穿模等解剖/几何错误，现有评估方案尤其是VLM评审checklist易出现分数饱和，无法识别这些人类肉眼可见的错误。
### 方法关键点
1. 构建MPIE-Bench，包含从视频挖掘的2500个编辑三元组样本，覆盖405个场景、14类交互、4个接触密度等级（C0-C3）；
2. 提出MPIE-Eval评估框架，基于开源预训练多人网格重建模型，从两个维度打分：Anatomy维度校验所有人体区域是否对应完整重建人体，Interaction维度校验人体间穿透度、表面距离是否符合指令要求的接触状态。
### 关键结果
测试10个主流编辑模型，Anatomy维度最高得分0.65，Interaction维度最高得分0.72，无模型在两个维度同时表现优异，相同样本的VLM checklist评分均高于0.95；5人标注验证显示该评估框架比零样本VLM评审更贴合人类判断，指标排名在所有超参数消融下保持稳定。
