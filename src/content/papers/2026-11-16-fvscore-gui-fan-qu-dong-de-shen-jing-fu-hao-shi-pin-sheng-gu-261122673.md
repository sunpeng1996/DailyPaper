---
title: 'FVScore: Specification-Driven Neuro-Symbolic Video Evaluation'
title_zh: FVScore：规范驱动的神经符号视频生成评估框架
authors:
- Do Xuan Long
- Long T. Le
- Yiwen Song
- Min-Yen Kan
- Tomas Pfister
- Yale Song
affiliations:
- Google Cloud AI Research
- National University of Singapore
arxiv_id: '2611.22673'
url: https://arxiv.org/abs/2611.22673
pdf_url: https://arxiv.org/pdf/2611.22673
published: '2026-11-16'
collected: '2026-11-19'
category: Eval
direction: 生成式内容 · 视频生成自动评估
tags:
- Video Generation
- Evaluation
- Neuro-Symbolic
- Temporal Logic
- MLLM
one_liner: 提出神经符号视频评估框架FVScore，匹配人类判断同时输出带时间戳的可解释评估报告
practical_value: '- 电商短视频广告、种草视频的自动质量评估可复用显式+隐式约束拆解思路：显式匹配运营/用户需求，隐式覆盖常识约束，比端到端MLLM整体判断准确率更高

  - 直播切片、时序类营销内容的违规检测可复用软时序算子+感知校准流程，既能准确定位问题时间戳，还能过滤人类感知不到的微小违规，降低误判率

  - 多模态Agent的事实校验模块可借鉴命题拆解+专用工具调用架构，将大的校验任务拆分为可验证的小命题，调用OCR、目标检测等专用工具执行，可解释性强且方便debug'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有视频生成评估方案依赖整体式MLLM判断或传统视语言指标，普遍存在与人类判断对齐度低、无法定位具体时序违规点的问题，复杂多事件场景下缺陷尤为明显。

### 方法关键点
1. 将评估需求拆解为两类命题：匹配prompt明确要求的显式命题，覆盖物理、时序、跨模态常识约束的隐式命题；
2. 调用专用感知工具对每个命题做接地，生成置信度时序轨迹，采用线性时序逻辑启发的软时序算子完成校验；
3. 新增感知感知校准步骤，仅保留人类可感知的违规，最终输出带时间戳、证据锚定的可解释报告及得分。

### 关键结果
在公开基准及复杂多事件测试集上，相比现有整体式、Agent类评估器，FVScore与人类判断的相关性更高，同时评估准确率、可解释性显著更优。
