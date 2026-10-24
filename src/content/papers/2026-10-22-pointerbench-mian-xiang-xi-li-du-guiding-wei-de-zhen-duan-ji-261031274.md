---
title: 'PointerBench: A Diagnostic Benchmark for Fine-Grained GUI Grounding'
title_zh: 《PointerBench：面向细粒度GUI定位的诊断基准》
authors:
- Valentino Sacco
- Saurabh Pandey
- Alexander Florian Jercher
- Maximilian Schilling
affiliations:
- Sapienza University of Rome
- Warmwind AG
arxiv_id: '2610.31274'
url: https://arxiv.org/abs/2610.31274
pdf_url: https://arxiv.org/pdf/2610.31274
published: '2026-10-22'
collected: '2026-10-24'
category: Agent
direction: Agent 电脑操作GUI定位评测
tags:
- GUI Grounding
- Multimodal LLM
- Agent Evaluation
- Computer Use
- Benchmark
one_liner: 推出含1500对截图-指令的细粒度GUI定位诊断基准，覆盖表格、长文本、百款专业应用三类场景
practical_value: '- 做电商自动化操作Agent（如后台上下架、数据导出）时，可直接复用PointerBench的细粒度表格、长文本定位评测逻辑，验证Agent界面操作准确率

  - 优化电商网页/APP导购Agent交互时，可参考基准的像素级目标标注方法，构建私域GUI操作评测集，降低Agent误触率

  - 针对长文本客服工单、商家后台长列表的定位需求，可优先优化字符级text grounding能力，这类场景现有通用多模态模型准确率仅~60%，优化空间大'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
现有端到端电脑操作Agent基准侧重长流程任务完成度，GUI定位基准仅覆盖常规控件、有限专业界面，缺乏细粒度定位能力的诊断工具。
### 方法关键点
构建1500组带像素级精确标注的截图-指令对，覆盖三类测试场景：
1.  Sheets：电子表格细粒度子元素识别与几何定位
2.  Text：长文本字符级定位
3.  Pro：覆盖100款专业应用的混合GUI定位
同时评测通用多模态模型与39种专用GUI定位配置。
### 关键结果
整体平均准确率上，Claude Fable 5达83.2%、GPT-5.6 Sol达77.7%、专用模型UI-Venus-2-9B达54.5%；其中长文本定位是最困难场景，三款模型对应准确率仅为69.6%、53.4%、25.8%，细粒度GUI定位仍有极大优化空间。
