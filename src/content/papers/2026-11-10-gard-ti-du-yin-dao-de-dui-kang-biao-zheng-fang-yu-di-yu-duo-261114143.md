---
title: 'GARD: Gradient-Guided Adversarial Representation Defense against Backdoors
  in Multimodal Contrastive Learning Models'
title_zh: GARD：梯度引导的对抗表征防御 抵御多模态对比学习模型后门
authors:
- Yuhong Wang
- Yujun Cai
- Lei Feng
- Songze Li
affiliations:
- Southeast University
arxiv_id: '2611.14143'
url: https://arxiv.org/abs/2611.14143
pdf_url: https://arxiv.org/pdf/2611.14143
published: '2026-11-10'
collected: '2026-11-12'
category: Multimodal
direction: 多模态对比学习 · 后门防御
tags:
- Multimodal Contrastive Learning
- Backdoor Defense
- CLIP
- Adversarial Probe
- Representation Learning
one_liner: 提出无需感知攻击目标与触发器的多模态对比学习模型后门事后防御方案GARD
practical_value: '- 电商多模态检索/推荐场景使用CLIP等预训练多模态模型时，可直接复用GARD做后门修复，规避恶意投毒样本触发的错误召回/排序，推理无额外开销适配线上部署

  - 全局+局部互补的对抗探针设计可迁移到推荐系统投毒攻击检测环节，识别不同类型的投毒触发特征，提升系统鲁棒性

  - 扰动表征与干净锚点重对齐的思路可复用在生成式推荐的语义表征优化中，降低对抗样本对生成推荐结果的干扰'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
多模态对比学习模型（如CLIP）易受局部补丁、全局扰动等多种类型的后门攻击，现有事后防御方案要么残留后门风险，要么依赖对攻击目标、触发器的准确预估，泛用性不足。
### 方法关键点
基于后门编码器的结构依赖表征敏感度观测（全局扰动优先暴露分布式后门，局部补丁扰动对局部后门更有效），设计无目标/触发器感知的事后防御GARD：1. 优化互补的全局+局部对抗探针，最大化偏移干净图像表征；2. 将扰动后的表征与脱离计算图的干净锚点重对齐，同时保留图文对齐能力；3. 推理阶段无额外计算开销，适配线上部署。
### 关键结果
在6种视觉后门攻击、2种CLIP视觉backbone的12组组合测试中，GARD将所有场景下的攻击成功率降至1%以下，同时保持与原模型相当的干净样本准确率。
