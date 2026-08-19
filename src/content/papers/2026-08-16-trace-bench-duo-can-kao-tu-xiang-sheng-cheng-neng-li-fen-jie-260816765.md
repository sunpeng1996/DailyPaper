---
title: 'TRACE-Bench: Decomposing and Diagnosing Multi-Reference Image Generation'
title_zh: TRACE-Bench：多参考图像生成能力分解与诊断基准
authors:
- Haoran Wang
- Chaofan Ma
- Ran Yi
- Lizhuang Ma
affiliations:
- Shanghai Jiao Tong University
arxiv_id: '2608.16765'
url: https://arxiv.org/abs/2608.16765
pdf_url: https://arxiv.org/pdf/2608.16765
published: '2026-08-16'
collected: '2026-08-19'
category: Eval
direction: 多模态生成 · 评测基准
tags:
- Multimodal Generation
- Image Generation
- Evaluation Benchmark
- Capability Decomposition
- Fault Localization
one_liner: 提出基于4种原子算子的多参考图像生成评测基准，支持细粒度能力打分与故障定位
practical_value: '- 电商多模态物料（定制商品图、AI海报）生成的评测可复用原子算子拆分思路，将复杂多参考生成任务拆解为锚定、解耦、属性绑定、组合四个环节，避免仅靠整体效果评估的局限性

  - 生成式推荐的多模态item生成场景，可参考算子对齐的评测协议，对每个生成环节做单独能力打分，快速定位模型瓶颈，降低调优成本

  - 多模态Agent的视觉生成模块故障排查，可复用诊断树递归错误定位方法，精准定位能力短板，减少问题定位耗时'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有多参考图像生成评测按预定义任务类型划分，存在覆盖碎片化、复杂度不可控、无细粒度诊断能力的问题，无法定位模型具体能力短板。
### 方法关键点
将多参考生成任务拆解为Anchor、Disentangle、Apply、Compose四种原子算子，任意多参考prompt都可表示为算子组合公式，复杂度用算子槽位数量量化；基于631个公式模板、4000余张覆盖多元艺术风格与真实物体的参考图，构建包含1~8个槽位共1600个评测用例的TRACE-Bench，配套算子对齐的单能力打分协议、支持递归错误定位的诊断树分析方法。
### 关键结果
评测9个主流多参考生成模型发现：核心能力瓶颈为Disentangle与Apply（属性绑定），最优模型的属性保真度仅0.74，场景级组合能力表现相对更好。
