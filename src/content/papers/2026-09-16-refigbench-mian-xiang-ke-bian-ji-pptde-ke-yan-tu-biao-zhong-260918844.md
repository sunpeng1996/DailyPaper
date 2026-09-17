---
title: 'ReFigBench: Benchmarking Scientific Figure Reconstruction as Editable PowerPoint
  Artifacts'
title_zh: ReFigBench：面向可编辑PPT的科研图表重建评测基准
authors:
- Liyang Fan
- Chi Wei
- Yitai Li
- Xinping Bi
- Guhong Chen
- Chenghao Sun
- Haoxiang Yang
- Qingwen Li
- Kai Yan
- Hong Li
affiliations:
- SZU
- SIAT, CAS
- UCAS
- China Tower Corporation
- SUAT
arxiv_id: '2609.18844'
url: https://arxiv.org/abs/2609.18844
pdf_url: https://arxiv.org/pdf/2609.18844
published: '2026-09-16'
collected: '2026-09-17'
category: Eval
direction: 多模态Agent · 任务评测基准
tags:
- Multimodal Agent
- Benchmark
- Document Agent
- Evaluation
- Tool Use
one_liner: 构建含1000个arXiv真实科研图表的ReFigBench，评测多模态编码Agent的图表重建能力
practical_value: '- 做Agent工具调用评测时，不要仅看API调用正确性等单一指标，需结合最终产物质量+人工盲评的多维度评估，避免误判模型/工具链真实能力

  - 多模态Agent落地时需将模型和运行harness（工具链/执行环境）联合调优，相同模型在不同harness下的性能差异甚至超过流程优化收益

  - 图文转可编辑文档类业务场景（如电商素材转PPT营销物料），需权衡生成保真度和产物可编辑性的冲突，优先对齐用户实际偏好'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：现有多模态编码Agent评测多聚焦短工具调用、API轨迹、截图相似度等代理指标，无法区分错误来源于感知能力、规划逻辑还是运行harness（工具链/上下文管理层）缺陷，缺少面向最终可用产物的端到端评测基准。
**方法关键点**：构建包含1000个arXiv公开真实科研综述图表的ReFigBench基准，任务要求Agent将输入图表转为保留文本、拓扑、布局、原生结构的可编辑PPT；测试4个模型家族的编码Agent在直接代码生成、专用PPTX生成2种工作流，以及2种商业harness下的共10种配置表现；评估融合确定性产物校验、2类大模型自动评分、人工盲评三类维度。
**关键结果**：感知是核心瓶颈，迭代渲染仅能部分缓解；相同模型在不同harness下，专用工作流的收益可正可负，harness差异在相同prompt下即可带来分数波动；专用工作流虽丢失全部原生连接线，但多数场景下人类更偏好其输出，当前最强Agent距离评分上限仍有较大差距。
