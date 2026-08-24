---
title: 'DAMOS: Learning Distortion-Aware Speech Quality Assessment through Explicit
  Distortion Localization'
title_zh: DAMOS：基于显式失真定位的失真感知语音质量评估方法
authors:
- Naiyuan Li
- Li Dong
- Diqun Yan
arxiv_id: '2608.21176'
url: https://arxiv.org/abs/2608.21176
pdf_url: https://arxiv.org/pdf/2608.21176
published: '2026-08-21'
collected: '2026-08-24'
category: Other
direction: 语音质量评估 · 显式失真定位
tags:
- Speech Quality Assessment
- MOS Prediction
- Frame-level Annotation
- Distortion Localization
- Cross-domain Generalization
one_liner: 构建首个帧级失真标注语音数据集，提出融合定位信息的DAMOS语音MOS预测框架，性能超现有SOTA
practical_value: '- 若业务涉及语音类场景（如电商智能客服语音、直播语音质检、语音广告合成效果评估），可复用「细粒度局部标注辅助粗粒度全局预测」的范式，类似推荐中用点击序列细粒度信号优化CTR预估的思路，用局部失真信号提升整体质量打分的准确性

  - 做语音AIGC（如虚拟主播语音生成、语音搜索TTS）效果校验时，可采用两阶段框架：先训练小模型定位感知敏感的失真区域，再将区域特征融合进全局打分 pipeline，更贴合人的主观感知

  - 框架的强跨数据集泛化特性，可减少不同语音场景下的标注成本，适合业务多语音场景快速复用'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有语音质量评估方法仅用 utterance 级 MOS 做粗粒度监督，无法定位人感知敏感的局部失真区域，预测精度和跨场景泛化性受限，不符合合成语音等场景失真局部出现、感知质量由敏感区域主导的特性。
### 方法关键点
1. 构建首个带帧级失真标注的部分失真语音数据集，训练定位模型生成失真提示信号；
2. 提出DAMOS框架，将显式失真定位信息作为辅助特征融入MOS预测流程，加权感知敏感区域的特征权重。
### 关键结果
在多个公开基准数据集上效果持续超越现有SOTA，跨数据集泛化能力显著提升，验证了显式失真定位对语音质量评估的有效性。
