---
title: 'HarmTrace: Anchor-Calibrated Decoupled Optimization for Fine-Grained Target
  Identification in Harmful Memes'
title_zh: HarmTrace：锚校准解耦优化实现有害梗图细粒度目标识别
authors:
- Yujia Li
- Yiqun Zhang
- Zihan Cheng
- Yijie Huang
- Tenglong Ye
- Zihan Wang
- Xiaocui Yang
- Shi Feng
- Yifei Zhang
- Daling Wang
affiliations:
- Northeastern University
- Apple Inc.
arxiv_id: '2608.16622'
url: https://arxiv.org/abs/2608.16622
pdf_url: https://arxiv.org/pdf/2608.16622
published: '2026-08-17'
collected: '2026-08-18'
category: Multimodal
direction: 多模态内容安全 · 细粒度实体识别
tags:
- Multimodal-LLM
- Content-Moderation
- Fine-grained-Identification
- SFT
- Policy-Optimization
one_liner: 提出锚校准解耦优化框架HarmTrace与标注数据集Meme3W，大幅提升有害梗图细粒度联合识别准确率
practical_value: '- 电商/广告内容审核场景可复用解耦优化思路：先识别违规属性再识别违规主体，避免仅判违规但漏判攻击对象的badcase，降低合规风险

  - 多任务联合识别场景可参考CTPO+虚拟正锚方案：仅在主任务（如违规判定）输出正确的样本上优化子任务，避免子任务优化拉低主任务精度

  - 细粒度多模态识别任务可参考JRA指标设计：要求所有关联字段联合正确，评估标准更贴近业务对结果完整性的要求'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有多模态有害梗图检测仅做有害性二分类，常出现有害性判定正确但攻击目标、支撑证据识别错误的问题，缺少细粒度标注数据与符合业务需求的联合精度评估标准。
### 方法关键点
1. 构建Meme3W数据集，整合公开有害梗图数据集，补充人工标注的目标类别、实体、文本提及、视觉区域4类细粒度信息；
2. 设计JRA（Joint Record Accuracy）指标，要求有害性标签与所有目标识别字段全正确才计为正例，更贴合实际审核要求；
3. 提出HarmTrace框架：先做实体感知SFT强化目标实体监督，再用CTPO解耦有害性判定与目标识别的优化梯度，仅在有害性判定正确的样本上优化目标识别任务，引入虚拟正锚VPA做优势归一化避免优化偏移。
### 关键结果
在Qwen3-VL-8B骨干上JRA从17.58%提升至52.51%，同时有害性判定准确率同步提升。
