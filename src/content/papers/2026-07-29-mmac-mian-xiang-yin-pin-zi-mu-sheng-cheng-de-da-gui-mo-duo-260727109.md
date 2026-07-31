---
title: 'MMAC: A Massive Multi-dimensional Benchmark for Audio Captioning'
title_zh: MMAC：面向音频字幕生成的大规模多维度评测基准
authors:
- Weijie Wu
- Junbo Li
- Lin Li
- Jun Fang
- Qingyang Hong
affiliations:
- Xiamen University
- DiDi Global Inc.
arxiv_id: '2607.27109'
url: https://arxiv.org/abs/2607.27109
pdf_url: https://arxiv.org/pdf/2607.27109
published: '2026-07-29'
collected: '2026-07-31'
category: Eval
direction: AudioLLM 细粒度多维度音频字幕评测
tags:
- AudioLLM
- Evaluation Benchmark
- Audio Captioning
- Fine-grained Evaluation
- Multimodal
one_liner: 构建覆盖6类能力15个维度的音频字幕评测基准，可诊断生成内容的信息覆盖度与可靠性
practical_value: '- 做音视频内容理解类Agent的生成效果评测时，可复用「分维度校验信息覆盖+内容一致性」的评估框架，避免只依赖单一生成质量指标导致的评估偏差

  - 做多模态电商内容（如短视频/直播带货商品）的字幕、标签生成评测时，可参考该基准的多维度能力拆解思路，针对业务场景自定义评估维度

  - 内部自研多模态生成模型时，可借鉴该基准的自动化评估逻辑，自动定位生成结果的信息遗漏与事实错误，降低人工标注评估成本'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
AudioLLM快速发展推动音频字幕从简短描述转向开放细粒度自由表述，现有评测仅聚焦生成质量或整体任务性能，无法有效诊断生成内容的信息覆盖度与描述可靠性。
### 方法关键点
1. 构建MMAC评测基准，包含5638条来自20+数据源的音频片段，覆盖6类能力、15个评估维度；
2. 采用双维度校验逻辑：先检查生成字幕是否提及目标维度的相关信息，再校验提及内容与参考标签的一致性。
### 关键结果
对主流开源及闭源AudioLLM的评测显示，不同模型在各评估维度、信息覆盖度、描述可靠性上的表现存在显著差异，可有效区分模型能力梯队。
