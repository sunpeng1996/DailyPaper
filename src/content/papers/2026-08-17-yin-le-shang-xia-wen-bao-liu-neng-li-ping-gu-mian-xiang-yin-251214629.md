---
title: 'Evaluating Music Context Preservation: A Multi-facet Framework for Music Editing
  Systems'
title_zh: 音乐上下文保留能力评估：面向音乐编辑系统的多维度框架
authors:
- Yash Vishe
- Eric Xue
- Xunyi Jiang
- Zachary Novack
- Junda Wu
- Julian McAuley
- Xin Xu
affiliations:
- University of California, San Diego
arxiv_id: '2512.14629'
url: https://arxiv.org/abs/2512.14629
pdf_url: https://arxiv.org/pdf/2512.14629
published: '2026-08-17'
collected: '2026-08-23'
category: Other
direction: 音乐编辑评估 · 多维度指标体系
tags:
- Music Editing
- Evaluation Framework
- Context Preservation
- Fine-grained Metrics
- Audio Processing
one_liner: 提出首个覆盖四类音乐维度的上下文保留评估框架MuseCPEval，可诊断现有音乐编辑系统能力
practical_value: '- 多维度上下文保留的评估设计思路可迁移到GenRec场景，比如生成商品营销文案时保留核心卖点、参数等非修改属性不偏移

  - 「客观指标对齐人类感知」的验证方法可复用在所有生成类推荐系统的新评测体系搭建中，降低评测偏差

  - 以评测框架作为诊断工具定位系统短板的思路，可用于快速迭代推荐系统的生成模块、内容改写模块性能'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
现有音乐编辑系统已支持音色转换、乐器替换、风格迁移等任务，但普遍缺乏对编辑过程中非目标修改的核心音乐属性保留能力（即MuseCP）的系统性评估，已有相关评测的协议和指标完备性严重不足。
### 方法关键点
提出首个MuseCP专项评估框架MuseCPEval，覆盖和声、节奏、结构等四大类音乐核心维度，设计细粒度定制化指标，可精准捕捉音乐属性的细微非预期变化，配套完整的评测执行协议。
### 关键结果
客观验证和人类评测一致性较高，证明指标有效性；在多类主流音乐编辑系统上的案例研究显示，该框架可作为测试床和诊断工具，清晰定位不同系统的优劣势，为系统迭代提供明确方向。
