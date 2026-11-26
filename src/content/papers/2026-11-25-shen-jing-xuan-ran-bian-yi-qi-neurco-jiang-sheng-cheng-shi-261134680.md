---
title: 'Neural Rendering Compiler: Generative Video Models as Programmable Renderers'
title_zh: 神经渲染编译器NeurCo：将生成式视频模型转化为可编程渲染器
authors:
- Yuxia Zhu
- Xinglong Xu
- Hao Liang
- Linzhuang Sun
- Caijun Jia
- Qifeng Cai
- Jincen Luo
- Lei Li
- Alden Cai
- Asher Qin
affiliations:
- Peking University
- University of Chinese Academy of Sciences
- Tencent
arxiv_id: '2611.34680'
url: https://arxiv.org/abs/2611.34680
pdf_url: https://arxiv.org/pdf/2611.34680
published: '2026-11-25'
collected: '2026-11-26'
category: Multimodal
direction: 多模态生成 · 视频生成可控性优化
tags:
- Video Generation
- Controllable Generation
- Neural Rendering
- Capability Probing
- Intermediate Representation
one_liner: 通过探测冻结束视频生成模型能力边界构建编译层，实现生成式视频可编程可控渲染
practical_value: '- 电商商品营销短视频生成场景，可复用模型能力探测逻辑，提前预判大模型对商品属性、运镜、特效要求的支持度，减少无效生成、提升素材投产比

  - 跨大模型调度场景，可参考NeurCo的模型无关中间表示设计，将用户意图统一拆解为结构化字段，降低多生成模型适配成本

  - 多约束生成任务中，可借鉴不可靠需求自动改写/兜底策略，优先保留核心业务需求，非核心需求自动替换为可执行方案，平衡生成效果与合规性'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
生成式视频模型渲染能力突出，但缺乏传统渲染器（如Blender）的可预测控制接口，能力边界随训练隐式形成，难以稳定执行多约束用户指令。

### 方法关键点
1. NeurCo神经渲染编译器可自动探测冻结束视频生成模型的能力边界，生成模型专属能力手册；
2. 设计模型无关的用户意图中间表示，统一拆解为对象、约束、事件、相机四类结构化字段；
3. 编译阶段保留可靠需求，对不可靠需求选择性改写或替换为可执行的备选策略。
配套构建VComBench基准，包含380个多约束任务，覆盖文生视频、图生视频、参考生视频三类场景。

### 关键结果
在Wan模型上需求满足率从46.8%提升至52.3%，在Minimax H3上从66.5%提升至69.3%，搭配prompt增强工具可获得进一步增益
