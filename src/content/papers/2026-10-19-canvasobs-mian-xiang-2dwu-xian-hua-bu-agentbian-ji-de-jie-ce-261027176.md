---
title: 'CanvasObs: Structured Spatial Observation for Agent Editing on 2D Infinite
  Canvases'
title_zh: CanvasObs：面向2D无限画布Agent编辑的结构化空间观测框架
authors:
- Jiahao Xu
- Haohui Wang
- Rebecca Faust
- Dawei Zhou
- Chris North
affiliations:
- Virginia Tech
- Tulane University
arxiv_id: '2610.27176'
url: https://arxiv.org/abs/2610.27176
pdf_url: https://arxiv.org/pdf/2610.27176
published: '2026-10-19'
collected: '2026-10-21'
category: Agent
direction: Agent 2D画布编辑观测增强
tags:
- Agent
- Structured Observation
- 2D Canvas
- GUI Agent
- Agent Evaluation
one_liner: 为2D无限画布编辑Agent新增结构化观测层，无需改动现有编辑管线即可大幅提升目标选择准确率
practical_value: '- 开发GUI交互Agent（如电商作图工具Agent、后台运营Agent）时，不要纯依赖视觉输入，可补充界面元数据（对象ID、隐藏状态、层级、绑定关系），能大幅降低操作错误率

  - 处理跨视口操作场景时，可提前返回屏外对象的动作坐标系边界，避免Agent重复创建对象或定位失效，适合大屏/无限画布类工具的Agent开发

  - 评估Agent任务时可拆分「目标选择正确率」「放置正确率」「全任务成功率」三个指标，分别定位观测、动作执行环节的瓶颈，避免整体评估掩盖问题

  - 做Agent能力增强时，优先优化输入侧的观测信息，无需改动下游规划、执行管线就能拿到明显收益，ROI更高'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
2D无限画布是当下主流的可拖拽编辑工作区，编辑Agent仅靠截图识别对象时，会遇到目标被遮挡、处于屏外、视觉布局和原生结构不一致（如箭头仅触碰未绑定、视觉包含但不属于同一帧）等问题，极易选错编辑对象，现有方案未将原生文档的结构化状态与视觉上下文有效结合。

### 方法关键点
- 新增4类结构化观测信息：①对象身份与状态：ID、内容、样式、层级、编辑状态；②可见性与结构：区分可见/部分可见/遮挡/屏外状态，标注原生层级关系；③关联关系：原生绑定（箭头端点、从属帧）和推理的空间关系（重叠、对齐）分开标注；④屏外对象的动作坐标系边界。
- 无需改动原有编辑管线，仅在prompt中追加结构化观测数据和解读指南，与原有截图、基础形状摘要共存。
- 观测信息按优先级排序：选中/上下文/部分可见对象 > 视口内对象 > 关联对象 > 屏外对象，控制token开销。

### 关键实验
基于tldraw画布实现，构造10种隐藏状态场景（屏外对象选择、遮挡对象选择、层级区分、绑定关系区分），对比基线（仅截图+基础形状摘要），用3个模型跑1200次浏览器测试：整体目标选择正确率从16.5%提升到48.3%，提升31.8个百分点；全任务成功率从4.3%提升到25%，提升20.7个百分点；越强的模型收益越高，Claude Sonnet 4.5的目标选择正确率提升65个百分点；新增结构化数据仅76kB，单趟请求耗时仅增加0.5秒以内。

### 最值得记住的一句话
对于GUI交互类Agent，输入侧的结构化信息增强往往比优化规划、执行模块的ROI高得多，无需改动现有管线就能拿到显著效果。
