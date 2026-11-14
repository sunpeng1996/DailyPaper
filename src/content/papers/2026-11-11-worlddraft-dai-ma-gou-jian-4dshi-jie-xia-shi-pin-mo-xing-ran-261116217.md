---
title: 'WorldDraft: If Code Builds the World, Can Video Models Just Render It?'
title_zh: WorldDraft：代码构建4D世界下视频模型渲染能力评测基准
authors:
- Zhiyu Hou
- Wen-Jie Shu
- Harold Haodong Chen
- Weilin Ruan
- Chenfei Liao
- Liuzhou Zhang
- Disen Lan
- Xiaogang Xu
- Qi Chen
- Ser-Nam Lim
affiliations:
- SUSTech
- ZODA
- HKUST
- CUHK
- HKUST(GZ)
arxiv_id: '2611.16217'
url: https://arxiv.org/abs/2611.16217
pdf_url: https://arxiv.org/pdf/2611.16217
published: '2026-11-11'
collected: '2026-11-14'
category: Multimodal
direction: 多模态生成 · 4D视频渲染评测
tags:
- Multimodal Agent
- Video Generation
- 4D Rendering
- Benchmark
- Visual Prompting
one_liner: 提出评测代码生成4D世界渲染能力的基准WorldDraft与即插即用视觉提示优化策略
practical_value: '- 电商商品短视频生成场景可复用WorldDraft-Primer提示策略，在保留预设运镜、动作结构的同时提升外观还原度，减少源素材信息泄漏

  - 多模态Agent生成可控动态内容时，可参考本文的3×3粒度-对齐度因子设计，平衡结构保真与外观生成效果

  - 做生成式内容合规/效果评测时，可复用WorldDraft的双维度（世界保留+视觉实现）评估框架，量化可控生成质量'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
多模态编码Agent将4D世界构建与视觉生成解耦后，视频模型作为生成式渲染器的能力缺乏统一量化评估框架，结构保留与外观生成的性能冲突问题未被系统验证。
### 方法关键点
提出WorldDraft基准，包含432组严格配对测试用例，覆盖48个可执行4D世界族、6类动态场景，采用3×3因子设计正交控制草稿粒度、外观对齐度变量；同时提出即插即用的WorldDraft-Primer视觉提示策略，无需微调即可优化冻结视频渲染器的双维度表现。
### 关键结果数字
12款代表性视频模型评测显示：冲突源提示会引发最高64%的源信息泄漏；更丰富的草稿结构可锚定动态逻辑但会降低外观保真度；Primer策略可同时提升世界保留与视觉实现两个核心指标。
