---
title: Evidence-Backed Video Question Answering
title_zh: 带可验证时空视觉证据支撑的视频问答技术与基准
authors:
- Shijie Wang
- Honglu Zhou
- Ziyang Wang
- Ran Xu
- Caiming Xiong
- Silvio Savarese
- Chen Sun
- Juan Carlos Niebles
affiliations:
- Salesforce
- Brown University
arxiv_id: '2607.11862'
url: https://arxiv.org/abs/2607.11862
pdf_url: https://arxiv.org/pdf/2607.11862
published: '2026-07-13'
collected: '2026-07-15'
category: Multimodal
direction: 多模态大模型 · 视频问答可解释性优化
tags:
- Video LLM
- Visual Grounding
- Video QA
- Multimodal Reasoning
- Benchmark Dataset
one_liner: 提出需同步输出时空视觉证据的E-VQA任务，配套基准数据集与微调方案，提升Video LLM可解释性与grounding能力
practical_value: '- 短视频/直播场景的多模态问答Agent可借鉴时空-语义对齐思路，给回答追加对应视频片段/视觉证据，大幅提升用户对答案的信任度，比如服饰带货场景下回答款式问题时同步返回对应裁剪片段

  - 多模态大模型微调时可复用这套细粒度grounding标注自动生成流水线，低成本构建业务场景微调数据，无需大量人工标注像素级掩码

  - 电商内容风控、虚假宣传识别Agent可复用E-VQA思路，让风控结论绑定对应时空视觉证据，提升结果可解释性与审核回溯效率'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有Video LLM执行视频问答任务时多为黑箱，仅输出文本答案缺乏可验证视觉grounding，传统可解释方案依赖文本理由或稀疏 bounding box，无法捕捉遮挡、非刚性形变等复杂视频动态，且QA准确率与实际视觉感知能力存在解耦，单纯缩放模型规模无法解决该问题。
### 方法关键点
1. 提出E-VQA新任务范式，要求模型同步输出语义答案+精准时空证据（时间片段、稠密跟踪目标分割掩码）
2. 发布ST-Evidence人类验证基准，是首个同时支持判别式、生成式像素级grounding的评测集
3. 搭建可扩展自动化生成流水线，产出160k规模ST-Evidence-Instruct数据集，打通高层语义推理与细粒度视觉grounding
4. 基于该数据集微调具备grounding能力的Video LLM
### 关键结果
7B规模微调模型对比同尺寸UniPixel基线，t-mean指标提升27.2，J&F指标提升13.8，构建了可解释、带证据支撑的视频理解强基线。
