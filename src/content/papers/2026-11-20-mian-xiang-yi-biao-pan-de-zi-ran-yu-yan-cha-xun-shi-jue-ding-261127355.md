---
title: 'Show Me the Answer: Visual Grounding on Dashboards'
title_zh: 面向仪表盘的自然语言查询视觉定位技术研究
authors:
- Yuefei Zhang
- Songyin Tang
- Yile Cai
- Yuqi Bu
- Liuwu Li
- Yanna Lin
- Zikun Deng
- Yi Cai
affiliations:
- South China University of Technology
- Shenzhen Polytechnic University
- Guangxi Normal University
- University of Waterloo
arxiv_id: '2611.27355'
url: https://arxiv.org/abs/2611.27355
pdf_url: https://arxiv.org/pdf/2611.27355
published: '2026-11-20'
collected: '2026-11-27'
category: Multimodal
direction: 多模态交互 · 仪表盘视觉定位
tags:
- Visual Grounding
- Multimodal Interaction
- Dashboard
- Two-stage Framework
- Benchmark
one_liner: 提出两阶段VGD-Net解决仪表盘自然语言查询视觉定位，配套发布专用评测基准VGD-Bench
practical_value: '- 电商BI看板、运营分析后台的自然语言查询交互场景，可复用两阶段定位架构：先召回query相关图表，再做图表内细粒度元素定位，比端到端多模态定位效果更优、可解释性更强

  - 涉及分层结构的跨模态检索/定位任务，可参考阶段分解思路，每个子模块单独优化，整体性能比端到端更可控，还可接入中间结果的用户反馈修正机制

  - 垂直领域多模态任务评测可复用VGD-Bench的分层设计思路，拆分全链路、子模块分别验证，便于快速定位性能瓶颈'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有视觉定位研究多聚焦自然图像，针对多图表布局、细粒度元素的仪表盘场景研究不足，无法满足BI看板、分析系统自然语言交互中精准定位查询相关视觉元素的需求。

### 方法关键点
两阶段VGD-Net框架对齐用户查找仪表盘信息的行为逻辑：第一阶段执行query感知的图表召回，先定位到相关的单张图表；第二阶段在召回的图表内做细粒度视觉元素定位，输出对应bounding box。配套构建专用评测基准VGD-Bench，覆盖图表召回、图表内定位、全链路VGD三个互补评测维度。

### 关键结果
VGD-Net性能优于主流多模态基线，全链路任务mean IoU达57.06，成功率达66.82，两个子阶段的性能也优于现有方案，验证了阶段分解思路在VGD任务上的可靠性与可解释性优势。
