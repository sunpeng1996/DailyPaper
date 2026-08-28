---
title: 'GUI-Primitives: Diagnosing Spatial Reasoning Failures in Vision-Language GUI
  Grounding'
title_zh: GUI-PRIMITIVES：视觉语言模型GUI空间推理故障诊断基准
authors:
- Md Abrar Jahin
- Md Rizwan Parvez
affiliations:
- University of Southern California
- USC Information Sciences Institute
- Qatar Computing Research Institute
arxiv_id: '2608.21832'
url: https://arxiv.org/abs/2608.21832
pdf_url: https://arxiv.org/pdf/2608.21832
published: '2026-08-21'
collected: '2026-08-28'
category: Agent
direction: Agent GUI交互空间推理能力评估
tags:
- GUI-Grounding
- VLM
- Spatial-Reasoning
- Benchmark
- Computer-Use-Agent
one_liner: 发布含994个对比样本的7类GUI空间关系诊断基准，定位VLM GUI Grounding核心缺陷
practical_value: '- 开发GUI交互类Agent（如电商后台自动操作Agent、客服工单处理Agent）时，可先用GUI-PRIMITIVES筛选VLM底座，优先选择空间推理能力达标的模型，避免上线后高频点击错控件

  - 推理侧优化优先选择Set-of-Mark（SoM）标注候选控件的方案，可直接提升35-57pp的控件选择准确率，无需微调

  - 不要在GUI空间推理场景浪费精力尝试CoT或激活 steering，实验证明这两类方法无显著效果，优化ROI极低

  - 诊断Agent点击错误时优先排查候选控件定位能力，60%-92%的错误来自点击位置落在候选区外，而非空间关系理解错误'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前计算机使用Agent依赖GUI Grounding能力将自然语言指令映射到屏幕控件点击，但现有基准无法区分模型错误是来自空间关系理解偏差还是控件定位失败，当Agent点错按钮时无法定位根因，亟需受控的诊断工具。

### 方法关键点
- 构建994个对比样本对，每对共用同一张截图和锚点控件，仅修改空间关系词（如left↔right、inside↔outside），正确目标在两个指定候选间切换，排除截图显著性、固定答案偏好等捷径
- 覆盖7类GUI常用空间原语：水平/垂直位置、包含关系、对齐关系、邻近度、列表序号、遮挡，兼顾真实UI-Vision截图和合成截图两类数据源
- 5名标注者验证196个子集，well-formedness的Fleiss κ达0.94，目标选择κ达0.79，基准质量可靠

### 关键结果
- 测评19款VLM，最强的Claude Opus 4.7严格点选准确率仅32%，比人类准确率96.9%低65pp
- 60%-92%的预测落在两个候选控件区域外，仅包含、遮挡两类原语的候选内选择率接近0.5，其余原语候选内选择率达0.82-0.9，核心错误来自控件定位而非关系理解
- GUI-PRIMITIVES准确率与ScreenSpot-Pro准确率的Spearman相关系数达0.74，可有效预测下游GUI Grounding性能
- 训练-free优化中，仅给两个候选打标记的SoM方案可提升35-57pp准确率，CoT和激活 steering无显著收益

**最值得记住的一句话：当前VLM在GUI场景的空间推理瓶颈是候选控件定位能力，而非关系语义理解，优先通过标记候选区的方案可快速提效。**
