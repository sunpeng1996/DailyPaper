---
title: 'OACap: Caption-Guided Active Observation for Detailed Video Captioning'
title_zh: OACap：字幕引导的主动观察细粒度视频字幕生成方法与评估基准
authors:
- Hao Shi
- Hong Yan
- Xiaoyang Zhang
- Qing Cui
- Chao Huang
affiliations:
- Ant Group
- Zhejiang University
- Peking University
arxiv_id: '2610.29327'
url: https://arxiv.org/abs/2610.29327
pdf_url: https://arxiv.org/pdf/2610.29327
published: '2026-10-21'
collected: '2026-10-22'
category: Agent
direction: Agent 主动观测 · 多模态内容生成评估
tags:
- Video Captioning
- Active Perception
- Multimodal Agent
- Evaluation Metric
- Factual Consistency
one_liner: 提出字幕引导的主动观察视频字幕Agent OACap，及事实语义字幕评估基准FSCap-Bench
practical_value: '- 电商短视频/直播内容结构化场景，可复用OACap的「生成草稿→诊断gap→工具补全→迭代修正」闭环逻辑，替代一次性生成，降低字幕幻觉、遗漏商品核心信息的问题

  - 生成式内容效果评估可借鉴CSFS设计：将输出拆分为原子claim，区分核心业务事实和辅助信息，加权计算精度与覆盖率，解决传统生成指标无法区分幻觉、核心信息遗漏的痛点

  - 多模态Agent调度可参考gap分类逻辑：区分可通过已有证据修正的问题和需要调用工具的问题，减少无效工具调用，平衡生成质量与推理成本'
score: 8
source: arxiv-cs.MM
depth: full_pdf
---

### 动机
现有细粒度视频字幕生成多采用单轮全局处理，易遗漏小物体、短时动作、长时序关系；开放无查询场景下没有明确的信息获取目标，纯文本修正无法恢复未观测事实，现有工具增强方法多依赖外部查询，无法适配无明确任务的内容结构化场景；同时现有字幕评估指标无法同时衡量事实准确性、核心信息覆盖率，也无法衡量字幕的跨模态语义可恢复性。

### 方法关键点
- OACap Agent架构：以迭代生成中的字幕为控制信号，诊断缺失、不实、冲突、时序不明确四类gap，区分可通过现有证据修正的revision gap和需要调用工具的observation gap
- 针对性工具调用：针对不同gap调用动态帧采样、裁剪、OCR、外部搜索等工具，返回证据后迭代修正字幕，直到gap解决或预算耗尽
- FSCap-Bench评估基准：包含498个多场景筛选视频，配套人工标注的核心/辅助事实集，设计CSFS（加权计算事实精度、核心/辅助事实覆盖率）和CSRS（视频-字幕跨模态循环得分）两个评估指标

### 关键结果
匹配5种多模态骨干，OACap相对单轮生成在Video-MME准确率最高提升9.17%，ActivityNet-QA准确率最高提升1.83%，VCapsBench答案召回率最高提升1.02%；CSFS在四类受控扰动下方向准确率达93.0%~98.3%，优于所有对比指标；OACap在FSCap-Bench上CSFS最高提升20.75个百分点。

> 最值得记住的结论：结构化内容生成可将生成草稿本身作为主动感知的控制信号，通过「生成-校验-补全」闭环大幅提升内容的事实准确性和信息密度
