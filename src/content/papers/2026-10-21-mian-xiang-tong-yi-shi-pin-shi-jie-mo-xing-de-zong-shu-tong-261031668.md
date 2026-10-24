---
title: Reading, Writing, Sharing, and Interacting with the World through Video
title_zh: 面向统一视频世界模型的综述：通过视频读写、共享与交互认知世界
authors:
- Shengqiong Wu
- Meng Luo
- Bobo Li
- Ziwei Liu
- Shuicheng Yan
- Ming-Hsuan Yang
- Philip Torr
- Hao Fei
affiliations:
- University of Oxford
- National University of Singapore
- Nanyang Technological University
- University of California, Merced
arxiv_id: '2610.31668'
url: https://arxiv.org/abs/2610.31668
pdf_url: https://arxiv.org/pdf/2610.31668
published: '2026-10-21'
collected: '2026-10-24'
category: Multimodal
direction: 多模态视频世界模型 · 统一框架综述
tags:
- Video Foundation Model
- World Model
- Video Generation
- Video Understanding
- Multimodal Survey
one_liner: 以世界建模为统一视角梳理视频领域研究，归纳四大核心操作、发展趋势与开放挑战
practical_value: '- 短视频/直播电商推荐场景可复用「Reading」操作的世界属性推断逻辑，从视频内容中提取商品属性、用户交互隐含状态，优化召回排序特征

  - 商品短视频生成场景可参考「Writing」模块的条件生成框架，结合给定商品属性、场景要求生成可控、符合物理因果的营销视频内容

  - 交互型导购Agent可借鉴「Interacting」模块的世界状态更新逻辑，基于用户实时交互动作动态调整视频展示内容与导购策略'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
视频基础模型在视觉序列理解、生成领域进展迅猛，视频世界模型则聚焦捕获视频背后的世界底层动态，两类研究目标不同但核心均关联视频观测与动态世界的映射关系，缺乏统一的梳理视角。
### 方法关键点
以世界建模为统一框架，将观测视频定义为潜在时序世界的部分、有损、时序有序投影，围绕四大互补操作系统梳理相关文献：1. Reading：从观测视频推断世界属性；2. Writing：基于指定/学习到的世界条件合成视频；3. Sharing：通过通用建模机制融合理解与生成能力；4. Interacting：在动作输入和动态观测下预测、更新世界状态。同时明确区分了观测/生成序列的时序一致性与底层世界状态的一致性两个核心概念。
### 关键结果
梳理出领域研究重心正从片段级识别、感知保真度，向持久状态建模、可控演化、物理因果有效性、交互与下游决策导向评估转移，提炼了当前领域核心开放挑战。
